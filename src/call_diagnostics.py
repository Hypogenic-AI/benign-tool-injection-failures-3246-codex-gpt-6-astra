"""Descriptive per-call failure rates with a scenario-cluster bootstrap."""
import json
from pathlib import Path
import numpy as np
from analyze import MODELS,CONDS

def diagnostics():
    items=[x['id'] for x in json.loads(Path('manifests/items.json').read_text()) if x['split']=='heldout'];idx={x:i for i,x in enumerate(items)}
    boot=np.random.default_rng(20261020).integers(0,100,(10000,100));out={}
    for model in MODELS:
        out[model]={}
        for condition in CONDS:
            calls=np.zeros(100);malformed=np.zeros(100);truncated=np.zeros(100);tokens=np.zeros(100)
            errors={}
            for p in (Path('results/traces')/model/'heldout').glob(f'*__{condition}__*.json'):
                r=json.loads(p.read_text());i=idx[r['id']];calls[i]+=len(r['events'])
                for e in r['events']:
                    malformed[i]+=int('error' in e);truncated[i]+=int(e['truncated'])
                    if 'error' in e:errors[e['error']]=errors.get(e['error'],0)+1
                tokens[i]+=sum(u.get('output_tokens',0) for u in r['usage'])
            entry={'n_base_items':100,'n_calls':int(calls.sum()),'output_tokens':int(tokens.sum()),'parse_error_counts':errors}
            for name,num in [('malformed',malformed),('truncated',truncated)]:
                if calls.sum()==0:entry[name]={'n':0,'mean':None,'se':None,'ci95':[None,None],'count':0};continue
                b=num[boot].sum(axis=1)/calls[boot].sum(axis=1)
                entry[name]={'n':100,'mean':float(num.sum()/calls.sum()),'se':float(b.std(ddof=1)),'ci95':[float(x) for x in np.quantile(b,[.025,.975])],'count':int(num.sum())}
            out[model][condition]=entry
    Path('results/call_diagnostics.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':diagnostics()
