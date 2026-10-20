"""Reproduction entry point: start/stop exactly one local vLLM server at a time."""
import argparse,json,os,signal,subprocess,sys,time
from pathlib import Path
import requests
MODELS={'qwen3-8b':('Qwen3-8B',.6),'deepseek-r1-distill-llama-8b':('DeepSeek-R1-Distill-Llama-8B',.6),'moonlight-16b-a3b-instruct':('Moonlight-16B-A3B-Instruct',.7)}

def run(models,port=8765):
    root=Path.cwd(); assert (root/'manifests/freeze.json').exists()
    subprocess.run([sys.executable,'src/validate.py'],check=True)
    env=os.environ.copy();env.update(HF_HOME=str(root/'models/hf_home'),XDG_CACHE_HOME=str(root/'.cache'),VLLM_CACHE_ROOT=str(root/'.cache/vllm'))
    # Respect the allocated device, and never select a second GPU.
    allocated=env.get('CUDA_VISIBLE_DEVICES','0').split(',')[0];env['CUDA_VISIBLE_DEVICES']=allocated
    summaries=[]
    for model in models:
        name,memory=MODELS[model]
        command=[sys.executable,'-m','vllm.entrypoints.openai.api_server','--model',str(root/'models'/name),'--served-model-name',model,'--host','127.0.0.1','--port',str(port),'--tensor-parallel-size','1','--dtype','bfloat16','--max-model-len','8192','--gpu-memory-utilization',str(memory),'--max-num-seqs','64','--generation-config','vllm','--enforce-eager']
        if model.startswith('moonlight'):command+=['--trust-remote-code']
        start=time.time();status={'model_id':model,'server_command':command,'allocated_gpu':allocated,'started_unix':start}
        with open(f'logs/server_{model}.log','w') as serverlog:
            server=subprocess.Popen(command,env=env,stdout=serverlog,stderr=subprocess.STDOUT,start_new_session=True)
            status['pid']=server.pid
            try:
                for _ in range(600):
                    if server.poll() is not None:raise RuntimeError(f'server exited {server.returncode}')
                    try:
                        if requests.get(f'http://127.0.0.1:{port}/health',timeout=2).status_code==200:break
                    except requests.RequestException:pass
                    time.sleep(1)
                else:raise RuntimeError('server readiness timeout')
                status['ready_seconds']=time.time()-start
                for dev in [True,False]:
                    cmd=[sys.executable,'src/run_checkpoint.py',model,'--port',str(port)]+(['--dev'] if dev else [])
                    with open(f'logs/{model}_{"dev" if dev else "main"}.log','w') as log:
                        result=subprocess.run(cmd,env=env,stdout=log,stderr=subprocess.STDOUT)
                    if result.returncode: raise RuntimeError(f'checkpoint runner exited {result.returncode}, dev={dev}')
                    # Fail fast on actual transport/parser-code exceptions; model malformed actions are allowed.
                    paths=list((root/'results/traces'/model/('dev' if dev else 'heldout')).glob('*.json'))
                    if any(json.loads(p.read_text()).get('error') for p in paths):raise RuntimeError('episode infrastructure errors; inspect trace files')
                status['status']='success'
            except Exception as exc:
                status.update(status='failed',error=str(exc))
            finally:
                # Kill only the process group launched here, not any shared-machine process.
                if server.poll() is None:
                    os.killpg(server.pid,signal.SIGTERM)
                    try:server.wait(timeout=30)
                    except subprocess.TimeoutExpired:os.killpg(server.pid,signal.SIGKILL);server.wait()
                status['duration_s']=time.time()-start;status['server_exit_code']=server.returncode
                summaries.append(status);Path('results/execution_status.json').write_text(json.dumps(summaries,indent=2))
        print(json.dumps(status),flush=True)
    return summaries
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--models',nargs='+',default=list(MODELS));p.add_argument('--port',type=int,default=8765);a=p.parse_args();run(a.models,a.port)
