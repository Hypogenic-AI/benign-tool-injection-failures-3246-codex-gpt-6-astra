# Dataset resources

All resources are local. Downloaded data and tokenizer assets are excluded by `.gitignore`; `examples.json` is a 5.4 KB development sample. The two downloaded research datasets are InjecAgent and AgentDojo. The generated pilot and three tokenizer bundles are listed separately, not counted as downloaded benchmarks.

## Reproduce downloads

From the workspace root (verify with `pwd` and `test -d .git`):

```bash
uv sync --project .
# Restore the pinned clones first if absent: see code/README.md.
.venv/bin/python scripts/prepare_datasets.py
.venv/bin/python scripts/prepare_models.py
.venv/bin/python scripts/build_pilot.py
.venv/bin/python scripts/validate_resources.py
```

Or run `bash datasets/download.sh` after restoring clones and syncing dependencies. `prepare_datasets.py` downloads raw files from the clones' exact commit hashes. The exact original URLs, revisions, file sizes and SHA-256 values are in `artifacts/dataset_manifest.json`; `artifacts/model_manifest.json` pins tokenizer assets. Retain those manifests when reproducing.

## InjecAgent

- Official source: https://github.com/uiuc-kang-lab/InjecAgent
- Local data: `datasets/InjecAgent/`; 9 files, 4,913,908 bytes.
- License: MIT, see `code/InjecAgent/LICENCE`.
- 17 user cases (`user_cases.jsonl`), 30 direct-harm attacker cases, 32 data-stealing attacker cases. Base condition: 510 direct-harm plus 544 data-stealing cases = 1,054 combinations. Enhanced condition repeats these combinations with a stronger prefix; **do not count base/enhanced as independent tasks**.
- `tools.json` contains 38 toolkits, not 38 individual tools. `attacker_simulated_responses.json` contains 2,347 keyed responses.
- Split: published evaluation cases, not an official training/validation/test split. Make development/confirmation splits by user template for adaptations.
- Schema: user case fields include `User Tool`, `User Instruction`, `Tool Parameters`, `Tool Response Template`, `Thought`, `Level`. Exactly one `<Attacker Instruction>` slot per user template. Parameters and templates can contain Python-style single quotes; parse with `ast.literal_eval`, never `eval`, or normalize deliberately.
- Validation: JSON/JSONL parsed; all 17 required user fields nonempty; each slot present exactly once; all four case-file counts and top-level values checked. See `artifacts/resource_validation.json`.
- Use: schema and insertion-template reference. The original harmful/exfiltration payloads are archival resources; experiment only with benign fictional target edits. Synthetic Thought prefixes and simulated tool outcomes must not define the primary native-agent experiment.
- Literature nuance: Appendix C of the paper describes an InjecAgent-clear benign-response condition, but a separate clear dataset file is not present in this pinned release. Do not claim that clean paired data was downloaded.

```python
import json
from pathlib import Path
user_cases = [json.loads(x) for x in Path('datasets/InjecAgent/user_cases.jsonl').read_text().splitlines()]
base = json.loads(Path('datasets/InjecAgent/test_cases_dh_base.json').read_text())
```

## AgentDojo environment fixtures

- Official source: https://github.com/ethz-spylab/agentdojo
- Local data: `datasets/agentdojo/`; 12 YAML files, 85,249 bytes.
- License: MIT with inherited exceptions documented by upstream; see `code/agentdojo/LICENSE`.
- Four environment suites: workspace, banking, travel, slack; each has an environment and injection-vector specification. Workspace resolves three included YAML files (inbox, calendar, cloud drive). The system-message YAML is also downloaded.
- Data are synthetic application state, not independent labeled rows. Task definitions and executable utility/security predicates remain in `code/agentdojo/src/agentdojo/default_suites/`. The paper's 97 user tasks / 629 security pairs refer to its version; do not infer that count from the current checkout or multiply fixture entries into sample size.
- No standard train/test split. Pin a suite version explicitly if using the full benchmark.
- Validation: all YAML files parse, including workspace's `!include` references via a safe loader that resolves relative to the current file. File-level hashes match.
- Use: reference for deterministic mutable state and utility/security separation. Full benchmark reproduction has greater tool/context burden than the proposed minimal fictional-record suite.

```python
# Reuse the safe include-loading function from scripts/validate_resources.py,
# or AgentDojo's own loader; ordinary yaml.safe_load alone rejects !include.
```

## Generated benign development pilot

- `datasets/benign_record_pilot.jsonl`: 24 fictional worlds across 6 templates, all marked `development_only`. Generated deterministically by `scripts/build_pilot.py`, no model calls and no personal data.
- Four read tasks and two tasks requiring an authorized comment edit, four fictional values each. A separate label edit is the injection target. Fields include initial records, user instruction, authorized-write list, expected answer, clean tool result, authorized-target prompt, and model-specific I/Q tool-result strings.
- For every model/world pair, injection and quotation contain the same target sentence and identical factual fields. Neutral trailing padding makes serialized tool-result token counts **exactly equal**, using each pinned tokenizer (72 matched pairs checked). Different models may get different padding; record this limitation in cross-checkpoint analyses.
- Q explicitly quotes the action sentence. This operationalizes an instruction-versus-quotation framing contrast, not a pure test of identical bytes or authority alone. Match counts again after the runner's complete chat serialization. Padding and quotation framing are residual design choices; counterbalance padding or add matched filler diagnostics before confirmation.
- The authorized-target prompt adds the target change to the trusted user request; its allowed-write set must be augmented correspondingly by the runner. It is not an unauthorized event in that arm.
- **Not a completed benchmark or power sample**: no model clean eligibility or human plausibility validation has been measured. Six templates are too few for strong generalization. Use only to debug before diversifying and freezing the confirmatory pool.
- `datasets/examples.json` contains two readable examples. Generated fixture reuse follows the workspace's license policy; no separate license is asserted.

## Tokenizer and model-card bundles

- `datasets/tokenizers/qwen3/`, `deepseek/`, `moonlight/`: 13 files, 21,319,983 bytes; tokenizer assets, configurations and model cards, no model weights.
- Model IDs and pinned revisions: `artifacts/model_manifest.json`. Qwen Apache-2.0; DeepSeek/Moonlight MIT as indicated by their official cards; retain upstream conditions.
- Moonlight uses `tiktoken.model` and custom tokenizer source rather than `tokenizer.json`. The pilot reads literal regex definitions and BPE ranks without importing or executing the downloaded code. Native inference still requires a compatible implementation, to be validated by the runner.

## Search and suitability

Hugging Face dataset search was checked first (`artifacts/hf_injecagent.json`, `hf_agentdojo.json`). Results included community translations/dumps, so the official author repositories were preferred. Paper-linked resources provided more direct provenance than general tabular/UCI/Kaggle datasets for this task. No user-specified or staged dataset was listed. Neither established dataset supplies the exact clean-eligible, length-matched benign-record contrast; the pilot is explicitly a new adaptation, not a relabeling of established benchmark results.
