from pathlib import Path
import json,re,requests,concurrent.futures,hashlib
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
assert Path.cwd()==ROOT and (ROOT/'.git').exists()
rows=json.loads(Path('artifacts/paper_resolution.json').read_text())
previous={r['index']:r for r in json.loads(Path('artifacts/paper_downloads.json').read_text())} if Path('artifacts/paper_downloads.json').exists() else {}
search=[json.loads(x) for x in max(Path('paper_search_results').glob('*.jsonl'),key=lambda p:p.stat().st_size).read_text().splitlines()]
def run(pair):
 i,r=pair; record={'index':i,'search':search[i],'resolution':r}
 if not r: return dict(record,status='unresolved')
 aid=r.get('externalIds',{}).get('ArXiv'); url=f'https://arxiv.org/pdf/{aid}' if aid else (r.get('openAccessPdf') or {}).get('url')
 prior=previous.get(i,{})
 if prior.get('status')=='downloaded':url=prior.get('url',url)
 if not url:return dict(record,status='no_open_pdf')
 existing=list(Path('papers').glob(f'{aid}_*.pdf')) if aid else []
 slug=re.sub('[^a-z0-9]+','_',r['title'].lower()).strip('_')[:90]
 p=Path(prior['file']) if prior.get('status')=='downloaded' else (existing[0] if existing else Path('papers')/f'{aid or "paper"}_{slug}.pdf')
 try:
  if not p.exists():
   resp=requests.get(url,timeout=60);resp.raise_for_status();assert resp.content.startswith(b'%PDF'), 'not PDF';p.write_bytes(resp.content)
  n=len(PdfReader(p).pages)
  return dict(record,status='downloaded',file=str(p),pages=n,url=url,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
 except Exception as e:return dict(record,status='failed',url=url,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
 out=list(ex.map(run,enumerate(rows)))
Path('artifacts/paper_downloads.json').write_text(json.dumps(out,indent=2))
from collections import Counter
print(Counter(r['status'] for r in out))
for r in out:
 if r['status']!='downloaded':print(r['index'],r['status'],r.get('error',''))
