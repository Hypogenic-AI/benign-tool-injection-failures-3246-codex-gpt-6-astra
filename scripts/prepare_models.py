from pathlib import Path
import json,requests,concurrent.futures,hashlib
assert (Path.cwd()/'.git').exists()
models={'qwen3':'Qwen/Qwen3-8B','deepseek':'deepseek-ai/DeepSeek-R1-Distill-Qwen-7B','moonlight':'moonshotai/Moonlight-16B-A3B-Instruct'}
def f(kv):
 key,repo=kv;meta=json.loads(Path(f'artifacts/{key}.json').read_text())['body'];rev=meta['sha']
 folder=Path('datasets/tokenizers')/key;folder.mkdir(parents=True,exist_ok=True)
 out={'key':key,'repo':repo,'revision':rev,'files':[]}
 for name in (['tiktoken.model','tokenization_moonshot.py'] if key=='moonlight' else ['tokenizer.json']) + ['tokenizer_config.json','config.json','README.md']:
  u=f'https://huggingface.co/{repo}/resolve/{rev}/{name}';r=requests.get(u,timeout=90);r.raise_for_status();p=folder/name;p.write_bytes(r.content)
  out['files'].append({'file':str(p),'url':u,'bytes':len(r.content),'sha256':hashlib.sha256(r.content).hexdigest()})
 print(key,'downloaded tokenizer and card');return out
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:out=list(ex.map(f,models.items()))
Path('artifacts/model_manifest.json').write_text(json.dumps(out,indent=2))
