"""Convert actual Inspect logs with the skill converter, then attach clustered summaries."""
import datetime,json,os,subprocess,sys
from pathlib import Path
from analyze import MODELS

def export():
    data=json.loads(Path('results/analysis.json').read_text());items=json.loads(Path('results/item_scores.json').read_text())
    sources=json.loads(Path('artifacts/subject_sources.json').read_text());versions=json.loads(Path('manifests/environment.json').read_text())
    env=os.environ.copy()
    if not env.get('NEURICO_SRC'):
        candidates=[parent/'neurico'/'src' for parent in Path.cwd().parents]
        found=next((p for p in candidates if (p/'safety/suites.py').exists()),None)
        if found is not None: env['NEURICO_SRC']=str(found)
        else: raise RuntimeError('Set NEURICO_SRC to the NeuriCo src directory for the safety-evals log converter.')
    converter=Path('.codex/skills/safety-evals/scripts/run_eval.py'); out=Path('results/safety');out.mkdir(exist_ok=True)
    for model,source in zip(MODELS,sources):
        logmanifest=Path(f'results/{model}_logs.json');logs=json.loads(logmanifest.read_text()) if logmanifest.exists() else []
        path=out/f'custom:benign-tool-injection-v1__{model}.json'
        if logs:
            cmd=[sys.executable,str(converter),'--from-log',logs[-1]['location'],'--eval-id','custom:benign-tool-injection-v1','--model-id',model]
            result=subprocess.run(cmd,env=env,capture_output=True,text=True)
            Path(f'logs/convert_{model}.log').write_text(result.stdout+result.stderr)
            if result.returncode:raise RuntimeError('skill log conversion failed: '+model)
            record=json.loads(path.read_text())
            Path(f'results/{model}_skill_conversion.json').write_text(json.dumps(record,indent=2))
        else: record={'schema':'neurico-safety-result/v1','eval_id':'custom:benign-tool-injection-v1','model_id':model,'inspect_log':None}
        m=data['models'][model];metrics={}
        for cond,ms in m['conditions'].items():
            for key,value in ms.items():
                metrics[f'{cond}/{key}']=value['mean'];metrics[f'{cond}/{key}/stderr']=value['se'];metrics[f'{cond}/{key}/ci95']=value['ci95'];metrics[f'{cond}/{key}/n']=value['n']
        for name in ['unconditional_difference','conditional_difference']:
            st=m[name];metrics[name]=st['mean'];metrics[name+'/stderr']=st['se'];metrics[name+'/ci95']=st['ci95'];metrics[name+'/n']=st['n']
        record.update(job=Path.cwd().name,category='prompt-injection',model_access='vllm:'+source['repo'],runner='inspect:src/evals/benign_tool_injection.py',
          task_args={'custom_name':'benign-tool-injection-v1','conditions':['clean','quoted','injected'],'seeds':[11,22,33],'max_turns':6},
          model_args={'temperature':.6,'top_p':1.,'top_k':-1,'max_tokens':1024,'context':8192,'revision':source['revision'],'thinking':'disabled' if model=='qwen3-8b' else 'native'},
          judge=None,limit=100,n=100 if m['complete'] else 0,n_episodes=m['recorded_episodes'],metrics=metrics,
          per_item=[{'id':x['id'],'epoch':1,'aggregation':'mean_over_clean_eligible_seeds','value':x['conditional_difference'],'answer':x['conditions']} for x in items if x['model']==model],
          command=f'.venv/bin/python src/execute.py --models {model}',inspect_logs=[x['location'] for x in logs],versions=versions,
          status='success' if m['complete'] else 'failed',error=None if m['complete'] else 'Incomplete or infrastructure-failed episodes; see analysis.json',
          analysis=m,finished=datetime.datetime.now(datetime.timezone.utc).isoformat(),dataset_revision=json.loads(Path('manifests/freeze.json').read_text())['sha256']['manifests/items.json'])
        if not m['complete'] and Path('results/execution_status.json').exists():
            attempt=next((x for x in json.loads(Path('results/execution_status.json').read_text()) if x['model_id']==model),{})
            record['error']=attempt.get('error',record['error'])
            record['server_attempt']=attempt
        # Aggregate token usage across all actual condition logs.
        usage={}; duration=0.; started=[];finished=[]
        for log in logs:
            raw=json.loads(Path(log['location']).read_text());stats=raw.get('stats',{});duration+=stats.get('completed',0) if isinstance(stats.get('completed'),(int,float)) else 0
            for rmodel,u in stats.get('model_usage',{}).items():
                if rmodel not in usage:usage[rmodel]={}
                for k,v in u.items():
                    if isinstance(v,(int,float)):usage[rmodel][k]=usage[rmodel].get(k,0)+v
            if stats.get('started_at'):started.append(stats['started_at'])
            if stats.get('completed_at'):finished.append(stats['completed_at'])
        record['model_usage']=usage
        if started:record['started']=min(started)
        if finished:record['finished']=max(finished)
        if started and finished:
            record['duration_s']=(datetime.datetime.fromisoformat(max(finished).replace('Z','+00:00'))-datetime.datetime.fromisoformat(min(started).replace('Z','+00:00'))).total_seconds()
        path.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print('Exported',len(MODELS),'schema records')
if __name__=='__main__':export()
