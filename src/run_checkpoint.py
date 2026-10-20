"""Run one locally served checkpoint through Inspect, clean first then paired arms."""
import argparse,json,os,sys,time
from pathlib import Path
os.environ['XDG_DATA_HOME']=str(Path('.cache/data').resolve())
os.environ['XDG_CACHE_HOME']=str(Path('.cache').resolve())
sys.path.insert(0,str(Path(__file__).resolve().parent))
from inspect_ai import eval
from evals.benign_tool_injection import benign_tool_injection

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('model');p.add_argument('--port',type=int,default=8765);p.add_argument('--dev',action='store_true');a=p.parse_args()
    os.environ['LOCAL_BASE_URL']=f'http://127.0.0.1:{a.port}/v1';os.environ['LOCAL_API_KEY']='local-unused'
    model_args={'stream':False}
    outputs=[]
    for condition in (['all'] if a.dev else ['clean','quoted','injected']):
        logs=eval(benign_tool_injection(model_id=a.model,split='dev' if a.dev else 'heldout',condition=condition,limit_items=2 if a.dev else 0),
          model='openai-api/local/'+a.model, model_args=model_args,
          log_dir='results/safety/inspect_logs',log_format='json',max_connections=64,max_samples=64,
          temperature=.6,top_p=1,max_tokens=1024,max_retries=0,extra_body={'top_k':-1,'chat_template_kwargs':{'enable_thinking':False} if a.model=='qwen3-8b' else {}},display='plain',fail_on_error=False)
        outputs.extend([{'location':l.location,'status':l.status,'condition':condition} for l in logs])
        Path(f'results/{a.model}'+('_dev' if a.dev else '')+'_logs.json').write_text(json.dumps(outputs,indent=2))
        if any(l.status!='success' for l in logs): raise RuntimeError('Inspect task failed; see logs')
        if condition=='clean':
            eligible={str(seed):[] for seed in [11,22,33]}
            for path in (Path('results/traces')/a.model/'heldout').glob('*__clean__*.json'):
                row=json.loads(path.read_text())
                if row['scores']['joint'] and not row['scores']['infrastructure_failure']: eligible[str(row['seed'])].append(row['id'])
            Path(f'results/{a.model}_clean_eligible.json').write_text(json.dumps(eligible,indent=2))
