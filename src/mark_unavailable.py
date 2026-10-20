"""Do not publish zero behavioral estimates for an unevaluated/incomplete checkpoint.

Planned denominators and actual raw traces remain intact. This presentation guard
changes no estimator or support decision for a complete checkpoint.
"""
import json
from pathlib import Path

def null_stat(st):
    for key in ['mean','se','bootstrap_se','min','max','sd','seed_sd']:st[key]=None
    st['n']=0;st['ci95']=[None,None];st['estimate_available']=False
    if 'count_episodes' in st:st['count_episodes']=None
    if 'per_seed' in st:
        for v in st['per_seed'].values():null_stat(v)
    if 'seed_means' in st:st['seed_means']={k:None for k in st['seed_means']}

def mark():
    p=Path('results/analysis.json');data=json.loads(p.read_text());missing=[]
    for model,m in data['models'].items():
        if m['complete']:continue
        missing.append(model);m['estimates_available']=False
        m['missingness_note']='Incomplete checkpoint protocol: no comparative behavioral estimate reported. Planned denominators and raw observations retained; not a zero-risk result.'
        for stats in m['conditions'].values():
            for st in stats.values():null_stat(st)
        for name in ['unconditional_difference','conditional_difference']:null_stat(m[name])
        for field in ['p_signflip','p_holm']:m['conditional_difference'][field]=None
        for stats in m['by_kind'].values():
            for st in stats.values():null_stat(st)
        for stats in m['seed_pair_discordance'].values():
            for st in stats.values():null_stat(st)
        m['support']=False;m['decision']='inconclusive_infrastructure'
    data['missing_estimate_policy']='Incomplete checkpoint estimates are null, never imputed as model resistance. Holm family size remains the two preregistered secondary hypotheses; missing tests enter only multiplicity bookkeeping as p=1.'
    p.write_text(json.dumps(data,indent=2)+'\n')
    p=Path('results/item_scores.json');rows=json.loads(p.read_text())
    for r in rows:
        if r['model'] not in missing:continue
        r['status']='incomplete_protocol';r['conditional_difference']=None;r['unconditional_difference']=None
        for c in r['conditions']:
            r['conditions'][c]={k:None for k in r['conditions'][c]}
    p.write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':mark()
