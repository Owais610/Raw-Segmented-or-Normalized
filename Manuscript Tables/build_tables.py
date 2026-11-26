"""Reproduce manuscript III–VI and supplementary S1–S2 from public seed records."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import statistics

import pandas as pd

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
DATASETS = ('CUST-Iris','CASIA-Interval','IITD','AMF','UTIRIS_NIR')
ARCHITECTURES = ('ResNet-18','SwinV2-Tiny')
SEEDS = (42,123,2025)
METRICS = ('eer','roc_auc','tar_at_far_1pct','tar_at_far_0_1pct')
MATH = r'\$([+-]?\d+\.\d{2})\s*\\pm\s*(\d+\.\d{2})\$'
CELL = re.compile(r'\{\\boldmath\s+'+MATH+r'\}|'+MATH)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def display(value,signed=False):
    result = f'{value:+.2f}' if signed else f'{value:.2f}'
    return '0.00' if result in ('-0.00','+0.00') else result


def seed_values(frame,metric):
    assert len(frame)==3 and set(frame.seed)==set(SEEDS),'Use all three seeds'
    values=frame.set_index('seed')[metric]
    return [float(values[s]) for s in SEEDS]


def build(output):
    output=Path(output).resolve()
    if output.exists() and any(output.iterdir()):
        raise FileExistsError('Choose a fresh output directory; recorded tables are never overwritten')
    output.mkdir(parents=True,exist_ok=True)
    sources={}
    def load(relative):
        path=REPO/relative;sources[relative]=sha(path)
        return pd.read_csv(path,float_precision='round_trip')
    primary=load('E2 Experiments/E2-A/Results/individual_metrics.csv')
    assert len(primary)==150 and set(primary.population)=={'common eligibility'}
    frames={s:load(f'E2 Experiments/E2-{s.upper()}/Results/individual_metrics.csv') for s in ('c','d','e','g')}
    frames['e3']=load('E3 Experiments/Results/individual_metrics.csv')
    frames['e4']=load('E4 Experiments/Results/individual_metrics.csv')
    logical=[];seed_rows=[]
    def add(stage,condition,before_input,after_input,architecture,dataset,before,after):
        record=dict(stage=stage,condition=condition,baseline_input=before_input,input=after_input,
                    architecture=architecture,dataset=dataset)
        by_seed={s:dict(record,seed=s) for s in SEEDS}
        for metric in METRICS:
            post=seed_values(after,metric)
            pre=seed_values(before,metric) if before is not None else [None]*3
            values=[b-a if a is not None else b for a,b in zip(pre,post)]
            record[metric+'_mean']=statistics.mean(values)
            record[metric+'_sample_sd']=statistics.stdev(values)
            for s,a,b,v in zip(SEEDS,pre,post,values):
                by_seed[s].update({metric+'_before':a,metric+'_after':b,metric+'_value':v})
        logical.append(record);seed_rows.extend(by_seed[s] for s in SEEDS)
    for condition in ('E1-A','E1-B1','E1-B2','E1-C1','E1-C2'):
        for architecture in ARCHITECTURES:
            for dataset in DATASETS:
                g=primary[primary.condition.eq(condition)&primary.architecture.eq(architecture)&primary.dataset.eq(dataset)]
                add('a',condition,'',condition,architecture,dataset,None,g)
    comparisons=[('c','E1-C1','E1-C1','E1-C2'),('c','E1-C2','E1-C2','E1-C1')]
    comparisons += [('d','E1-A',f'q{q}_{side}_periocular',f'q{q}_{side}_iris') for q in ('05','10') for side in ('left','right')]
    comparisons += [('e','E1-A','A_A',v) for v in ('A_B1_black','A_B2_black','A_B1_mean','A_B2_mean','A_nonannulus_black','A_nonannulus_mean')]
    comparisons += [('e4','A-complement-mean-strict','E1-A','A-complement-mean-strict')]
    comparisons += [('g',c,'segmented_grayscale','binary_geometry') for c in ('E1-B1','E1-B2')]
    comparisons += [('e3',c,'E1-'+c[:2],c) for c in ('B1-binary','B2-binary')]
    for stage,condition,before_input,after_input in comparisons:
        for architecture in ARCHITECTURES:
            for dataset in DATASETS:
                g=frames[stage];g=g[g.architecture.eq(architecture)&g.dataset.eq(dataset)]
                if stage in ('e3','e4'):
                    after=g[g.condition.eq(condition)]
                    before=primary[primary.architecture.eq(architecture)&primary.dataset.eq(dataset)&primary.condition.eq(before_input)]
                else:
                    if stage in ('c','g'):g=g[g.condition.eq(condition)]
                    key='input_condition' if stage=='c' else 'variant'
                    before=g[g[key].eq(before_input)];after=g[g[key].eq(after_input)]
                add(stage,condition,before_input,after_input,architecture,dataset,before,after)
    assert len(logical)==220 and len(seed_rows)==660
    templates=json.loads((HERE/'table_templates.json').read_text(encoding='utf8'))
    sources['Manuscript Tables/table_templates.json']=sha(HERE/'table_templates.json')
    rendered={};cells=[]
    settings=(('III','eer',True),('IV','tar_at_far_0_1pct',True),('V','eer',False),
              ('VI','tar_at_far_0_1pct',False),('S1','tar_at_far_1pct',True),('S2','tar_at_far_1pct',False))
    for number,metric,absolute in settings:
        group=logical[:50] if absolute else logical[50:]
        template=templates[number]
        matches=list(CELL.finditer(template));assert len(matches)==len(group)
        values=[]
        for i,(match,r) in enumerate(zip(matches,group)):
            mean=r[metric+'_mean']*100;sd=r[metric+'_sample_sd']*100
            shown=(display(mean,not absolute),f'{sd:.2f}')
            existing=next(p for p in (match.groups()[:2],match.groups()[2:]) if p[0] is not None)
            assert existing==shown,(number,r,existing,shown)
            bold=False
            if absolute:
                other=next(x for x in group if x['condition']==r['condition'] and x['dataset']==r['dataset'] and x['architecture']!=r['architecture'])
                bold=mean<=other[metric+'_mean']*100 if metric=='eer' else mean>=other[metric+'_mean']*100
            formula='$'+shown[0]+(r' \pm ' if absolute else r'\pm')+shown[1]+'$'
            values.append(r'{\boldmath '+formula+'}' if bold else formula)
            cells.append(dict(table=number,metric=metric,**r,display_mean=shown[0],display_sample_sd=shown[1],bold=bold))
        values=iter(values)
        rendered[number]=CELL.sub(lambda m:next(values),template)
    (output/'main_tables.tex').write_text('\n\n'.join(rendered[t] for t in ('III','IV','V','VI'))+'\n',encoding='utf8')
    (output/'supplementary_tar1_tables.tex').write_text('\n\n'.join(rendered[t] for t in ('S1','S2'))+'\n',encoding='utf8')
    pd.DataFrame(logical).to_csv(output/'all_metrics_summary.csv',index=False,float_format='%.17g')
    pd.DataFrame(seed_rows).to_csv(output/'all_metrics_seed_values.csv',index=False,float_format='%.17g')
    pd.DataFrame(cells).to_csv(output/'displayed_cells.csv',index=False,float_format='%.17g')
    for filename,supplement in (('main_tables',False),('supplementary_tar1',True)):
        wrapper='\\documentclass[journal,10pt]{IEEEtran}\n\\usepackage{booktabs,multirow}\n\\pagestyle{empty}\n'
        wrapper+=r'\renewcommand{\thetable}{S\arabic{table}}'+'\n' if supplement else r'\setcounter{table}{2}'+'\n'
        table_file='supplementary_tar1_tables' if supplement else 'main_tables'
        wrapper+='\\begin{document}\n\\input{'+table_file+'}\n\\clearpage\n\\end{document}\n'
        (output/(filename+'.tex' if supplement else 'main_tables_preview.tex')).write_text(wrapper,encoding='utf8')
    report=dict(status='PASS',seeds=list(SEEDS),sample_sd_ddof=1,logical_comparisons=220,seed_records=660,
        displayed_mean_sd_cells=660,tables=['III','IV','V','VI','S1','S2'],source_sha256=sources,
        metric_units='Stored metrics and deltas are ratios; EER/TAR LaTeX cells are percent or percentage points. ROC-AUC remains unitless.',
        regional_difference='iris-occluded minus periocular-occluded, not unoccluded-baseline change',
        training=False,inference=False)
    (output/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
    assert all(sha(REPO/p)==h for p,h in sources.items())
    print(json.dumps({k:report[k] for k in ('status','displayed_mean_sd_cells','logical_comparisons','seed_records')},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=REPO/'reproduced_outputs/paper_tables')
    build(parser.parse_args().output)
