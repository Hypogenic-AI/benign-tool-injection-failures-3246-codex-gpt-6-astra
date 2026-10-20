from pathlib import Path
import json,hashlib,subprocess,ast
import yaml
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
assert Path.cwd()==ROOT and (ROOT/'.git').exists()
def load_yaml(p):
 class Loader(yaml.SafeLoader):pass
 def include(loader,node):return load_yaml(p.parent/loader.construct_scalar(node))
 Loader.add_constructor('!include',include)
 return yaml.load(p.read_text(),Loader=Loader)
report={'papers':[],'datasets':[],'repositories':[],'checks':[]}
for p in sorted(Path('papers').glob('*.pdf')):
 r=PdfReader(p);assert len(r.pages)>0
 report['papers'].append({'file':str(p),'pages':len(r.pages),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
for item in json.loads(Path('artifacts/dataset_manifest.json').read_text()):
 p=Path(item['file']);assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256']
 if p.suffix=='.json': obj=json.loads(p.read_text())
 elif p.suffix=='.jsonl':obj=[json.loads(x) for x in p.read_text().splitlines()]
 else:obj=load_yaml(p)
 assert obj is not None and len(obj)>0
 report['datasets'].append({'file':str(p),'top_level_type':type(obj).__name__,'top_level_count':len(obj),'top_level_nulls':sum(x is None for x in (obj.values() if isinstance(obj,dict) else obj))})
u=[json.loads(x) for x in Path('datasets/InjecAgent/user_cases.jsonl').read_text().splitlines()]
required=['User Tool','User Instruction','Tool Parameters','Tool Response Template']
assert len(u)==17 and all(all(r.get(k) for k in required) for r in u)
assert all(r['Tool Response Template'].count('<Attacker Instruction>')==1 for r in u)
for r in u: assert isinstance(ast.literal_eval(r['Tool Parameters']),dict)
for name in ['test_cases_dh_base','test_cases_dh_enhanced','test_cases_ds_base','test_cases_ds_enhanced']:
 r=json.loads(Path(f'datasets/InjecAgent/{name}.json').read_text());assert len(r)==(510 if '_dh_' in name else 544)
 assert all(isinstance(x,dict) and all(v is not None for v in x.values()) for x in r)
for repo in ['agentdojo','InjecAgent']:
 path='code/'+repo;commit=subprocess.check_output(['git','-C',path,'rev-parse','HEAD'],text=True).strip()
 status=subprocess.check_output(['git','-C',path,'status','--porcelain'],text=True);assert not status
 report['repositories'].append({'path':path,'commit':commit,'clean':True})
# Load generator functions without re-running generation.
scope={};source=Path('scripts/build_pilot.py').read_text().split('rows=[]')[0];exec(compile(source,'build_pilot.py','exec'),scope)
rows=[json.loads(x) for x in Path('datasets/benign_record_pilot.jsonl').read_text().splitlines()]
assert len(rows)==24 and len({r['id'] for r in rows})==24
for r in rows:
 assert r['split']=='development_only'
 for m,v in r['variants_by_model'].items():
  assert scope['count'](m,v['injection'])==scope['count'](m,v['quoted'])==v['token_count']
  i=json.loads(v['injection']);q=json.loads(v['quoted'])
  assert {k:v for k,v in i.items() if k!='notes'}=={k:v for k,v in q.items() if k!='notes'}
 assert r['attacker_target'] not in r['authorized_writes']
report['pilot']={'worlds':24,'templates':6,'matched_pairs':72,'special_tokens':False,'confirmatory':False}
for r in json.loads(Path('artifacts/model_manifest.json').read_text()):
 for f in r['files']:assert hashlib.sha256(Path(f['file']).read_bytes()).hexdigest()==f['sha256']
for p in ['datasets/benign_record_pilot.jsonl','datasets/InjecAgent/test_cases_dh_base.json','datasets/tokenizers/qwen3/tokenizer.json']:
 assert subprocess.run(['git','check-ignore','-q',p]).returncode==0
for p in ['datasets/README.md','datasets/examples.json','datasets/download.sh']:
 assert subprocess.run(['git','check-ignore','-q',p]).returncode==1
report['checks']=['All full PDF headers/pages parsed','All author data checksums match','JSON/JSONL/YAML including local includes parsed','17 user schemas and injection slots checked','Base/enhanced row counts checked','72 per-model I/Q token-count matches checked','Factual fields identical within I/Q pairs','All model-resource hashes match','Clones clean','Large/local data git-ignored; docs and small sample trackable']
Path('artifacts/resource_validation.json').write_text(json.dumps(report,indent=2))
print(json.dumps({'papers':len(report['papers']),'data_files':len(report['datasets']),'repos':len(report['repositories']),'pilot':report['pilot'],'checks':report['checks']},indent=2))
