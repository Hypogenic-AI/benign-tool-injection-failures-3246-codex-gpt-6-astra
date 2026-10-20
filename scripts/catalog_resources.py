from pathlib import Path
import json,re,hashlib
assert (Path.cwd()/'.git').exists()
rows=json.loads(Path('artifacts/paper_downloads.json').read_text())
notes={
0:'Controlled tool-result templates; valid/all denominators and clear benign responses. Core schema reference; complete PDF reviewed.',
1:'Adaptive evaluation challenges static-defense claims. Contextual limitation, not an additional implementation direction.',
2:'Dynamic mutable environments with independent utility and security checks. Core environment reference; complete PDF reviewed.',
3:'Checks whether actions serve the user task; relevant authorization perspective, but a new defense is outside scope.',
4:'Masked-user replay compares actions; useful counterfactual context, not our primary intervention.',
5:'Symbolic tool privileges and constrained policy updates; runtime restrictions differ from model susceptibility.',
6:'Model-based input sanitization with detector error rates; not selected for implementation.',
7:'Open-ended tasks include useful external guidance, exposing utility loss from indiscriminate blocking.',
8:'Conference version of AgentVigil; incomplete service abstract replaced by PDF first-page screening. Do not count as independent evidence from preprint.',
9:'Black-box search with MCTS across agent benchmarks; adaptive optimization is outside the fixed-payload hypothesis.',
10:'Preplanned tool dependencies restrict execution; structural defense changes available action space.',
11:'Separates abstract planning, concrete app mapping and execution with information-flow checks.',
12:'Task-conditioned sanitization removes injected content; requires trained defense rather than a matched utility experiment.',
13:'Fictional banking data-flow attacks connect task structure and exfiltration; use only as contextual evidence.',
14:'Counterfactual replay at tool boundaries localizes deviations and supports recovery.',
15:'Tool-interface firewalls and benchmark auditing emphasize metric validity and stronger attacks.',
16:'Graph representations of runtime traces support program-analysis security policies.',
17:'Ablation-based attribution selectively triggers sanitization; causal attribution is established related work.',
18:'RL search improves adaptive attack discovery; training and optimization are pruned from implementation.',
19:'Broad agent-security survey; background rather than primary evidence for a paired effect.',
20:'Parsing tool results into data aims to remove commands; may alter useful content and needs utility assessment.',
21:'Tool-sequence feedback drives greybox mutation; adaptive discovery is outside the selected intervention.',
22:'Defense taxonomy and circumvention analysis; background for limitations of general robustness claims.',
23:'Generates adaptive attacks across AgentDojo and AgentDyn; changes attacker budget and distribution.',
24:'Sampling and task-guided aggregation trade additional inference for defense; not selected.',
25:'Distinguishes covert and overt successful actions; final response alone can miss actual modifications.',
26:'Token-level removal of agent-directed instructions; quotation/framing controls are important for assessing collateral loss.',
27:'Dynamic attack/defense evaluation and hidden-state intervention; probes are outside the selected directions.',
28:'Self-reflection training includes Qwen3-8B, so this checkpoint alone is not a novel contribution.',
29:'Chat-template impersonation makes exact serialized roles and wrappers part of the threat model.',
30:'Dynamic policies, planning and context isolation; architectural defense outside the primary contrast.',
31:'Persistent workspace control creates multi-stage threats beyond the single-tool-return scope.',
32:'Layered governance and judge cascades; not a direct matched benign record-edit estimate.',
33:'Replication study emphasizes goal reachability, benign utility and run variation when ASR is low.',
34:'Reachability-based capability restriction; runtime tool restriction must not masquerade as model resistance.',
35:'Iterative rewriting of external instructions; non-imperative payloads limit guarantees.',
36:'Self-distillation targets robustness while preserving legitimate use of tool-provided guidance.',
37:'Multi-agent composition can change provenance guarantees; outside the single-agent scope.',
38:'Small-scale adaptive evaluation of external enforcement; useful warning about limited attack/model generality.',
39:'Localizes injected instructions and data spans; detection is not execution-grounded success.',
40:'Learned attack-strategy library enables low-query transfer; attack optimization is not selected.',
41:'Compares execution provenance with clean authorization graphs at argument level.',
42:'Balances excessive and insufficient tool privileges; motivates measuring authorized action capability.',
43:'Persistent labeled artifacts and planned information flow address cross-query attacks, outside scope.',
44:'Feedback-driven payload optimization and mechanistic analysis; fixed treatment and held-out confirmation are needed here.',
45:'Hidden states can encode exposure without preventing unsafe actions; exposure and behavioral success differ.',
46:'Causal context attribution plus explicit monitor rules; alternative monitor rather than required resource.',
47:'Runtime architecture models evolving trajectory risks; broader than the selected benign intervention.',
48:'Compares black-box and gradient attack search with budget-dependent transfer; not a fixed-effect replication.',
49:'Provenance paths can remain short despite long trajectories; structural proximity is not proof of causal effect.',
50:'Narrative enterprise-security synthesis, not an original experimental dataset or risk estimate.',
51:'Selective structural verification escalates uncertain actions; useful distinction between checks and model behavior.',
52:'Unified evaluation platform warns about weak cross-benchmark generalization and aligned injected tasks.',
53:'Broad agent-security benchmark spans many surfaces; narrower AgentDojo/InjecAgent resources better fit this hypothesis.',
54:'Boundary awareness and reminders motivate the single secondary prompt-defense ablation.',
55:'Public adversarial competition supplies broad failures but not controlled benign paired denominators.',
56:'Approved-change controls reveal overblocking from static allowlists; strong conceptual utility match.',
57:'Audits payload delivery, exact arguments, capability confounds and trace retention; important instrumentation warning.',
58:'Context-dependent tasks expose defenses that discard needed runtime evidence.',
59:'Lifecycle survey covers persistent state and authority; contextual rather than direct experimental support.',
60:'Synthetic step-labeled trajectories include resisted attacks and hard negatives; labels do not substitute for live model outcomes.',
61:'Multimodal carriers separate attempted and completed attacks; outside text-only checkpoint scope.',
62:'Multi-agent aggregation changes system-level exposure; not a single-checkpoint paired contrast.',
63:'Provenance tracing in educational workflows; forensic attribution rather than fictional record editing.',
64:'Separates action induction, source provenance and execution authority; close conceptual related work.',
65:'End-to-end web evaluation exposes capability-limited attack completion; browser infrastructure is pruned.',
66:'Guardrail stack combines classifiers, reasoning audit and code checks; not needed for the primary state outcome.',
67:'Counterfactual tool-action replay tests support from user intent; related causal-attribution work.',
68:'Large-scale competition emphasizes hidden side effects and transfer; not a matched-control experiment.',
69:'Context-aware attacks require benign causal support for actions; motivates preserving factual evidence in controls.',
70:'Stakeholder-specific web-agent harms require outcome and process measures; different deployment scope.',
71:'Live controlled service benchmark; infrastructure exceeds the local fictional-record requirement.',
72:'Multi-step page chains trade attack depth and capability; computer-use setting is excluded.',
73:'Layered spotlighting/detection/authentication study reports security and utility together; not the primary intervention.',
74:'Attack-chain detection with benign hard negatives; useful warning about false positives and random splits.',
75:'Depth and framing can confound ASR through non-encounter; log exposure and fixed insertion position.',
76:'Co-evolving adversarial training changes the model; training direction pruned.',
77:'Matched ambiguity/clarification states illustrate channel confounding; our user task remains fully specified.',
78:'Compiles policies to tool-call gates; illustrates authorized-action blockage and argument-level constraints.',
79:'Proxy injects into live web responses; a browser deployment toolkit, not needed for local fixtures.',
80:'Trace contracts support replay and stateful assurance; broad design context.',
81:'Multimodal agent decomposition separates component attacks; outside text-only experiment.',
82:'Forensic log analysis using LLMs; full PDF unavailable, screened from service abstract only.',
83:'Poisons tool metadata at registration; different attack surface from a returned tool result.',
84:'Treats attack generation as budgeted search; motivates prespecifying attack budget and payloads.',
85:'Composable research toolkit spans many carriers/defenses; existing two repositories suffice for this narrow task.',
86:'Execution-aware email evaluation distinguishes tool calls from delivered outcomes; live email execution not selected.',
87:'Stage markers distinguish exposure, propagation and execution; evidence from different surfaces is not interchangeable.',
88:'Layered agent-security review; background outside the bounded causal question.',
89:'Unvalidated lifecycle framework synthesizes governance; not independent experimental evidence.',
90:'Direct harmful-user task benchmark; authorization and harmless indirect injection are different questions.',
91:'LLM-emulated tools improve scale but simulator/judge contamination motivates deterministic local execution.',
92:'Adaptive web-agent attack discovery; browser deployment and search are outside selected directions.',
93:'DOM-context attacks against web agents; full PDF inaccessible, not selected for implementation.',
94:'Persistent memory trajectories study delayed activation, beyond the single-return contrast.',
95:'Assumption-driven Monte Carlo simulation, not deployed-model incident rates; full abstract recovered from PDF.',
96:'Capability-controlled agent runtime separates visibility and authority; infrastructure direction not selected.',
97:'Trajectory detector trained on AgentDrift; synthetic regularities and template leakage limit transfer claims.',
98:'Formal information-flow calculus and verified harness; proof engineering is outside this empirical contrast.',
99:'Matched benign shams and clustered uncertainty already appear in related work; warns against pseudoreplication.',
100:'Conceptual enterprise zero-trust architecture; coverage scores are not measured attack prevention.',
101:'Multi-agent message-flow policy enforcement; outside single-agent experimental scope.'}
core={0,2};support={1,7,28,33,36,54,56,57,64,67,75,99}
lines=['# Downloaded papers and screening index','',
'102 paper-finder records screened; 97 candidate PDFs downloaded plus two supplemental papers = 99 full PDF files. AgentVigil conference/preprint records represent related versions, not independent studies. Five candidate PDFs remain unavailable. Service relevance is retained separately from local reading priority. Main synthesis: `../literature_review.md`; sequential full-reading notes: `../artifacts/literature_chunk_notes.md`.','',
'Review depth: only AgentDojo and InjecAgent received full all-chunk review. All other entries are abstract/selected-section screening; absent sample-size, baseline, or metric details must be recovered from the PDF before quantitative reuse. Screening notes are interpretive summaries, not replicated results.','']
screen=[]
for r in rows:
 i=r['index'];p=r['search'];group='Core full review' if i in core else 'Design support' if i in support else 'Context only; outside implementation scope'
 screen.append({'index':i,'title':p['title'],'service_relevance':p['relevance'],'decision':group,'abstract_screened':True,'abstract_source':'PDF first page' if i in {8,95} else 'paper-finder','note':notes[i]})
 target=Path(r['file']).name if r.get('file') else None
 lines += [f"## {i+1}. {p['title']}",f"- Authors: {p['authors']}",f"- Year: {p['year']}; source: {p['url']}",f"- Local PDF: [{target}]({target})" if target else f"- PDF unavailable: {r['status']}; retry: {r.get('retry_note',r.get('error','no open PDF found'))}",f"- Service relevance: {p['relevance']}/3; local decision: {group}.",f"- Method / relevance / limitation: {notes[i]}"]
 ids=(r.get('resolution') or {}).get('externalIds',{})
 if ids:lines += ['- Identifiers: '+json.dumps(ids,ensure_ascii=False)]
 links=re.findall(r'https://github.com/[^\s<>]+',p.get('abstract',''))
 if links:lines += ['- Code referenced by abstract (not necessarily cloned): '+', '.join(links)]
 lines.append('')
lines += ['## Supplemental citation-chased papers','']
for r in json.loads(Path('artifacts/paper_metadata.json').read_text()):
 if r['id'] not in ['2302.12173','2503.18813']:continue
 meta=r['metadata'];title=next(v for k,v in meta if k=='title');authors='; '.join(v for k,v in meta if k=='author');f=r['id']+'_'+r['name']+'.pdf'
 lines += [f'### {title}',f'- Authors: {authors}',f'- Source: https://arxiv.org/abs/{r["id"]}',f'- File: [{f}]({f})','- Reading: abstract/opening-section screening; see main review for contribution and limitations.','']
Path('papers/README.md').write_text('\n'.join(lines))
Path('artifacts/screening.json').write_text(json.dumps(screen,indent=2))
print('Cataloged',len(rows),'screened records and 2 supplements')
