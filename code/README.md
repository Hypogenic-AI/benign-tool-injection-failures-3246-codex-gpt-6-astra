# Code resources

Two official repositories were cloned and inspected. No repositories or staged paths were explicitly specified by the research author. All experiment code remains to be implemented by the runner; the scripts in `scripts/` prepare and validate resources only.

## AgentDojo

- URL: https://github.com/ethz-spylab/agentdojo
- Local: `code/agentdojo/`
- Commit: `089ed468cf3ed0322acc66b0211f26d9d90dbf60`
- License: MIT; upstream inherited components may have their own terms.
- Version declared in inspected pyproject: 0.1.35; Python >=3.10.
- Purpose: mutable application environments, typed tools, registered user and injection tasks, separate utility/security predicates, attack and defense pipelines.
- Entry points: `src/agentdojo/scripts/benchmark.py`, `src/agentdojo/base_tasks.py`, `src/agentdojo/functions_runtime.py`, `src/agentdojo/task_suite/`, `src/agentdojo/default_suites/`, `src/agentdojo/attacks/`.
- Minimal adaptation example: `examples/counter_benchmark/` shows a small fictional stateful environment, separate attacker and user tasks, and state/trace scoring. This is a better starting point for our custom task than a full banking environment.
- Dependencies include Pydantic, PyYAML, docstring-parser, tenacity, Click, DeepDiff, Rich, LangChain, and several provider SDKs. Transformers/Torch are optional upstream extras. Full dependency set has **not** been installed or smoke-tested here.
- Inspection caveat: `examples/counter_benchmark/suites/counter/user_tasks.py` contains nested function-name/argument checks that should not be copied blindly: arguments are checked under `function != "increment_by"`. Write explicit tests for correct tool/wrong arguments, wrong tool, no-op, unauthorized mutation then reversal, and valid authorized edits in the new scorer.
- Clone initially timed out while checking out the large upstream run archive. The clone was repaired into a clean sparse checkout (src, tests, examples, docs plus root files), and clean status/commit verified. Its `.git` is about 30 MB. Upstream run outputs are omitted.

Reproduce from the workspace root:

```bash
pwd
test -d .git
git clone --filter=blob:none --no-checkout https://github.com/ethz-spylab/agentdojo.git code/agentdojo
git -C code/agentdojo sparse-checkout init --cone
git -C code/agentdojo sparse-checkout set src tests examples docs
git -C code/agentdojo checkout 089ed468cf3ed0322acc66b0211f26d9d90dbf60
```

If adapting the package itself, the runner can add it to the isolated project with `uv add --project . --editable ./code/agentdojo` after resolving required inference dependencies. This is an installation option, not a claim that the complete benchmark ran.

## InjecAgent

- URL: https://github.com/uiuc-kang-lab/InjecAgent
- Local: `code/InjecAgent/`
- Commit: `f19c9f2c79a41046eb13c03c51a24c567a8ffa07`
- License: MIT (`LICENCE`).
- Purpose: controlled tool-return templates, base/enhanced attack conditions, prompted ReAct and function-calling evaluation, valid/all denominators.
- Entry points: `src/evaluate_prompted_agent.py`, `src/evaluate_finetuned_agent.py`, `src/models.py`, `src/output_parsing.py`, `src/utils.py`.
- `requirements.txt` lists openai, anthropic, transformers, torch. Inspection found an NLTK import in `output_parsing.py` not included in that requirements file. Provider classes and model formats predate our chosen checkpoints; a local adapter is needed.
- The paper and code distinguish valid/all ASR, but the primary experiment must execute and inspect exact fictional record mutations, not just detect the target tool name in generated text. The published initial assistant Thought is simulated; do not use it as evidence of actual clean completion.
- Data have been independently downloaded to `datasets/InjecAgent/` with commit-level provenance. Keep original harmful payloads as reference data; use benign fictional targets in experiments.
- Validation: clean clone, README/requirements/entry points inspected, all JSON/JSONL resources parsed. Full model evaluation was not attempted in this resource phase.

```bash
pwd
test -d .git
git clone https://github.com/uiuc-kang-lab/InjecAgent.git code/InjecAgent
git -C code/InjecAgent checkout f19c9f2c79a41046eb13c03c51a24c567a8ffa07
```

## Local preparation scripts and runtime handoff

- `scripts/download_papers.py`: fetch resolved open PDFs; original URLs/statuses in `artifacts/paper_downloads.json` (later alternate-source recoveries are recorded there).
- `scripts/prepare_datasets.py`: download author data from pinned clones.
- `scripts/prepare_models.py`: download pinned tokenizer/config/card assets, not weights.
- `scripts/build_pilot.py`: construct 24 development-only worlds with exact I/Q token-length matching for three checkpoint tokenizers.
- `scripts/validate_resources.py`: verify PDF parsing, file hashes, data schema/counts, tokenizer matches, git exclusions, and clean clone status.

`pyproject.toml` and `uv.lock` describe a fresh `.venv` in this workspace. The user explicitly prohibited using the shared safety environment, so all preparation ran here. The safety-evals skill's result format can still be reused by the runner without its shared interpreter. See `planning.md` for the custom Inspect-task and result-conversion handoff.

Model cards are snapshots, not guaranteed current compatibility recipes. Qwen3's card requires Transformers >=4.51.0; Moonlight's card recommends a historical 4.48.2 setup and custom tokenizer/model code. Do not pin a single environment to mutually incompatible historical recommendations. Validate a contemporary vLLM/Transformers stack or use separate project-local serving environments if needed. DeepSeek's card recommends no system prompt and reasoning-aware generation; any common tool adapter is therefore a measured configuration choice. Token matching here does not establish successful tool use or inference compatibility.
