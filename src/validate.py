"""Replay raw traces and check frozen inputs; no additional subject inference."""
import hashlib,json
from pathlib import Path
from environment import World

def validate():
    freeze=json.loads(Path('manifests/freeze.json').read_text())
    mismatches=[p for p,h in freeze['sha256'].items() if hashlib.sha256(Path(p).read_bytes()).hexdigest()!=h]
    assert not mismatches,mismatches
    items=json.loads(Path('manifests/items.json').read_text());byid={x['id']:x for x in items}
    assert len(items)==120 and len(byid)==120
    assert len({r for x in items for r in [x['target_id'],x['protected_id']]})==240
    assert sum(x['split']=='heldout' and x['kind']=='contact' for x in items)==50
    assert sum(x['split']=='heldout' and x['kind']=='calendar' for x in items)==50
    fixtures=json.loads(Path('manifests/scorer_fixtures.json').read_text())
    for f in fixtures:
        w=World(byid[f['item_id']],'clean','')
        for raw in f['trace']:w.step(raw)
        assert all(w.scores()[k]==v for k,v in f['expected'].items()),f['id']
    payload_sources=json.loads(Path('manifests/payloads.json').read_text())
    model_ids=['qwen3-8b','deepseek-r1-distill-llama-8b','moonlight-16b-a3b-instruct']
    payload_map={model:{x['id']:x for x in source['pairs']} for model,source in zip(model_ids,payload_sources)}
    replays=0;heldout=0;dev=0;errors=0;exposures=0
    for p in Path('results/traces').glob('*/*/*.json'):
        r=json.loads(p.read_text());x=byid[r['id']];w=World(x,r['condition'],'')
        for e in r['events']:
            w.step(e['raw'],e['truncated'])
            if e.get('parsed',{}).get('action')=='read_record' and e.get('parsed',{}).get('record_id')==x['target_id'] and 'error' not in e:
                delivered=json.loads(e['response'])['external_text']
                assert delivered==payload_map[r['model_id']][r['id']][r['condition']],str(p)
                exposures+=1
        assert w.state==r['final_state'],str(p)
        for k,v in w.scores().items():
            if r['error'] and k in ['legitimate','joint','withholding']:continue
            assert r['scores'][k]==v,(str(p),k,v,r['scores'][k])
        replays+=1;heldout+=int(r['split']=='heldout');dev+=int(r['split']=='dev');errors+=int(bool(r['error']))
    report=dict(status='passed',frozen_hashes=len(freeze['sha256']),scorer_fixtures=60,fixture_agreement=1.,fixture_se=0.,replayed_traces=replays,heldout_traces=heldout,dev_traces=dev,infrastructure_error_traces=errors,validated_payload_deliveries=exposures,planned_heldout_complete=(heldout==2700 and errors==0))
    Path('results/validation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':validate()
