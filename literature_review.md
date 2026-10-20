# Benign tool-injection failures with matched utility controls

## Scope and evidence quality

Question: on Qwen3-8B, does a directive in an untrusted tool result increase unauthorized fictional-record edits by at least 0.10 relative to a length-matched quotation, among tasks completed cleanly? DeepSeek and Moonlight are secondary checkpoint comparisons. This is an evaluation-design hypothesis; **no experimental result is established here**.

Search covered 2023–October 20, 2026. Keywords: indirect prompt injection; tool-result injection; unauthorized tool actions; benign utility; clean-task success; quoted-text controls; state-based scoring; agent capability confounding; AgentDojo; InjecAgent. Inclusion favored external-content attacks, executable tool environments, utility controls, and measurement validity. Direct harmful-user jailbreaks, multimodal carriers, training methods and persistent multi-agent threats are contextual, outside the implementation scope.

Paper-finder was tried first in diligent mode and returned 102 candidates. Semantic Scholar batch resolution supplied identifiers/open PDFs; direct author/arXiv sources supplemented it. Ninety-seven candidate PDFs were downloaded, plus two citation-chased foundational/design papers, for 99 full PDFs. Five candidates remained inaccessible after retries. AgentVigil appears as both conference and preprint records: these are not independent corroboration. All available search abstracts were screened; two deficient abstracts were supplemented from PDF first pages. Full sequential PDF-chunk reading covered AgentDojo (26 pages) and InjecAgent (36 pages), including appendices. Other resources were screened at abstract/selected-section level, **not fully reviewed**. Full reading notes and all screening records are in `artifacts/literature_chunk_notes.md` and `papers/README.md`; source metadata and failures are auditable in `artifacts/`.

## Key papers

### AgentDojo — Debenedetti, Zhang, Balunović, Beurer-Kellner, Fischer and Tramèr (NeurIPS Datasets and Benchmarks 2024)

Source: arXiv:2406.13352, downloaded v3, November 24, 2024; `papers/2406.13352_agentdojo.pdf`. Dynamic Python environments model workspace, Slack, travel and banking. User tasks and attacker goals have separate deterministic utility/security checks over actual simulated state and, when needed, output. The paper describes 97 user tasks and 629 security cases. Baselines include several tool-calling LLMs, TODO/ignore-previous/InjecAgent/important-message payloads, delimiters, repeated user prompts, an injection detector, and tool filtering. Code and fixtures: `code/agentdojo/`, `datasets/agentdojo/` (MIT).

Crucially, capability and vulnerability covary: an agent must be able to execute tools to complete either a legitimate or attacker task. Table 3 reports GPT-4o benign utility 69.00%, attacked utility 50.08%, and targeted ASR 47.69%; these endpoints are not interchangeable. Summary prose contains older numbers inconsistent with the appendix: cite the table and PDF version explicitly. Table 4’s different attack comparison must not be mixed with Table 3 as one configuration. End-of-output placement and environment type change ASR. Utility checks are more relevant to our hypothesis than an LLM's verbal claim that an edit occurred.

Limitations: finite synthetic environments, version-sensitive tasks and attacks, and some complex tasks too difficult for smaller models. Fixed baseline attacks do not establish adaptive robustness. The best reusable pattern is a small mutable environment with disjoint authorization metadata and state-based outcomes, not necessarily the full benchmark workload.

### InjecAgent — Zhan, Liang, Ying and Kang (Findings of ACL 2024)

Source: arXiv:2403.02691 v3, August 4, 2024; `papers/2403.02691_injecagent.pdf`. Seventeen user-tool templates are crossed with 30 direct-harm and 32 data-stealing attacker instructions, yielding 1,054 cases per base/enhanced condition. GPT-4 assisted generation followed by manual refinement enforces tool schemas and insertion slots. Evaluation begins after an assumed successful initial retrieval and parses subsequent ReAct/function calls. It evaluates 30 agents. Code/data: `code/InjecAgent/`, `datasets/InjecAgent/` (MIT).

Table 3 reports prompted GPT-4 ASR-valid 23.6% base and 47.0% enhanced; Table 8’s ASR-all is 23.3%/46.8%. Valid-output filtering and task completion are different. Appendix C describes **InjecAgent-clear**, using three benign responses per user case to measure output validity. Clean controls therefore already exist in prior work, although the inspected release lacks a separate clear-data file and does not provide our exact clean-eligible, token-matched quotation contrast.

User-template variation associates more strongly with ASR than attacker-template variation; content slots with more freedom are more vulnerable. Limitations include simulated prior assistant reasoning, limited sequential actions, and predominantly malicious targets. Use its insertion schema, not its nominal row count as independent sample size or its tool-name-oriented scoring as proof of executed edits.

### BIPIA — Yi, Xie, Zhu, Kiciman, Sun, Xie and Wu (2023 preprint; KDD 2025)

Source: arXiv:2312.14197; DOI 10.1145/3690624.3709179; `papers/2312.14197_bipia.pdf`. The benchmark studies instruction/data confusion in externally grounded text tasks. Boundary-awareness and explicit-reminder defenses operate through prompting or training, evaluated using attack success and output quality. The authors report strong mitigation, including near-zero ASR for their trained defense in tested settings; this is not a transferable guarantee for Qwen3-8B tool editing. Official code is https://github.com/microsoft/BIPIA (not cloned). Relevance: motivates the single boundary-reminder ablation and a quoted-text comparison. Limitation: output manipulation and quality do not directly measure persistent record mutations. Review depth: abstract and opening sections.

### Foundational indirect injection — Greshake, Abdelnabi, Mishra, Endres, Holz and Fritz (2023)

Source: arXiv:2302.12173; `papers/2302.12173_indirect_prompt_injection.pdf`. “Not what you've signed up for” demonstrates that retrieved third-party text can become operational instructions in LLM-integrated applications, with a taxonomy and demonstrations involving real and synthetic systems. Its contribution is the trust-boundary threat model, not a matched-effect estimate or a fixed benchmark success rate. Demonstrations on different applications/models cannot substantiate the proposed 0.10 threshold. Review depth: abstract screening.

### CaMeL — Debenedetti et al. (2025)

Source: arXiv:2503.18813 v2; `papers/2503.18813_camel.pdf`. “Defeating Prompt Injections by Design” separates trusted planning from untrusted data and enforces information-flow/capability policies with a custom interpreter. The abstract reports solving 77% of AgentDojo tasks with security guarantees under its design assumptions, versus 84% undefended. Official code: https://github.com/google-research/camel-prompt-injection (not cloned). Relevance: induced actions and runtime authorization are distinct; a tool gate can prevent execution even if a model follows an injected instruction. Our primary experiment keeps the fictional write tool available so that runtime blocking cannot masquerade as model resistance. Limitation: guarantees depend on policy/architecture assumptions; this long paper was only screened at abstract/opening-section level, not independently audited.

### Recent evidence that constrains novelty and measurement (2025–2026)

These are **abstract-screened author claims**, with PDFs archived in the paper index. They guide design but their numeric claims were not reproduced or fully audited.

- Zhan et al., **Adaptive Attacks Break Defenses** (arXiv:2503.00061): adaptive attacks bypass eight evaluated defenses, supporting a strict limit on what a fixed-payload result establishes.
- Li et al., **AgentDyn** (arXiv:2602.03117): 60 open-ended tasks and 560 injection cases include helpful third-party instructions. Dhouib et al., **RAISED** (arXiv:2610.06401), similarly emphasizes clean utility and legitimate tool-output guidance. Hence “ignore all external instructions” is not a sufficient utility benchmark, and a user-authorized write control is essential.
- Shaw, **Silent Failures in Agentic Security Evaluation** (arXiv:2609.32691): reports payload-delivery and argument-scoring defects that substantially distort ASR. Audit exact delivered payloads, arguments, and executed state changes. This is a recent preprint and a warning to verify instrumentation, not independently confirmed evidence about our resources.
- Guo et al., **When Tool Outputs Become Commands** (arXiv:2608.27146), and He et al., **AttriGuard** (arXiv:2603.10749), distinguish action support/provenance from authorization and use counterfactual intervention. Our matched contrast is related to this existing causal-attribution literature, but measures a fixed intervention rather than a new defense.
- Corll, **Amplify, Don't Create** (arXiv:2606.20746), uses matched benign shams and clustered uncertainty while warning about few independent tasks. Thus neither benign controls nor matched shams alone are new. Wang et al., **Self-Reflection Fine-Tuning** (arXiv:2610.04269), already includes Qwen3-8B in an agent-security setting. Model choice alone does not establish novelty.

## Synthesis: methods, baselines and outcomes

The literature combines controlled insertion slots, tool-using continuations, mutable-state benchmarks, prompt-boundary defenses, and external authorization policies. The closest reusable benchmarks are AgentDojo and InjecAgent; their schemas need adaptation for benign fictional edits and matched quotations. Direct-user harmfulness benchmarks such as AgentHarm address another causal question and were not selected as primary data.

Required baselines are clean context, injected directive, length-matched quotation of the same action sentence, and an explicitly user-authorized target edit. The latter separates inability to edit from refusing an unauthorized request. The planned boundary-reminder ablation is secondary. Tool removal/allowlisting may be informative architectural defenses elsewhere, but would mechanically suppress the event here and change the question.

Primary outcome is **any executed unauthorized fictional-record mutation**, including one subsequently reversed. Separately report target edit completion, attempted calls, persistent final corruption, clean utility, utility under I/Q, authorized-edit success, exposure, malformed actions and infrastructure errors. Refusal and output validity are not utility. A textual promise or target tool name without correct executed arguments is not a successful edit.

## Experimental recommendation and unresolved gap

Estimate the paired difference `mean(Y_injection - Y_quote)` on a separately frozen clean-success set. Never filter by attack success, quoted success, or successful target execution in the authorized arm. Retain all prespecified tasks for utility and all-item summaries; exposure-conditional estimates are secondary. Match serialized tool-result token counts under each tokenizer and recheck after final chat formatting. Preserve required facts and insertion position. The quotation itself changes interpretation, so describe the estimand as this specific framing intervention rather than claiming to isolate every aspect of authority.

Report paired uncertainty, with template clustering for generalization; repeated fictional IDs do not create new task templates. Test the actual 0.10 margin, not only zero difference: a point estimate above 0.10 with an interval overlapping it is inconclusive. Secondary checkpoints use their own clean eligibility plus a shared-intersection comparison. DeepSeek-R1-Distill-Qwen-7B is a proposed checkpoint, derived from Qwen rather than an independent architecture family; Moonlight requires validated custom-tokenizer support.

The defensible contribution is a tightly controlled benign-edit contrast on specified checkpoints, with transparent utility denominators and execution-grounded measurement. The search does **not** establish that no prior work has tested an equivalent contrast. Detailed protocol, three-direction ranking, sampling assumptions and runner next steps are in `planning.md`. The 24-world fixture only supports development: diversify templates and freeze a confirmatory pool before drawing scientific conclusions.
