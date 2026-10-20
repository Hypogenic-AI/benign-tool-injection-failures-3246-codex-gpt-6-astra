# Benign tool-injection-v1

A custom harmless stateful proxy comparing instruction-bearing tool text with token-matched quoted text and clean utility controls. All subject actions operate on fictional in-memory records; this is not a reproduction of AgentDojo or AgentHarm.

- Recorded 1800/2700 planned held-out episodes on the three requested checkpoints.
- Qwen primary conditional difference: 0.000 (SE 0.000; 95% CI [0.000, 0.000]; n=100); decision: **not supported**.
- Secondary conditional differences: DeepSeek 0.175 (SE 0.036; 95% CI [0.108, 0.250]; n=78); Moonlight undefined.
- Scorer controls: 60/60 agreement (mean 1, SE 0; four categories of 15).
- Local subject inference only; no LLM judge or evaluation API spend. Codex orchestration differed from the requested Claude orchestration.

Full methods, results and limitations: [REPORT.md](REPORT.md).

## Reproduce

```bash
uv sync --project .
source .venv/bin/activate
python src/download_models.py
python src/execute.py
python src/analyze.py
python src/mark_unavailable.py
python src/call_diagnostics.py
python src/validate.py
python src/export_results.py
python src/write_report.py
```

Use one allocated 80GB GPU for subject inference. `src/execute.py` manages sequential server lifecycles. Reanalysis/replay needs no GPU. Input hashes are in `manifests/freeze.json`; do not regenerate the held-out data after inspecting results. `python src/candidates.py` emits a finding only if the preregistered support rule passes.

## Files

- `preregistration.md`, `planning.md`: frozen protocol and rationale.
- `src/`, `manifests/`: reproduction code, scenarios, exact strings, scorer fixtures.
- `results/safety/`, `results/traces/`: schema records and actual model output.
- `results/analysis.json`, `results/item_scores.json`, `results/episode_scores.csv`: statistics and scores.
- `figures/`: exported research plot.
- `literature_review.md`, `resources.md`: gathered background resources.
