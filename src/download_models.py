"""Download exact subject revisions into workspace-local directories."""
import json, os, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
os.environ['HF_HOME']=str(Path('models/hf_home').resolve())
os.environ['HF_HUB_DISABLE_XET']='1'
from huggingface_hub import snapshot_download

def fetch(entry):
    name=entry['repo'].split('/')[-1]
    start=time.time()
    try:
        path=snapshot_download(entry['repo'], revision=entry['revision'], local_dir='models/'+name,
             allow_patterns=['*.json','*.safetensors','*.py','*.model','*.txt','*.md'],max_workers=8)
        return dict(repo=entry['repo'],path=path,status='success',seconds=time.time()-start)
    except Exception as e:
        return dict(repo=entry['repo'],status='failed',error=str(e),seconds=time.time()-start)
if __name__=='__main__':
    sources=json.loads(Path('artifacts/subject_sources.json').read_text())
    with ThreadPoolExecutor(max_workers=3) as pool:
        out=list(pool.map(fetch,sources))
    Path('artifacts/download_results.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
