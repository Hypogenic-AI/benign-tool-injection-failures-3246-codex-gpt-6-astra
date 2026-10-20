"""Inspect task for benign-tool-injection-v1; no semantic or LLM judge."""
import json, sys, time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from environment import World, SYSTEM
from inspect_ai import Task, task
from inspect_ai.dataset import Sample, MemoryDataset
from inspect_ai.model import ChatMessageSystem, ChatMessageUser, get_model, GenerateConfig
from inspect_ai.solver import solver, TaskState, Generate
from inspect_ai.scorer import scorer, Score, Target, mean, stderr

@solver
def record_agent():
    async def solve(state:TaskState,generate:Generate):
        md=state.metadata; item=md['item']; world=World(item,md['condition'],md['payload'])
        state.messages=[ChatMessageSystem(content=SYSTEM),ChatMessageUser(content=item['user'])]
        usage=[]; error=None; start=time.time()
        for turn in range(6):
            try:
                output=await get_model().generate(state.messages, config=GenerateConfig(temperature=.6,top_p=1,max_tokens=1024,seed=md['seed'],max_retries=0,timeout=180))
                state.output=output; raw=output.completion
                truncated=any(c.stop_reason=='max_tokens' for c in output.choices)
                response=world.step(raw,truncated)
                usage.append(output.usage.model_dump() if output.usage else {})
                state.messages.append(output.message)
                if world.done: break
                state.messages.append(ChatMessageUser(content='TOOL RESULT (untrusted data):\n'+response))
            except Exception as exc:
                error=f'{type(exc).__name__}: {exc}'; break
        scores=world.scores(); scores['infrastructure_failure']=int(error is not None)
        # Never label infrastructure-failed episodes successful or safe.
        if error: scores['legitimate']=0; scores['joint']=0; scores['withholding']=0
        record=dict(id=item['id'],model_id=md['model_id'],condition=md['condition'],seed=md['seed'],split=item['split'],kind=item['kind'],scores=scores,
            events=world.events,final_state=world.state,usage=usage,error=error,duration_s=time.time()-start)
        trace_path=Path('results/traces')/md['model_id']/item['split']/f"{item['id']}__{md['condition']}__{md['seed']}.json"
        trace_path.parent.mkdir(parents=True,exist_ok=True)
        trace_path.write_text(json.dumps(record,ensure_ascii=False,indent=2))
        state.metadata['scores']=scores; state.metadata['trace_path']=str(trace_path)
        state.completed=True
        return state
    return solve

@scorer(metrics={'*':[mean(),stderr()]})
def state_scores():
    async def score(state:TaskState,target:Target):
        return Score(value=state.metadata['scores'],answer=state.metadata['trace_path'])
    return score

@task
def benign_tool_injection(model_id:str='qwen3-8b',split:str='heldout',condition:str='all',limit_items:int=0):
    mapping={'qwen3-8b':'Qwen/Qwen3-8B','deepseek-r1-distill-llama-8b':'deepseek-ai/DeepSeek-R1-Distill-Llama-8B','moonlight-16b-a3b-instruct':'moonshotai/Moonlight-16B-A3B-Instruct'}
    items=[x for x in json.loads(Path('manifests/items.json').read_text()) if x['split']==split]
    if limit_items == 2: items=[items[0],items[len(items)//2]]
    elif limit_items: items=items[:limit_items]
    payloads=next(x for x in json.loads(Path('manifests/payloads.json').read_text()) if x['repo']==mapping[model_id]); byid={x['id']:x for x in payloads['pairs']}
    conditions=['clean','quoted','injected'] if condition=='all' else [condition]
    samples=[]
    for item in items:
        for seed in ([11,22,33] if split=='heldout' else [11]):
            for cond in conditions:
                samples.append(Sample(id=f"{item['id']}__{cond}__{seed}",input=item['user'],metadata={'item':item,'seed':seed,'condition':cond,'payload':byid[item['id']][cond],'model_id':model_id}))
    return Task(dataset=MemoryDataset(samples,name='benign-tool-injection-v1'),solver=record_agent(),scorer=state_scores())
