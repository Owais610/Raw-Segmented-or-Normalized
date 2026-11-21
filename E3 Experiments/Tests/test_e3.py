"""CPU-only publication checks; no training, inference or licensed pixels needed."""
import ast
import copy
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

import cv2
import numpy as np
import pandas as pd
import torch


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
NOTEBOOKS = sorted((ROOT / 'Training Codes').glob('*.ipynb'))


def sources(path):
    book = json.loads(path.read_text(encoding='utf8'))
    return [''.join(c['source']) for c in book['cells'] if c['cell_type']=='code']


def definitions(path):
    namespace = {'__name__':__name__}
    for source in sources(path):
        if source.startswith('configurations =') or source.startswith('if SHOW_RECORDED_RESULTS:'):
            break
        exec(compile(source,str(path),'exec'),namespace)
    return namespace


def named_definitions(path):
    return {node.name:ast.dump(node,include_attributes=False)
        for source in sources(path) for node in ast.parse(source).body
        if isinstance(node,(ast.FunctionDef,ast.ClassDef))}


def row(index=0, split='train'):
    return dict(image_id=f'CUST-Iris:001:L:{index}',dataset='CUST-Iris',subject_id='001',
        eye_side='L',iris_id='CUST-Iris:001:L',source_id=f'source{index}',split=split,
        raw_path='DO_NOT_OPEN_OCULAR.png',native_path='DO_NOT_OPEN_NATIVE.png')


class E3PublicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.train = definitions(ROOT/'Training Codes/ResNet-18_B1-binary.ipynb')
        cls.evaluation = definitions(ROOT/'Evaluation.ipynb')
        cls.evaluation['E3_CHECKPOINT_INDEX']=REPO/'Assets/e3_checkpoints.json'

    def test_imports_at_top_and_execution_is_opt_in(self):
        self.assertEqual(len(NOTEBOOKS),4)
        for path in [*NOTEBOOKS,ROOT/'Evaluation.ipynb']:
            code=sources(path)
            compile('\n'.join(code),str(path),'exec')
            self.assertTrue(any(isinstance(x,(ast.Import,ast.ImportFrom)) for x in ast.walk(ast.parse(code[0]))))
            for cell in code[1:]:
                self.assertFalse(any(isinstance(x,(ast.Import,ast.ImportFrom)) for x in ast.walk(ast.parse(cell))))
            self.assertIsNone(re.search(r'[A-Z]:[\\/](?:Users|data)', '\n'.join(code)))
        self.assertFalse(self.train['RUN_TRAINING'])
        self.assertFalse(self.train['CHECK_REAL_ASSETS'])
        self.assertFalse(self.evaluation['RUN_ANALYSIS'])

    def test_scientific_training_functions_equal_existing_e1(self):
        for path in NOTEBOOKS:
            architecture='SwinV2-Tiny' if path.name.startswith('Swin') else 'ResNet-18'
            baseline=REPO/architecture/'Training Codes/E1-B1_Cartesian_Unmasked.ipynb'
            old,new=named_definitions(baseline),named_definitions(path)
            for name in new:
                if name!='data_IrisDataset':
                    self.assertEqual(new[name],old[name],(path.name,name))

    def test_binary_loading_exactly_matches_e2_without_ocular_paths(self):
        ns=self.train
        with tempfile.TemporaryDirectory() as directory:
            pixels=np.zeros((320,320),np.uint8)
            pixels[40:260,50:250]=255
            pixels[100:180,110:190]=0
            mask=Path(directory)/'support.png'
            self.assertTrue(cv2.imwrite(str(mask),pixels))
            for support in ('B1','B2'):
                r=row();r[support.lower()+'_support_path']=str(mask)
                cfg=ns['config_frozen_config']('ResNet-18','E1-'+support)
                cfg['augmentation']['enabled']=False
                dataset=ns['data_IrisDataset']([r],cfg,split='train',augment=True)
                actual=dataset[0]['image']
                expected=self.evaluation['binary_tensor'](pixels==255)
                self.assertTrue(torch.equal(actual,expected))
                self.assertEqual(actual.shape,(1,320,320))
                self.assertEqual(actual.dtype,torch.float32)
                self.assertEqual(actual.unique().numel(),2)
                self.assertNotIn('raw_path',dataset.records[0])
                self.assertNotIn('native_path',dataset.records[0])
                self.assertIsNone(dataset.augmentation)
            cv2.imwrite(str(mask),np.full((320,320),127,np.uint8))
            with self.assertRaisesRegex(ValueError,'binary mask'):
                dataset[0]
            with self.assertRaisesRegex(ValueError,'train/validation'):
                ns['data_IrisDataset']([dict(r,split='test')],cfg,split='test')
            cfg['augmentation']['enabled']=True
            with self.assertRaisesRegex(ValueError,'strictly binary'):
                ns['data_IrisDataset']([r],cfg,split='train',augment=True)

    def test_evaluation_loader_and_metric_definitions_equal_e2_g(self):
        old=named_definitions(REPO/'E2 Experiments/E2-G/E2-G.ipynb')
        new=named_definitions(ROOT/'Evaluation.ipynb')
        for name in ('binary_tensor','GeometryDataset','aligned_inputs','validate_pairs','pair_scores',
                     'summary','infer','metric_artifacts','metrics_verification_metrics'):
            self.assertEqual(old[name],new[name],name)

    def test_frozen_configuration_snapshots_all_twelve_runs(self):
        jobs=json.loads((REPO/'Assets/e3_checkpoints.json').read_text())['jobs']
        self.assertEqual(len(jobs),12)
        self.assertEqual(len({(j['architecture'],j['condition'],j['seed']) for j in jobs}),12)
        for job in jobs:
            old=self.train['config_frozen_config'](job['architecture'],job['reference_condition'],job['seed'])
            expected=copy.deepcopy(old)
            expected['augmentation']['enabled']=False
            for key in ('augmentation','sampler','objective','optimizer','runtime','schedule','logging'):
                self.assertEqual(expected[key],job['config'][key],(job['name'],key))
            self.assertEqual(job['config']['data']['representation'],job['condition'])
            self.assertTrue(job['config']['e3']['independent_pretrained_initialization'])
            self.assertEqual(len(job['checkpoint_sha256']),64)

    def test_saved_embedding_orchestration_without_images_or_gpu(self):
        ns=self.evaluation
        jobs=ns['e3_jobs']()
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            populations={}
            for dataset in ns['DATASETS']:
                rows=[]
                for subject in ('001','002'):
                    for eye in ('L','R'):
                        for capture in (0,1):
                            image_id=f'{dataset}:{subject}:{eye}:{capture}'
                            rows.append(dict(image_id=image_id,dataset=dataset,subject_id=subject,eye_side=eye,
                                iris_id=f'{dataset}:{subject}:{eye}',source_id=image_id,
                                split='test' if dataset in ns['ORIGINAL_DATASETS'] else 'external'))
                pairs={k:[] for k in ns['KINDS']}
                for i,a in enumerate(rows):
                    for b in rows[i+1:]:
                        kind='genuine' if a['iris_id']==b['iris_id'] else (
                            'impostor' if a['subject_id']!=b['subject_id'] else 'opposite_eye_diagnostic')
                        pairs[kind].append(dict(pair_id=f'{dataset}:{kind}:{len(pairs[kind])}',
                            image_id_a=a['image_id'],image_id_b=b['image_id']))
                members=pd.DataFrame(rows)
                populations[dataset]=(members,{k:pd.DataFrame(v) for k,v in pairs.items()},rows)
                vectors=np.zeros((8,256),np.float32)
                for i in range(8):vectors[i,i//2]=1;vectors[i,4+i]=0.01
                vectors/=np.linalg.norm(vectors,axis=1,keepdims=True)
                for job in jobs:
                    target=root/'embeddings'/dataset/job['name']
                    target.mkdir(parents=True)
                    np.savez_compressed(target/'embeddings.npz',image_ids=members.image_id.to_numpy(dtype=str),
                        embeddings=vectors)
            forbidden=lambda *a,**k: self.fail('Synthetic saved-embedding replay attempted GPU inference')
            with patch.dict(ns,OUTPUT_ROOT=root/'outputs',E3_EMBEDDING_ROOT=root/'embeddings',
                INFERENCE_SOURCE='saved_embeddings',aligned_inputs=lambda d:populations[d],
                load_e3_model=forbidden,infer=forbidden),redirect_stdout(io.StringIO()):
                frame=ns['evaluate_e3']()
            self.assertEqual(len(frame),60)
            self.assertTrue(frame.eer.eq(0).all())
            self.assertTrue(frame.roc_auc.eq(1).all())
            self.assertTrue(frame.num_genuine.eq(4).all())
            self.assertTrue(frame.num_impostor.eq(16).all())
            self.assertEqual(len(list((root/'outputs').rglob('metrics.json'))),60)


if __name__=='__main__':
    unittest.main()
