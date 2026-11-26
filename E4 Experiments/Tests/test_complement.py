"""Bounded CPU-only publication checks; no training or biometric images."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

import cv2
import numpy as np
import pandas as pd
import torch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('complement_inputs',ROOT/'Code/complement_inputs.py')
INPUTS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INPUTS)


class ComplementTests(unittest.TestCase):
    def setUp(self):
        self.geometry=dict(content_width=320,content_height=213,pad_left=0,pad_right=0,pad_top=53,pad_bottom=54)
        y,x=np.mgrid[:480,:720]
        self.annulus=((x-360)**2+(y-240)**2<150**2)&((x-355)**2+(y-238)**2>45**2)
        self.old=cv2.copyMakeBorder(cv2.resize(self.annulus.astype('uint8'),(320,213),interpolation=cv2.INTER_NEAREST_EXACT),53,54,0,0,cv2.BORDER_CONSTANT,value=0)>0
        self.mask,self.fraction=INPUTS.removal_mask(self.annulus,self.geometry,self.old)

    def test_strict_footprint_and_original_geometry(self):
        self.assertTrue(np.array_equal(self.mask,self.old|(self.fraction>0)))
        self.assertFalse(((self.fraction>0)&~self.mask).any())
        self.assertFalse((self.mask&~INPUTS.content_mask(self.geometry)).any())

    def test_exact_mean_fill_and_unchanged_other_samples(self):
        pixels=np.random.default_rng(42).integers(0,256,(320,320),dtype='uint8')
        raw=(torch.from_numpy(pixels[None]).float()/255-INPUTS.NORMALIZATION['mean'])/INPUTS.NORMALIZATION['std']
        out=INPUTS.tensor_from_pixels(pixels,self.mask,INPUTS.content_mask(self.geometry))
        self.assertTrue(torch.all(out[:,self.mask]==0))
        self.assertTrue(torch.equal(out[:,~self.mask],raw[:,~self.mask]))

    def test_discarded_texture_cannot_affect_contrast(self):
        a=np.full((320,320),113,np.uint8);b=a.copy();a[self.mask]=0;b[self.mask]=255
        def contrast(x):return ((x-x.mean())*.91+x.mean()).clamp(0,1)
        first=INPUTS.tensor_from_pixels(a,self.mask,INPUTS.content_mask(self.geometry),contrast)
        second=INPUTS.tensor_from_pixels(b,self.mask,INPUTS.content_mask(self.geometry),contrast)
        self.assertTrue(torch.equal(first,second))
        self.assertTrue(torch.all(first[:,self.mask]==0))

    def test_wrong_cache_shape_is_rejected(self):
        with self.assertRaises(ValueError):
            INPUTS.tensor_from_pixels(np.zeros((256,256),np.uint8),self.mask,INPUTS.content_mask(self.geometry))

    def test_mask_join_preserves_partitions_and_ids(self):
        records=[dict(image_id='a',split='train'),dict(image_id='b',split='validation'),dict(image_id='c',split='test')]
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'manifest.parquet'
            pd.DataFrame([dict(image_id='a',split='train',removal_mask_path='a.png'),dict(image_id='b',split='validation',removal_mask_path='b.png')]).to_parquet(path)
            out=INPUTS.attach_removal_masks(records,path,directory)
            self.assertEqual([r['image_id'] for r in out],['a','b','c'])
            self.assertNotIn('e4_removal_mask_path',out[2])
            self.assertNotIn('e4_removal_mask_path',records[0])
            pd.DataFrame([dict(image_id='c',split='test',removal_mask_path='c.png')]).to_parquet(path)
            with self.assertRaises(ValueError):INPUTS.attach_removal_masks(records,path,directory)


if __name__=='__main__':unittest.main()
