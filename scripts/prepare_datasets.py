"""Re-download pinned author data, validate it, and retain provenance. Run at repo root."""
from pathlib import Path
import requests,json,subprocess,hashlib,concurrent.futures
ROOT=Path(__file__).resolve().parents[1]
assert Path.cwd()==ROOT and (ROOT/'.git').exists()
sources=[]
for repo,folder,sub in [('uiuc-kang-lab/InjecAgent','InjecAgent','data'),('ethz-spylab/agentdojo','agentdojo','src/agentdojo/data')]:
 commit=subprocess.check_output(['git','-C','code/'+folder,'rev-parse','HEAD'],text=True).strip()
 for p in (Path('code')/folder/sub).rglob('*'):
  if not p.is_file() or p.suffix not in ['.json','.jsonl','.yaml']:continue
  rel=p.relative_to(Path('code')/folder)
  target=Path('datasets')/folder/p.relative_to(Path('code')/folder/sub)
  sources.append({'repo':repo,'commit':commit,'url':f'https://raw.githubusercontent.com/{repo}/{commit}/{rel}','file':str(target)})
def get(s):
 r=requests.get(s['url'],timeout=60);r.raise_for_status();p=Path(s['file']);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(r.content)
 s.update(bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest())
 return s
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:out=list(ex.map(get,sources))
Path('artifacts/dataset_manifest.json').write_text(json.dumps(out,indent=2))
print('Downloaded',len(out),'files',sum(x['bytes'] for x in out),'bytes')
