# Downloaded papers and screening index

102 paper-finder records screened; 97 candidate PDFs downloaded plus two supplemental papers = 99 full PDF files. AgentVigil conference/preprint records represent related versions, not independent studies. Five candidate PDFs remain unavailable. Service relevance is retained separately from local reading priority. Main synthesis: `../literature_review.md`; sequential full-reading notes: `../artifacts/literature_chunk_notes.md`.

Review depth: only AgentDojo and InjecAgent received full all-chunk review. All other entries are abstract/selected-section screening; absent sample-size, baseline, or metric details must be recovered from the PDF before quantitative reuse. Screening notes are interpretive summaries, not replicated results.

## 1. InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents
- Authors: Qiusi Zhan, Zhi-Xiang Liang, Zifan Ying, Daniel Kang
- Year: 2024; source: https://api.semanticscholar.org/CorpusId:268248325
- Local PDF: [2403.02691_injecagent.pdf](2403.02691_injecagent.pdf)
- Service relevance: 3/3; local decision: Core full review.
- Method / relevance / limitation: Controlled tool-result templates; valid/all denominators and clear benign responses. Core schema reference; complete PDF reviewed.
- Identifiers: {"DBLP": "journals/corr/abs-2403-02691", "ArXiv": "2403.02691", "DOI": "10.48550/arXiv.2403.02691", "CorpusId": 268248325}
- Code referenced by abstract (not necessarily cloned): https://github.com/uiuc-kang-lab/InjecAgent.

## 2. Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents
- Authors: Qiusi Zhan, Richard Fang, H. Panchal, Daniel Kang
- Year: 2025; source: https://www.semanticscholar.org/paper/0ed8da38a5fb60cd5fc70d325a63e6120111756c
- Local PDF: [2503.00061_adaptive_attacks_break_defenses_against_indirect_prompt_injection_attacks_on_llm_agents.pdf](2503.00061_adaptive_attacks_break_defenses_against_indirect_prompt_injection_attacks_on_llm_agents.pdf)
- Service relevance: 3/3; local decision: Design support.
- Method / relevance / limitation: Adaptive evaluation challenges static-defense claims. Contextual limitation, not an additional implementation direction.
- Identifiers: {"DBLP": "conf/naacl/ZhanFPK25", "ArXiv": "2503.00061", "DOI": "10.48550/arXiv.2503.00061", "CorpusId": 276741414}
- Code referenced by abstract (not necessarily cloned): https://github.com/uiuc-kang-lab/AdaptiveAttackAgent.

## 3. AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents
- Authors: Edoardo Debenedetti, Jie Zhang, Mislav Balunovic, Luca Beurer-Kellner, Marc Fischer, Florian Tramèr
- Year: 2024; source: https://www.semanticscholar.org/paper/cf95279b1da9de1aad9e7c651f5048f69af295ed
- Local PDF: [2406.13352_agentdojo.pdf](2406.13352_agentdojo.pdf)
- Service relevance: 3/3; local decision: Core full review.
- Method / relevance / limitation: Dynamic mutable environments with independent utility and security checks. Core environment reference; complete PDF reviewed.
- Identifiers: {"ArXiv": "2406.13352", "DBLP": "journals/corr/abs-2406-13352", "DOI": "10.48550/arXiv.2406.13352", "CorpusId": 270619628}
- Code referenced by abstract (not necessarily cloned): https://github.com/ethz-spylab/agentdojo.

## 4. The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents
- Authors: Feiran Jia, Tong Wu, Xin Qin, A. Squicciarini
- Year: 2024; source: https://api.semanticscholar.org/CorpusId:274981671
- Local PDF: [2412.16682_the_task_shield_enforcing_task_alignment_to_defend_against_indirect_prompt_injection_in_ll.pdf](2412.16682_the_task_shield_enforcing_task_alignment_to_defend_against_indirect_prompt_injection_in_ll.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Checks whether actions serve the user task; relevant authorization perspective, but a new defense is outside scope.
- Identifiers: {"DBLP": "journals/corr/abs-2412-16682", "ArXiv": "2412.16682", "DOI": "10.48550/arXiv.2412.16682", "CorpusId": 274981671}

## 5. MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents
- Authors: Kai-Jie Zhu, Xianjun Yang, Jin-Dong Wang, Wen-Bo Guo, William Yang Wang
- Year: 2025; source: https://api.semanticscholar.org/CorpusId:276235401
- Local PDF: [2502.05174_melon_provable_defense_against_indirect_prompt_injection_attacks_in_ai_agents.pdf](2502.05174_melon_provable_defense_against_indirect_prompt_injection_attacks_in_ai_agents.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Masked-user replay compares actions; useful counterfactual context, not our primary intervention.
- Identifiers: {"DBLP": "conf/icml/ZhuY00W25", "ArXiv": "2502.05174", "CorpusId": 276235401}
- Code referenced by abstract (not necessarily cloned): https://github.com/kaijiezhu11/MELON.

## 6. Progent: Securing AI Agents with Privilege Control
- Authors: Tian-Neng Shi, Jingxuan He, Zhun Wang, Hong-Wei Li, Linyu Wu, Wen-Bo Guo, D. Song
- Year: 2025; source: https://www.semanticscholar.org/paper/d38e9870513e8933b0eb5abe51708470105d57a5
- Local PDF: [2504.11703_progent_securing_ai_agents_with_privilege_control.pdf](2504.11703_progent_securing_ai_agents_with_privilege_control.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Symbolic tool privileges and constrained policy updates; runtime restrictions differ from model susceptibility.
- Identifiers: {"ArXiv": "2504.11703", "CorpusId": 277824060}

## 7. PromptArmor: Simple yet Effective Prompt Injection Defenses
- Authors: Tian-Neng Shi, Kai-Jie Zhu, Zhun Wang, Yu-Qi Jia, Will Cai, Wei-Da Liang, Haonan Wang, Hend Alzahrani, Joshua Lu, Kenji Kawaguchi, Basel Alomair, Xuandong Zhao, William Yang Wang, N. Gong, Wen-Bo Guo, D. Song
- Year: 2025; source: https://api.semanticscholar.org/CorpusId:280282510
- Local PDF: [2507.15219_promptarmor_simple_yet_effective_prompt_injection_defenses.pdf](2507.15219_promptarmor_simple_yet_effective_prompt_injection_defenses.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Model-based input sanitization with detector error rates; not selected for implementation.
- Identifiers: {"DBLP": "journals/corr/abs-2507-15219", "ArXiv": "2507.15219", "DOI": "10.48550/arXiv.2507.15219", "CorpusId": 280282510}

## 8. AgentDyn: Are Your Agent Security Defenses Deployable in Real-World Dynamic Environments?
- Authors: Hao Li, Ruoyao Wen, Shang-Hao Shi, Ning Zhang, Yevgeniy Vorobeychik, Chao-Wei Xiao
- Year: 2026; source: https://www.semanticscholar.org/paper/1d86e0762647c3405e6554e0be47d4f8ccb4d4e2
- Local PDF: [2602.03117_agentdyn_are_your_agent_security_defenses_deployable_in_real_world_dynamic_environments.pdf](2602.03117_agentdyn_are_your_agent_security_defenses_deployable_in_real_world_dynamic_environments.pdf)
- Service relevance: 3/3; local decision: Design support.
- Method / relevance / limitation: Open-ended tasks include useful external guidance, exposing utility loss from indiscriminate blocking.
- Identifiers: {"ArXiv": "2602.03117", "CorpusId": 285276160}
- Code referenced by abstract (not necessarily cloned): https://github.com/leolee99/AgentDyn.

## 9. AGENTVIGIL: Automatic Black-Box Red-teaming for Indirect Prompt Injection against LLM Agents
- Authors: Zhun Wang, Vincent Siu, Zhe Ye, Tian-Neng Shi, Yu-Zhou Nie, Xuandong Zhao, Chen-Guang Wang, Wen-Bo Guo, D. Song
- Year: 2025; source: https://www.semanticscholar.org/paper/f502fd8f67f3f849d5ab19cc2cb694e0de2c7d4f
- Local PDF: [paper_agentvigil_automatic_black_box_red_teaming_for_indirect_prompt_injection_against_llm_agent.pdf](paper_agentvigil_automatic_black_box_red_teaming_for_indirect_prompt_injection_against_llm_agent.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Conference version of AgentVigil; incomplete service abstract replaced by PDF first-page screening. Do not count as independent evidence from preprint.
- Identifiers: {"DBLP": "conf/emnlp/WangSYSNZWGS25", "DOI": "10.18653/v1/2025.findings-emnlp.1258", "CorpusId": 282905125}

## 10. AgentVigil: Generic Black-Box Red-teaming for Indirect Prompt Injection against LLM Agents
- Authors: Zhun Wang, Vincent Siu, Zhe Ye, Tian-Neng Shi, Yu-Zhou Nie, Xuandong Zhao, Chen-Guang Wang, Wen-Bo Guo, D. Song
- Year: 2025; source: https://api.semanticscholar.org/CorpusId:278481145
- Local PDF: [2505.05849_agentvigil_generic_black_box_red_teaming_for_indirect_prompt_injection_against_llm_agents.pdf](2505.05849_agentvigil_generic_black_box_red_teaming_for_indirect_prompt_injection_against_llm_agents.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Black-box search with MCTS across agent benchmarks; adaptive optimization is outside the fixed-payload hypothesis.
- Identifiers: {"ArXiv": "2505.05849", "CorpusId": 278481145}

## 11. IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents
- Authors: Heng-Yu An, Jinghuai Zhang, Tianyu Du, Chun-Yi Zhou, Qing-Ming Li, Tao Lin, Shou-Ling Ji
- Year: 2025; source: https://api.semanticscholar.org/CorpusId:280700086
- Local PDF: [2508.15310_ipiguard_a_novel_tool_dependency_graph_based_defense_against_indirect_prompt_injection_in_.pdf](2508.15310_ipiguard_a_novel_tool_dependency_graph_based_defense_against_indirect_prompt_injection_in_.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Preplanned tool dependencies restrict execution; structural defense changes available action space.
- Identifiers: {"ArXiv": "2508.15310", "DBLP": "journals/corr/abs-2508-15310", "DOI": "10.48550/arXiv.2508.15310", "CorpusId": 280700086}

## 12. ACE: A Security Architecture for LLM-Integrated App Systems
- Authors: E. Li, Tushin Mallick, Evan Rose, William K. Robertson, Alina Oprea, Cristina Nita-Rotaru
- Year: 2025; source: https://api.semanticscholar.org/CorpusId:278171668
- Local PDF: [2504.20984_ace_a_security_architecture_for_llm_integrated_app_systems.pdf](2504.20984_ace_a_security_architecture_for_llm_integrated_app_systems.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Separates abstract planning, concrete app mapping and execution with information-flow checks.
- Identifiers: {"DBLP": "journals/corr/abs-2504-20984", "ArXiv": "2504.20984", "DOI": "10.14722/ndss.2026.230352", "CorpusId": 278171668}

## 13. Defending Against Prompt Injection with DataFilter
- Authors: Yizhu Wang, Si-Zhe Chen, Raghad F Alkhudair, Basel Alomair, David A. Wagner
- Year: 2025; source: https://api.semanticscholar.org/CorpusId:282271955
- Local PDF: [2510.19207_defending_against_prompt_injection_with_datafilter.pdf](2510.19207_defending_against_prompt_injection_with_datafilter.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Task-conditioned sanitization removes injected content; requires trained defense rather than a matched utility experiment.
- Identifiers: {"DBLP": "journals/corr/abs-2510-19207", "ArXiv": "2510.19207", "DOI": "10.1109/SaTML68715.2026.00017", "CorpusId": 282271955}

## 14. Simple Prompt Injection Attacks Can Leak Personal Data Observed by LLM Agents During Task Execution
- Authors: Meysam Alizadeh, Zeynab Samei, Daria Stetsenko, Fabrizio Gilardi
- Year: 2025; source: https://api.semanticscholar.org/CorpusId:279074865
- Local PDF: [2506.01055_simple_prompt_injection_attacks_can_leak_personal_data_observed_by_llm_agents_during_task_.pdf](2506.01055_simple_prompt_injection_attacks_can_leak_personal_data_observed_by_llm_agents_during_task_.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Fictional banking data-flow attacks connect task structure and exfiltration; use only as contextual evidence.
- Identifiers: {"DBLP": "journals/corr/abs-2506-01055", "ArXiv": "2506.01055", "DOI": "10.48550/arXiv.2506.01055", "CorpusId": 279074865}

## 15. AgentSentry: Mitigating Indirect Prompt Injection in LLM Agents via Temporal Causal Diagnostics and Context Purification
- Authors: Tianke Zhang, Yi-Wei Xu, Juan Wang, Keyan Guo, Xiaoyang Xu, Bowen Xiao, Quanlong Guan, Jinlin Fan, Jia-Wei Liu, Zhiquan Liu, Hongxin Hu
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:286083518
- Local PDF: [2602.22724_agentsentry_mitigating_indirect_prompt_injection_in_llm_agents_via_temporal_causal_diagnos.pdf](2602.22724_agentsentry_mitigating_indirect_prompt_injection_in_llm_agents_via_temporal_causal_diagnos.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Counterfactual replay at tool boundaries localizes deviations and supports recovery.
- Identifiers: {"ArXiv": "2602.22724", "DBLP": "journals/corr/abs-2602-22724", "DOI": "10.48550/arXiv.2602.22724", "CorpusId": 286083518}

## 16. Indirect Prompt Injections: Are Firewalls All You Need, or Stronger Benchmarks?
- Authors: Rishika Bhagwatkar, Kevin Kasa, Abhay Puri, Gabriel Huang, Irina Rish, Graham W. Taylor, K. Dvijotham, Alexandre Lacoste
- Year: 2025; source: https://api.semanticscholar.org/CorpusId:281886462
- Local PDF: [2510.05244_indirect_prompt_injections_are_firewalls_all_you_need_or_stronger_benchmarks.pdf](2510.05244_indirect_prompt_injections_are_firewalls_all_you_need_or_stronger_benchmarks.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Tool-interface firewalls and benchmark auditing emphasize metric validity and stronger attacks.
- Identifiers: {"ArXiv": "2510.05244", "DBLP": "journals/corr/abs-2510-05244", "DOI": "10.48550/arXiv.2510.05244", "CorpusId": 281886462}

## 17. AgentArmor: Enforcing Program Analysis on Agent Runtime Trace to Defend Against Prompt Injection
- Authors: Peiran Wang, Yang Liu, Yun-Fei Lu, Yifeng Cai, Hongbo Chen, Qingyou Yang, Jie Zhang, Jue Hong, Ye Wu
- Year: 2025; source: https://www.semanticscholar.org/paper/46a4e8c7d5fb84288c067c9ee769273a591226f2
- Local PDF: [2508.01249_agentarmor_enforcing_program_analysis_on_agent_runtime_trace_to_defend_against_prompt_inje.pdf](2508.01249_agentarmor_enforcing_program_analysis_on_agent_runtime_trace_to_defend_against_prompt_inje.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Graph representations of runtime traces support program-analysis security policies.
- Identifiers: {"DBLP": "journals/corr/abs-2508-01249", "ArXiv": "2508.01249", "DOI": "10.48550/arXiv.2508.01249", "CorpusId": 280422396}

## 18. CausalArmor: Efficient Indirect Prompt Injection Guardrails via Causal Attribution
- Authors: Minbeom Kim, Mihir Parmar, Phillip Wallis, Lesly Miculicich, Kyomin Jung, K. Dvijotham, Long T. Le, Tomas Pfister
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:285453708
- Local PDF: [2602.07918_causalarmor_efficient_indirect_prompt_injection_guardrails_via_causal_attribution.pdf](2602.07918_causalarmor_efficient_indirect_prompt_injection_guardrails_via_causal_attribution.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Ablation-based attribution selectively triggers sanitization; causal attribution is established related work.
- Identifiers: {"DBLP": "journals/corr/abs-2602-07918", "ArXiv": "2602.07918", "DOI": "10.48550/arXiv.2602.07918", "CorpusId": 285453708}

## 19. PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses
- Authors: Chen-Long Yin, Runpeng Geng, Yan-Ting Wang, Jin-Yuan Jia
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:286519920
- Local PDF: [2603.13026_pismith_reinforcement_learning_based_red_teaming_for_prompt_injection_defenses.pdf](2603.13026_pismith_reinforcement_learning_based_red_teaming_for_prompt_injection_defenses.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: RL search improves adaptive attack discovery; training and optimization are pruned from implementation.
- Identifiers: {"DBLP": "journals/corr/abs-2603-13026", "ArXiv": "2603.13026", "DOI": "10.48550/arXiv.2603.13026", "CorpusId": 286519920}
- Code referenced by abstract (not necessarily cloned): https://github.com/albert-y1n/PISmith.

## 20. A Survey on Agentic Security: Applications, Threats and Defenses
- Authors: Asif Shahriar, Md Nafiu Rahman, Sadif Ahmed, Farig Sadeque, Md. Rizwan Parvez
- Year: 2025; source: https://www.semanticscholar.org/paper/088e1cc233bde4491d067e706240381d7793aa9b
- Local PDF: [2510.06445_a_survey_on_agentic_security_applications_threats_and_defenses.pdf](2510.06445_a_survey_on_agentic_security_applications_threats_and_defenses.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Broad agent-security survey; background rather than primary evidence for a paired effect.
- Identifiers: {"ArXiv": "2510.06445", "DBLP": "journals/corr/abs-2510-06445", "DOI": "10.48550/arXiv.2510.06445", "CorpusId": 281892378}

## 21. Defense Against Indirect Prompt Injection via Tool Result Parsing
- Authors: Qiang Yu, Xin-Ran Cheng, Chuanyi Liu
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:284544560
- Local PDF: [2601.04795_defense_against_indirect_prompt_injection_via_tool_result_parsing.pdf](2601.04795_defense_against_indirect_prompt_injection_via_tool_result_parsing.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Parsing tool results into data aims to remove commands; may alter useful content and needs utility assessment.
- Identifiers: {"DBLP": "journals/corr/abs-2601-04795", "ArXiv": "2601.04795", "DOI": "10.48550/arXiv.2601.04795", "CorpusId": 284544560}

## 22. VeriGrey: Greybox Agent Validation
- Authors: Yun-Tong Zhang, S. Kang, Rui-Jie Meng, Marcel Böhme, Abhik Roychoudhury
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:286643546
- Local PDF: [2603.17639_verigrey_greybox_agent_validation.pdf](2603.17639_verigrey_greybox_agent_validation.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Tool-sequence feedback drives greybox mutation; adaptive discovery is outside the selected intervention.
- Identifiers: {"ArXiv": "2603.17639", "DBLP": "journals/corr/abs-2603-17639", "DOI": "10.48550/arXiv.2603.17639", "CorpusId": 286643546}

## 23. Taxonomy, Evaluation and Exploitation of IPI-Centric LLM Agent Defense Frameworks
- Authors: Zimo Ji, Xun-Guang Wang, Zong-Jie Li, Pingchuan Ma, Yu-Dong Gao, Dao-Yuan Wu, Xincheng Yan, Tian Tian, Shuai Wang
- Year: 2025; source: https://www.semanticscholar.org/paper/66c8e83ed0fc215dc8be0e44715a692ef27f005b
- Local PDF: [2511.15203_taxonomy_evaluation_and_exploitation_of_ipi_centric_llm_agent_defense_frameworks.pdf](2511.15203_taxonomy_evaluation_and_exploitation_of_ipi_centric_llm_agent_defense_frameworks.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Defense taxonomy and circumvention analysis; background for limitations of general robustness claims.
- Identifiers: {"ArXiv": "2511.15203", "DBLP": "journals/corr/abs-2511-15203", "DOI": "10.48550/arXiv.2511.15203", "CorpusId": 283103202}

## 24. AutoDojo: A Generative Benchmark for Evaluating Prompt Injection Defenses in LLM Agents
- Authors: Xinhang Ma, Taoran Li, Chao-Wei Xiao, Zhiyuan Yu, Ning Zhang, Yevgeniy Vorobeychik
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:289300189
- Local PDF: [2606.15057_autodojo_a_generative_benchmark_for_evaluating_prompt_injection_defenses_in_llm_agents.pdf](2606.15057_autodojo_a_generative_benchmark_for_evaluating_prompt_injection_defenses_in_llm_agents.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Generates adaptive attacks across AgentDojo and AgentDyn; changes attacker budget and distribution.
- Identifiers: {"ArXiv": "2606.15057", "CorpusId": 289300189}
- Code referenced by abstract (not necessarily cloned): https://github.com/xhOwenMa/AutoDojo

## 25. SecInfer: Preventing Prompt Injection via Inference-time Scaling
- Authors: Yupei Liu, Yan-Ting Wang, Yu-Qi Jia, Jin-Yuan Jia, N. Gong
- Year: 2025; source: https://api.semanticscholar.org/CorpusId:281674810
- Local PDF: [2509.24967_secinfer_preventing_prompt_injection_via_inference_time_scaling.pdf](2509.24967_secinfer_preventing_prompt_injection_via_inference_time_scaling.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Sampling and task-guided aggregation trade additional inference for defense; not selected.
- Identifiers: {"DBLP": "journals/corr/abs-2509-24967", "ArXiv": "2509.24967", "DOI": "10.48550/arXiv.2509.24967", "CorpusId": 281674810}

## 26. Will the User Ever Know? Covert Indirect Prompt Injection Attacks on Tool-Using LLM Agents
- Authors: Yunseok Lee, Yunji Kim, Woo-Jin Lee
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:291542510
- Local PDF: [2608.30362_will_the_user_ever_know_covert_indirect_prompt_injection_attacks_on_tool_using_llm_agents.pdf](2608.30362_will_the_user_ever_know_covert_indirect_prompt_injection_attacks_on_tool_using_llm_agents.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Distinguishes covert and overt successful actions; final response alone can miss actual modifications.
- Identifiers: {"ArXiv": "2608.30362", "CorpusId": 291542510}

## 27. CommandSans: Securing AI Agents with Surgical Precision Prompt Sanitization
- Authors: Debeshee Das, Luca Beurer-Kellner, Marc Fischer, Maximilian Baader
- Year: 2025; source: https://www.semanticscholar.org/paper/7831394c96fc49695da441d91159f1e9f2e68251
- Local PDF: [2510.08829_commandsans_securing_ai_agents_with_surgical_precision_prompt_sanitization.pdf](2510.08829_commandsans_securing_ai_agents_with_surgical_precision_prompt_sanitization.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Token-level removal of agent-directed instructions; quotation/framing controls are important for assessing collateral loss.
- Identifiers: {"ArXiv": "2510.08829", "DBLP": "journals/corr/abs-2510-08829", "DOI": "10.48550/arXiv.2510.08829", "CorpusId": 282055975}

## 28. Your Agent is More Brittle Than You Think: Uncovering Indirect Injection Vulnerabilities in Agentic LLMs
- Authors: Wen-Hui Zhu, Xuan-Zhao Dong, Xi-Wen Chen, Rui Cai, Pei-Jie Qiu, Zhi-Peng Wang, Oana Frunza, Shao Tang, Jin-Dong Gu, Yalin Wang
- Year: 2026; source: https://www.semanticscholar.org/paper/b02c2db7580b600815a486dce0766df5e2987a7c
- Local PDF: [2604.03870_your_agent_is_more_brittle_than_you_think_uncovering_indirect_injection_vulnerabilities_in.pdf](2604.03870_your_agent_is_more_brittle_than_you_think_uncovering_indirect_injection_vulnerabilities_in.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Dynamic attack/defense evaluation and hidden-state intervention; probes are outside the selected directions.
- Identifiers: {"DBLP": "journals/corr/abs-2604-03870", "ArXiv": "2604.03870", "DOI": "10.48550/arXiv.2604.03870", "CorpusId": 287199956}

## 29. Self-Reflection Fine-Tuning: Enhancing Agent Security against Prompt Injection Attacks from Failure Experience
- Authors: Zi-Xu Wang, Hao Li, Feng Gao, G. Suh, Yi Zeng, Yevgeniy Vorobeychik, Ning Zhang, Chao-Wei Xiao
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:292639359
- Local PDF: [2610.04269_self_reflection_fine_tuning_enhancing_agent_security_against_prompt_injection_attacks_from.pdf](2610.04269_self_reflection_fine_tuning_enhancing_agent_security_against_prompt_injection_attacks_from.pdf)
- Service relevance: 3/3; local decision: Design support.
- Method / relevance / limitation: Self-reflection training includes Qwen3-8B, so this checkpoint alone is not a novel contribution.
- Identifiers: {"ArXiv": "2610.04269", "CorpusId": 292639359}
- Code referenced by abstract (not necessarily cloned): https://github.com/Eden-Wang1710/srft-repo.

## 30. ChatInject: Abusing Chat Templates for Prompt Injection in LLM Agents
- Authors: Hwan Chang, Yonghyun Jun, Hwanhee Lee
- Year: 2025; source: https://api.semanticscholar.org/CorpusId:281676128
- Local PDF: [2509.22830_chatinject_abusing_chat_templates_for_prompt_injection_in_llm_agents.pdf](2509.22830_chatinject_abusing_chat_templates_for_prompt_injection_in_llm_agents.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Chat-template impersonation makes exact serialized roles and wrappers part of the threat model.
- Identifiers: {"ArXiv": "2509.22830", "DBLP": "journals/corr/abs-2509-22830", "DOI": "10.48550/arXiv.2509.22830", "CorpusId": 281676128}

## 31. DRIFT: Dynamic Rule-Based Defense with Injection Isolation for Securing LLM Agents
- Authors: Hao Li, Xiaogeng Liu, Hung-Chun Chiu, Dianqi Li, Ning Zhang, Chao-Wei Xiao
- Year: 2025; source: https://www.semanticscholar.org/paper/ec9062053726fa4c501b7deb016b2174bd93cc21
- Local PDF: [2506.12104_drift_dynamic_rule_based_defense_with_injection_isolation_for_securing_llm_agents.pdf](2506.12104_drift_dynamic_rule_based_defense_with_injection_isolation_for_securing_llm_agents.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Dynamic policies, planning and context isolation; architectural defense outside the primary contrast.
- Identifiers: {"DBLP": "conf/nips/LiLCLZX25", "ArXiv": "2506.12104", "DOI": "10.48550/arXiv.2506.12104", "CorpusId": 279403157}

## 32. From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors
- Authors: Jiejun Tan, Zhicheng Dou, Xin-Yu Yang, Yuyang Hu, Yi-Ruo Cheng, Xiaoxi Li, Jia-Ning Wen
- Year: 2026; source: https://www.semanticscholar.org/paper/ce9d30735c0c27de65e68b228d77381d77f2a28b
- Local PDF: [2605.31042_from_prompt_injection_to_persistent_control_defending_agentic_harness_against_trojan_backd.pdf](2605.31042_from_prompt_injection_to_persistent_control_defending_agentic_harness_against_trojan_backd.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Persistent workspace control creates multi-stage threats beyond the single-tool-return scope.
- Identifiers: {"DBLP": "journals/corr/abs-2605-31042", "ArXiv": "2605.31042", "DOI": "10.48550/arXiv.2605.31042", "CorpusId": 288814599}

## 33. Governance Architecture for Autonomous Agent Systems: Threats, Framework, and Engineering Practice
- Authors: Yu Ge
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:286371764
- Local PDF: [2603.07191_governance_architecture_for_autonomous_agent_systems_threats_framework_and_engineering_pra.pdf](2603.07191_governance_architecture_for_autonomous_agent_systems_threats_framework_and_engineering_pra.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Layered governance and judge cascades; not a direct matched benign record-edit estimate.
- Identifiers: {"ArXiv": "2603.07191", "DBLP": "journals/corr/abs-2603-07191", "DOI": "10.48550/arXiv.2603.07191", "CorpusId": 286371764}

## 34. Evaluating Indirect Prompt Injection Defenses in Tool-Using LLM Agents: Security, Utility, and Replication
- Authors: Adil Khan, Khaled AlKhanbashi, Azza Mohamed
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:291654459
- Local PDF: [paper_33_evaluating_indirect_prompt_injection_defenses_in_tool_using_llm_agents.pdf](paper_33_evaluating_indirect_prompt_injection_defenses_in_tool_using_llm_agents.pdf)
- Service relevance: 3/3; local decision: Design support.
- Method / relevance / limitation: Replication study emphasizes goal reachability, benign utility and run variation when ASR is low.
- Identifiers: {"DOI": "10.3390/computers15090570", "CorpusId": 291654459}

## 35. Reachability-Based Capability Confinement for LLM Agents under Indirect Prompt Injection
- Authors: Wu-Jie Xiong, Rabimba Karanjai, Yang Lu, Wei-Dong Shi, Lei Xu
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:291542481
- Local PDF: [2608.30041_reachability_based_capability_confinement_for_llm_agents_under_indirect_prompt_injection.pdf](2608.30041_reachability_based_capability_confinement_for_llm_agents_under_indirect_prompt_injection.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Reachability-based capability restriction; runtime tool restriction must not masquerade as model resistance.
- Identifiers: {"ArXiv": "2608.30041", "CorpusId": 291542481}

## 36. Soft Instruction De-escalation Defense
- Authors: Nils Philipp Walter, Chawin Sitawarin, Jamie Hayes, David Stutz, Ilia Shumailov
- Year: 2025; source: https://www.semanticscholar.org/paper/a33345c6aca10d3979aa33c612e8ca18363ce53d
- Local PDF: [2510.21057_soft_instruction_de_escalation_defense.pdf](2510.21057_soft_instruction_de_escalation_defense.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Iterative rewriting of external instructions; non-imperative payloads limit guarantees.
- Identifiers: {"ArXiv": "2510.21057", "DBLP": "journals/corr/abs-2510-21057", "DOI": "10.48550/arXiv.2510.21057", "CorpusId": 282384291}

## 37. RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents
- Authors: Mohamed Dhouib, Clément Elliker, Alexi Canesse, Maël Jenny, Lucas Thil, M. El Sharkawy, S. Vanier, Elie Bursztein
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:292655701
- Local PDF: [2610.06401_raised_self_distillation_for_robustness_to_prompt_injection_in_llm_agents.pdf](2610.06401_raised_self_distillation_for_robustness_to_prompt_injection_in_llm_agents.pdf)
- Service relevance: 3/3; local decision: Design support.
- Method / relevance / limitation: Self-distillation targets robustness while preserving legitimate use of tool-provided guidance.
- Identifiers: {"ArXiv": "2610.06401", "CorpusId": 292655701}

## 38. Can CaMeLs Talk? Securing Multi-Agent Systems Against Indirect Prompt Injection Attacks
- Authors: James Peters-Gill, Avi Semler, Henning Bartsch, I. Shumailov, C. D. de Witt
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:292655365
- Local PDF: [2610.05640_can_camels_talk_securing_multi_agent_systems_against_indirect_prompt_injection_attacks.pdf](2610.05640_can_camels_talk_securing_multi_agent_systems_against_indirect_prompt_injection_attacks.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Multi-agent composition can change provenance guarantees; outside the single-agent scope.
- Identifiers: {"ArXiv": "2610.05640", "CorpusId": 292655365}

## 39. Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents
- Authors: Praneeth Narisetty, Shivanand Kore, Uday Kumar Reddy Kattamanchi, Jayaram Kumarapu
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:289625855
- Local PDF: [2606.26479_adaptive_evaluation_of_out_of_band_defenses_against_prompt_injection_in_llm_agents.pdf](2606.26479_adaptive_evaluation_of_out_of_band_defenses_against_prompt_injection_in_llm_agents.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Small-scale adaptive evaluation of external enforcement; useful warning about limited attack/model generality.
- Identifiers: {"DBLP": "journals/corr/abs-2606-26479", "ArXiv": "2606.26479", "DOI": "10.48550/arXiv.2606.26479", "CorpusId": 289625855}

## 40. PromptLocate: Localizing Prompt Injection Attacks
- Authors: Yu-Qi Jia, Yupei Liu, Ze-Dian Shao, Jin-Yuan Jia, N. Gong
- Year: 2025; source: https://www.semanticscholar.org/paper/532f88e78c96a7efb418c6fedd428b741a73e9af
- Local PDF: [2510.12252_promptlocate_localizing_prompt_injection_attacks.pdf](2510.12252_promptlocate_localizing_prompt_injection_attacks.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Localizes injected instructions and data spans; detection is not execution-grounded success.
- Identifiers: {"DBLP": "journals/corr/abs-2510-12252", "ArXiv": "2510.12252", "DOI": "10.1109/SP63933.2026.00105", "CorpusId": 282064646}
- Code referenced by abstract (not necessarily cloned): https://github.com/liu00222/Open-Prompt-Injection.

## 41. Agent Against Agent: An Agentic System for Automatic Prompt Injection Red Teaming
- Authors: Yan-Ting Wang, Chen-Long Yin, Runpeng Geng, Jin-Yuan Jia
- Year: 2026; source: https://www.semanticscholar.org/paper/350028a2fb1b8e1dddb6d1b814dcba2b2dd4e3e0
- Local PDF: [2608.05108_agent_against_agent_an_agentic_system_for_automatic_prompt_injection_red_teaming.pdf](2608.05108_agent_against_agent_an_agentic_system_for_automatic_prompt_injection_red_teaming.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Learned attack-strategy library enables low-query transfer; attack optimization is not selected.
- Identifiers: {"ArXiv": "2608.05108", "CorpusId": 290844763}

## 42. Aligning Provenance with Authorization: A Dual-Graph Defense for LLM Agents
- Authors: Pei-Ran Wang, Ying Li, Yuan Tian
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:288672754
- Local PDF: [2605.26497_aligning_provenance_with_authorization_a_dual_graph_defense_for_llm_agents.pdf](2605.26497_aligning_provenance_with_authorization_a_dual_graph_defense_for_llm_agents.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Compares execution provenance with clean authorization graphs at argument level.
- Identifiers: {"ArXiv": "2605.26497", "DBLP": "journals/corr/abs-2605-26497", "DOI": "10.48550/arXiv.2605.26497", "CorpusId": 288672754}

## 43. AgenTRIM: Tool Risk Mitigation for Agentic AI
- Authors: Roy Betser, Amit Giloni, Shamik Bose, Sindhu Padakandla, Chiara Picardi, Lidor Erez, R. Vainshtein
- Year: 2026; source: https://www.semanticscholar.org/paper/01faaf29f224194719d37bcb522264fdcc07bc24
- Local PDF: [2601.12449_agentrim_tool_risk_mitigation_for_agentic_ai.pdf](2601.12449_agentrim_tool_risk_mitigation_for_agentic_ai.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Balances excessive and insufficient tool privileges; motivates measuring authorized action capability.
- Identifiers: {"DBLP": "journals/corr/abs-2601-12449", "ArXiv": "2601.12449", "DOI": "10.48550/arXiv.2601.12449", "CorpusId": 284909839}

## 44. SPA: Securing Persistent LLM Agents Across Queries with Plan-First Information-Flow Control
- Authors: Dylan Girrens, Guang-Jing Wang
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:291387221
- Local PDF: [2608.27234_spa_securing_persistent_llm_agents_across_queries_with_plan_first_information_flow_control.pdf](2608.27234_spa_securing_persistent_llm_agents_across_queries_with_plan_first_information_flow_control.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Persistent labeled artifacts and planned information flow address cross-query attacks, outside scope.
- Identifiers: {"ArXiv": "2608.27234", "CorpusId": 291387221}

## 45. IterInject: Indirect Prompt Injection Against LLM Agents via Feedback-Guided Iterative Optimization
- Authors: Zi-Xuan Chen, Jiaxiang Chen, Ling-Lun Luo, Ke Xu, Xiaoxia Huang, Tan-Feng Sun, Xing-Hao Jiang
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:288671130
- Local PDF: [2605.24659_iterinject_indirect_prompt_injection_against_llm_agents_via_feedback_guided_iterative_opti.pdf](2605.24659_iterinject_indirect_prompt_injection_against_llm_agents_via_feedback_guided_iterative_opti.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Feedback-driven payload optimization and mechanistic analysis; fixed treatment and held-out confirmation are needed here.
- Identifiers: {"ArXiv": "2605.24659", "DBLP": "journals/corr/abs-2605-24659", "DOI": "10.48550/arXiv.2605.24659", "CorpusId": 288671130}

## 46. Your Agentic LLMs Secretly Encode Indirect Prompt-Injection Exposure in Hidden States
- Authors: Jianshuo Dong, Yiming Liu, Maosen Zhang, Nan Deng, Peng Xu, Xiaoping Zhang, Tian-Wei Zhang, Jie Zhang, Han Qiu
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:290833086
- Local PDF: [2608.02657_your_agentic_llms_secretly_encode_indirect_prompt_injection_exposure_in_hidden_states.pdf](2608.02657_your_agentic_llms_secretly_encode_indirect_prompt_injection_exposure_in_hidden_states.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Hidden states can encode exposure without preventing unsafe actions; exposure and behavioral success differ.
- Identifiers: {"ArXiv": "2608.02657", "CorpusId": 290833086}
- Code referenced by abstract (not necessarily cloned): https://github.com/jianshuod/IPI-exposure-signal.

## 47. AgentWatcher: A Rule-based Prompt Injection Monitor
- Authors: Yan-Ting Wang, Wei Zou, Runpeng Geng, Jinyuan Jia
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:287023515
- Local PDF: [2604.01194_agentwatcher_a_rule_based_prompt_injection_monitor.pdf](2604.01194_agentwatcher_a_rule_based_prompt_injection_monitor.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Causal context attribution plus explicit monitor rules; alternative monitor rather than required resource.
- Identifiers: {"DBLP": "journals/corr/abs-2604-01194", "ArXiv": "2604.01194", "DOI": "10.48550/arXiv.2604.01194", "CorpusId": 287023515}
- Code referenced by abstract (not necessarily cloned): https://github.com/wang-yanting/AgentWatcher.

## 48. SafeAgent: A Runtime Protection Architecture for Agentic Systems
- Authors: Hailin Liu, Eugene Ilyushin, Jie Ni, Minjun Zhu
- Year: 2026; source: https://www.semanticscholar.org/paper/246757c8ad6b30391c40b4df10e9ca89a5bc5c09
- Local PDF: [2604.17562_safeagent_a_runtime_protection_architecture_for_agentic_systems.pdf](2604.17562_safeagent_a_runtime_protection_architecture_for_agentic_systems.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Runtime architecture models evolving trajectory risks; broader than the selected benign intervention.
- Identifiers: {"ArXiv": "2604.17562", "DBLP": "journals/corr/abs-2604-17562", "DOI": "10.48550/arXiv.2604.17562", "CorpusId": 287634921}

## 49. Assessing Automated Prompt Injection Attacks in Agentic Environments
- Authors: David K. Hofer, Edoardo Debenedetti, Florian Tramèr
- Year: 2026; source: https://www.semanticscholar.org/paper/93d58e1c36636c8cd046db68ca3cd6e69fdd4b42
- Local PDF: [2606.10525_assessing_automated_prompt_injection_attacks_in_agentic_environments.pdf](2606.10525_assessing_automated_prompt_injection_attacks_in_agentic_environments.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Compares black-box and gradient attack search with budget-dependent transfer; not a fixed-effect replication.
- Identifiers: {"DBLP": "journals/corr/abs-2606-10525", "ArXiv": "2606.10525", "DOI": "10.48550/arXiv.2606.10525", "CorpusId": 289132834}

## 50. Structurally Close, Temporally Distant: Measuring Security Exposure in Long-Horizon LLM Agents
- Authors: Md Jafrin Hossain, Nur Al Hasan Haldar
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:291832304
- Local PDF: [2609.05911_structurally_close_temporally_distant_measuring_security_exposure_in_long_horizon_llm_agen.pdf](2609.05911_structurally_close_temporally_distant_measuring_security_exposure_in_long_horizon_llm_agen.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Provenance paths can remain short despite long trajectories; structural proximity is not proof of causal effect.
- Identifiers: {"ArXiv": "2609.05911", "CorpusId": 291832304}

## 51. Securing Enterprise Language Model Applications Against Data Leakage and Response Manipulation
- Authors: Kaik Tavares Barroso
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:292585322
- Local PDF: [paper_50_securing_enterprise_language_model_applications_against_data_leakage_a.pdf](paper_50_securing_enterprise_language_model_applications_against_data_leakage_a.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Narrative enterprise-security synthesis, not an original experimental dataset or risk estimate.
- Identifiers: {"DOI": "10.66104/3m1m5x77", "CorpusId": 292585322}

## 52. SIEVE: Selective Integrity Verification and Escalation for Defending LLM Agents against Indirect Prompt Injection
- Authors: Zhibo Liang, Tianze Hu, Zaiye Chen, Mingjie Tang
- Year: 2025; source: https://api.semanticscholar.org/CorpusId:283693648
- Local PDF: [2512.06716_sieve_selective_integrity_verification_and_escalation_for_defending_llm_agents_against_ind.pdf](2512.06716_sieve_selective_integrity_verification_and_escalation_for_defending_llm_agents_against_ind.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Selective structural verification escalates uncertain actions; useful distinction between checks and model behavior.
- Identifiers: {"ArXiv": "2512.06716", "CorpusId": 283693648}

## 53. PIArena: A Platform for Prompt Injection Evaluation
- Authors: Runpeng Geng, Chen-Long Yin, Yan-Ting Wang, Ying Chen, Jin-Yuan Jia
- Year: 2026; source: https://www.semanticscholar.org/paper/480371304f3ff8e861ea2f9f851fa583c45f2c24
- Local PDF: [2604.08499_piarena_a_platform_for_prompt_injection_evaluation.pdf](2604.08499_piarena_a_platform_for_prompt_injection_evaluation.pdf)
- Service relevance: 3/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Unified evaluation platform warns about weak cross-benchmark generalization and aligned injected tasks.
- Identifiers: {"ArXiv": "2604.08499", "DBLP": "conf/acl/GengYWCJ26", "DOI": "10.48550/arXiv.2604.08499", "CorpusId": 287256447}
- Code referenced by abstract (not necessarily cloned): https://github.com/sleeepeer/PIArena.

## 54. Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents
- Authors: Hanrong Zhang, Jingyuan Huang, Kai Mei, Yifei Yao, Zhen-Ting Wang, Chen-Lu Zhan, Hong-Wei Wang, Yongfeng Zhang
- Year: 2024; source: https://www.semanticscholar.org/paper/5f4efbe3aae1d8f44ceab1da257ae685d6beb00b
- Local PDF: [2410.02644_agent_security_bench_asb_formalizing_and_benchmarking_attacks_and_defenses_in_llm_based_ag.pdf](2410.02644_agent_security_bench_asb_formalizing_and_benchmarking_attacks_and_defenses_in_llm_based_ag.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Broad agent-security benchmark spans many surfaces; narrower AgentDojo/InjecAgent resources better fit this hypothesis.
- Identifiers: {"ArXiv": "2410.02644", "DBLP": "conf/iclr/ZhangHMYWZWZ25", "DOI": "10.48550/arXiv.2410.02644", "CorpusId": 273098793}
- Code referenced by abstract (not necessarily cloned): https://github.com/agiresearch/ASB.

## 55. Benchmarking and Defending against Indirect Prompt Injection Attacks on Large Language Models
- Authors: Jing-Wei Yi, Yueqi Xie, Bin Zhu, Keegan Hines, Emre Kıcıman, Guang-Zhong Sun, Xing Xie, Fang-Zhao Wu
- Year: 2023; source: https://www.semanticscholar.org/paper/6d465be006615460d41060f9f5068d51fc1f46b1
- Local PDF: [2312.14197_bipia.pdf](2312.14197_bipia.pdf)
- Service relevance: 2/3; local decision: Design support.
- Method / relevance / limitation: Boundary awareness and reminders motivate the single secondary prompt-defense ablation.
- Identifiers: {"DBLP": "conf/kdd/YiX0KS0W25", "ArXiv": "2312.14197", "DOI": "10.1145/3690624.3709179", "CorpusId": 266521508}
- Code referenced by abstract (not necessarily cloned): https://github.com/microsoft/BIPIA.

## 56. Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition
- Authors: Andy Zou, Maxwell Lin, E. Jones, Micha V. Nowak, Mateusz Dziemian, Nick Winter, Alexander Grattan, Valent Nathanael, Ayla Croft, Xander Davies, Jainee Patel, Robert Kirk, Nate Burnikell, Yarin Gal, Dan Hendrycks, J. Kolter, Matt Fredrikson
- Year: 2025; source: https://www.semanticscholar.org/paper/b13ca9944c6deeae92419b64fcf9d0af431c32b2
- Local PDF: [2507.20526_security_challenges_in_ai_agent_deployment_insights_from_a_large_scale_public_competition.pdf](2507.20526_security_challenges_in_ai_agent_deployment_insights_from_a_large_scale_public_competition.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Public adversarial competition supplies broad failures but not controlled benign paired denominators.
- Identifiers: {"ArXiv": "2507.20526", "DBLP": "journals/corr/abs-2507-20526", "DOI": "10.48550/arXiv.2507.20526", "CorpusId": 280323438}

## 57. NetInjectBench: Benchmarking Indirect Prompt Injection in Tool-Using Large Language Model Agents for Network Operations
- Authors: Ruksat Khan Shayoni, Muhammad Shoaib, S. M. Asif Hossain, M. Mridha
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:290135833
- Local PDF: [2607.10490_netinjectbench_benchmarking_indirect_prompt_injection_in_tool_using_large_language_model_a.pdf](2607.10490_netinjectbench_benchmarking_indirect_prompt_injection_in_tool_using_large_language_model_a.pdf)
- Service relevance: 2/3; local decision: Design support.
- Method / relevance / limitation: Approved-change controls reveal overblocking from static allowlists; strong conceptual utility match.
- Identifiers: {"DBLP": "journals/corr/abs-2607-10490", "ArXiv": "2607.10490", "DOI": "10.48550/arXiv.2607.10490", "CorpusId": 290135833}

## 58. Silent Failures in Agentic Security Evaluation: A Validated Harness for Tool-Call Mediation Under Indirect Prompt Injection
- Authors: Animesh Shaw
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:292436154
- Local PDF: [2609.32691_silent_failures_in_agentic_security_evaluation_a_validated_harness_for_tool_call_mediation.pdf](2609.32691_silent_failures_in_agentic_security_evaluation_a_validated_harness_for_tool_call_mediation.pdf)
- Service relevance: 2/3; local decision: Design support.
- Method / relevance / limitation: Audits payload delivery, exact arguments, capability confounds and trace retention; important instrumentation warning.
- Identifiers: {"ArXiv": "2609.32691", "CorpusId": 292436154}

## 59. The Landscape of Prompt Injection Threats in LLM Agents: From Taxonomy to Analysis
- Authors: Pei Wang, Xin-Feng Li, Chong Xiang, Jing-Huai Zhang, Ying Li, Li-Xia Zhang, Xiao-Feng Wang, Yuan Tian
- Year: 2026; source: https://www.semanticscholar.org/paper/8a410033cc924106c373c57d7032cc8b0756e69a
- Local PDF: [2602.10453_the_landscape_of_prompt_injection_threats_in_llm_agents_from_taxonomy_to_analysis.pdf](2602.10453_the_landscape_of_prompt_injection_threats_in_llm_agents_from_taxonomy_to_analysis.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Context-dependent tasks expose defenses that discard needed runtime evidence.
- Identifiers: {"DBLP": "journals/corr/abs-2602-10453", "ArXiv": "2602.10453", "DOI": "10.48550/arXiv.2602.10453", "CorpusId": 285470089}

## 60. Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation
- Authors: Yu-Chen Ling, Sheng-Cheng Yu, Zhen-Yu Chen, Chun-Rong Fang
- Year: 2026; source: https://www.semanticscholar.org/paper/2a1f56382f4e1e7652f62d2c42c75855ea4f90a0
- Local PDF: [2606.10749_toward_secure_llm_agents_threat_surfaces_attacks_defenses_and_evaluation.pdf](2606.10749_toward_secure_llm_agents_threat_surfaces_attacks_defenses_and_evaluation.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Lifecycle survey covers persistent state and authority; contextual rather than direct experimental support.
- Identifiers: {"ArXiv": "2606.10749", "DBLP": "journals/corr/abs-2606-10749", "DOI": "10.48550/arXiv.2606.10749", "CorpusId": 289131982}

## 61. AgentDrift: A Step-Labeled Benchmark of Injection-Hijacked LLM Agent Trajectories
- Authors: Asif Pinjari, Mithun Paul Saint-Germain
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:291870792
- Local PDF: [2609.06972_agentdrift_a_step_labeled_benchmark_of_injection_hijacked_llm_agent_trajectories.pdf](2609.06972_agentdrift_a_step_labeled_benchmark_of_injection_hijacked_llm_agent_trajectories.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Synthetic step-labeled trajectories include resisted attacks and hard negatives; labels do not substitute for live model outcomes.
- Identifiers: {"ArXiv": "2609.06972", "CorpusId": 291870792}

## 62. An Experimental Evaluation of Multimodal Prompt Injection Attacks on Agentic AI Frameworks
- Authors: V. Nguyen, Mohammad I. Husain
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:291872256
- Local PDF: [2609.09404_an_experimental_evaluation_of_multimodal_prompt_injection_attacks_on_agentic_ai_frameworks.pdf](2609.09404_an_experimental_evaluation_of_multimodal_prompt_injection_attacks_on_agentic_ai_frameworks.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Multimodal carriers separate attempted and completed attacks; outside text-only checkpoint scope.
- Identifiers: {"ArXiv": "2609.09404", "CorpusId": 291872256}

## 63. Security Engineering of OpenClaw: Analyzing Attack Surface Expansion and Trust-Boundary Violations
- Authors: Saeid Jamshidi, Arghavan Moradi Dakhel, Kawser Wazed Nafi, F. Khomh
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:289300811
- Local PDF: [2606.15008_security_engineering_of_openclaw_analyzing_attack_surface_expansion_and_trust_boundary_vio.pdf](2606.15008_security_engineering_of_openclaw_analyzing_attack_surface_expansion_and_trust_boundary_vio.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Multi-agent aggregation changes system-level exposure; not a single-checkpoint paired contrast.
- Identifiers: {"DBLP": "journals/corr/abs-2606-15008", "ArXiv": "2606.15008", "DOI": "10.48550/arXiv.2606.15008", "CorpusId": 289300811}

## 64. TrustTrace: Provenance-Aware Tracing of Indirect Prompt Injection Propagation in LLM-Assisted Learning Workflows
- Authors: Jing-Yi Chen, Rong-Qing Lu
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:291417675
- PDF unavailable: failed; retry: No PDF from alternate/retry source
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Provenance tracing in educational workflows; forensic attribution rather than fictional record editing.
- Identifiers: {"DOI": "10.1109/ACCESS.2026.3726909", "CorpusId": 291417675}

## 65. When Tool Outputs Become Commands: Separating Action Induction from Runtime Authorization in Tool-Augmented LLM Agents
- Authors: Xiao-Kun Guo, Zhen Xu, Dongdong Huo, Yan-Qiu Zhang, Wei Wang, Qin-Fu Yang, Dong-Jin Yu, Yu Wang
- Year: 2026; source: https://www.semanticscholar.org/paper/50dab35ee09285dab775a823906a728048c166ba
- Local PDF: [2608.27146_when_tool_outputs_become_commands_separating_action_induction_from_runtime_authorization_i.pdf](2608.27146_when_tool_outputs_become_commands_separating_action_induction_from_runtime_authorization_i.pdf)
- Service relevance: 2/3; local decision: Design support.
- Method / relevance / limitation: Separates action induction, source provenance and execution authority; close conceptual related work.
- Identifiers: {"ArXiv": "2608.27146", "CorpusId": 291387642}

## 66. WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks
- Authors: Ivan Evtimov, A. Zharmagambetov, Aaron Grattafiori, Chuan Guo, Kamalika Chaudhuri
- Year: 2025; source: https://www.semanticscholar.org/paper/b5fdd8fd5f398c81136fa7dac941f52b9568ad0a
- Local PDF: [2504.18575_wasp_benchmarking_web_agent_security_against_prompt_injection_attacks.pdf](2504.18575_wasp_benchmarking_web_agent_security_against_prompt_injection_attacks.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: End-to-end web evaluation exposes capability-limited attack completion; browser infrastructure is pruned.
- Identifiers: {"DBLP": "conf/nips/EvtimovZGGC25", "ArXiv": "2504.18575", "DOI": "10.48550/arXiv.2504.18575", "CorpusId": 278166059}

## 67. LlamaFirewall: An open source guardrail system for building secure AI agents
- Authors: Sahana Chennabasappa, Cyrus Nikolaidis, D. Song, David Molnar, Stephanie Ding, Sheng-Ye Wan, Spencer Whitman, L. Deason, Nicholas Doucette, Abraham Montilla, Alekhya Gampa, B. de Paola, Dominik Gabi, James Crnkovich, Jean-Christophe Testud, Kat He, Rashnil Chaturvedi, Wu Zhou, Joshua Saxe
- Year: 2025; source: https://www.semanticscholar.org/paper/07734909a75edc13eb838d9f83b52dcc1ea06e64
- Local PDF: [2505.03574_llamafirewall_an_open_source_guardrail_system_for_building_secure_ai_agents.pdf](2505.03574_llamafirewall_an_open_source_guardrail_system_for_building_secure_ai_agents.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Guardrail stack combines classifiers, reasoning audit and code checks; not needed for the primary state outcome.
- Identifiers: {"ArXiv": "2505.03574", "DBLP": "journals/corr/abs-2505-03574", "DOI": "10.48550/arXiv.2505.03574", "CorpusId": 278339401}

## 68. AttriGuard: Defeating Indirect Prompt Injection in LLM Agents via Causal Attribution of Tool Invocations
- Authors: Yu He, Haozhe Zhu, Yi-Ming Li, Shuo Shao, H. Yao, Zhi-Hao Liu, Zhan Qin
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:286462340
- Local PDF: [2603.10749_attriguard_defeating_indirect_prompt_injection_in_llm_agents_via_causal_attribution_of_too.pdf](2603.10749_attriguard_defeating_indirect_prompt_injection_in_llm_agents_via_causal_attribution_of_too.pdf)
- Service relevance: 2/3; local decision: Design support.
- Method / relevance / limitation: Counterfactual tool-action replay tests support from user intent; related causal-attribution work.
- Identifiers: {"ArXiv": "2603.10749", "DBLP": "journals/corr/abs-2603-10749", "DOI": "10.48550/arXiv.2603.10749", "CorpusId": 286462340}

## 69. How Vulnerable Are AI Agents to Indirect Prompt Injections? Insights from a Large-Scale Public Competition
- Authors: Mateusz Dziemian, Maxwell Lin, Xiao-Han Fu, Micha V. Nowak, Nick Winter, E. Jones, Andy Zou, L. Ahmad, Kamalika Chaudhuri, Sahana Chennabasappa, Xander Davies, L. Deason, Benjamin L. Edelman, Tanner Emek, I. Evtimov, Jim Gust, Maia Hamin, Kat He, Klaudia Krawiecka, Riccardo Patana, Neil W. Perry, Troy A. Peterson, Xiangyu Qi, Javier Rando, Zifan Wang, Wang, Spencer Whitman, Eric Winsor, A. Zharmagambetov, Matt Fredrikson, Zico Kolter
- Year: 2026; source: https://www.semanticscholar.org/paper/2bb20a787ff31972a5199ac281bd839aa4602843
- Local PDF: [2603.15714_how_vulnerable_are_ai_agents_to_indirect_prompt_injections_insights_from_a_large_scale_pub.pdf](2603.15714_how_vulnerable_are_ai_agents_to_indirect_prompt_injections_insights_from_a_large_scale_pub.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Large-scale competition emphasizes hidden side effects and transfer; not a matched-control experiment.
- Identifiers: {"DBLP": "journals/corr/abs-2603-15714", "ArXiv": "2603.15714", "DOI": "10.48550/arXiv.2603.15714", "CorpusId": 286579814}

## 70. ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection
- Authors: Shi-Hao Weng, Yang Feng, Jinrui Zhang, Xiao-Fei Xie, Jiongchi Yu, Jia Liu
- Year: 2026; source: https://www.semanticscholar.org/paper/cc7a9701833cf982f6cc28957b604357e53248b8
- Local PDF: [2605.03378_argus_defending_llm_agents_against_context_aware_prompt_injection.pdf](2605.03378_argus_defending_llm_agents_against_context_aware_prompt_injection.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Context-aware attacks require benign causal support for actions; motivates preserving factual evidence in controls.
- Identifiers: {"DBLP": "journals/corr/abs-2605-03378", "ArXiv": "2605.03378", "DOI": "10.48550/arXiv.2605.03378", "CorpusId": 287962873}

## 71. Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents
- Authors: Zihao Wang, Yi-Ming Li, Yu-Tong Wu, Zhe-Yu Liu, Kangjie Chen, Fok Kar Wai, Pin-Yu Chen, V. Thing, Bo Li, Da-Cheng Tao, Tian-Wei Zhang
- Year: 2026; source: https://www.semanticscholar.org/paper/23fbdf41b1981e07d60b1fc9e8b65cbf2237012e
- Local PDF: [2606.13385_who_pays_the_price_stakeholder_centric_prompt_injection_benchmarking_for_real_world_web_ag.pdf](2606.13385_who_pays_the_price_stakeholder_centric_prompt_injection_benchmarking_for_real_world_web_ag.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Stakeholder-specific web-agent harms require outcome and process measures; different deployment scope.
- Identifiers: {"ArXiv": "2606.13385", "DBLP": "journals/corr/abs-2606-13385", "DOI": "10.48550/arXiv.2606.13385", "CorpusId": 289186952}

## 72. LivePI: More Realistic Benchmarking of Agents Against Indirect Prompt Injection
- Authors: Lei Zhao, Abhay Bhaskar, Edgar Dobriban
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:288656389
- Local PDF: [2605.17986_livepi_more_realistic_benchmarking_of_agents_against_indirect_prompt_injection.pdf](2605.17986_livepi_more_realistic_benchmarking_of_agents_against_indirect_prompt_injection.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Live controlled service benchmark; infrastructure exceeds the local fictional-record requirement.
- Identifiers: {"ArXiv": "2605.17986", "DBLP": "journals/corr/abs-2605-17986", "DOI": "10.48550/arXiv.2605.17986", "CorpusId": 288656389}

## 73. StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection
- Authors: Zhuoxin Zhan, Akbar Rafiey, A. Ma, Leila Pishdad, Layla El Asri
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:290978629
- Local PDF: [2608.06477_stepjack_benchmarking_computer_use_agent_safety_against_multi_step_indirect_prompt_injecti.pdf](2608.06477_stepjack_benchmarking_computer_use_agent_safety_against_multi_step_indirect_prompt_injecti.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Multi-step page chains trade attack depth and capability; computer-use setting is excluded.
- Identifiers: {"ArXiv": "2608.06477", "CorpusId": 290978629}
- Code referenced by abstract (not necessarily cloned): https://github.com/BorealisAI/StepJack.

## 74. Balancing Security and Performance in LLM Agents: Spotlight-Guard, a Layered Defense Against Indirect Prompt Injection
- Authors: Doygun Demirol, Murat Aydoğan
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:290933563
- Local PDF: [paper_73_balancing_security_and_performance_in_llm_agents_spotlight_guard_a_lay.pdf](paper_73_balancing_security_and_performance_in_llm_agents_spotlight_guard_a_lay.pdf)
- Service relevance: 2/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Layered spotlighting/detection/authentication study reports security and utility together; not the primary intervention.
- Identifiers: {"DOI": "10.3390/app16157662", "CorpusId": 290933563}

## 75. Prompt Injection Detection for Email Agents Through Attack Chain Modeling
- Authors: A. Hashmi, D. Patel, Yun-Ting Yin
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:292360252
- Local PDF: [2609.30657_prompt_injection_detection_for_email_agents_through_attack_chain_modeling.pdf](2609.30657_prompt_injection_detection_for_email_agents_through_attack_chain_modeling.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Attack-chain detection with benign hard negatives; useful warning about false positives and random splits.
- Identifiers: {"ArXiv": "2609.30657", "CorpusId": 292360252}

## 76. Depth-Dependent Indirect Prompt Injection in Tool-Calling ReAct Agents: Injection Depth, Payload Framing, and Turn-Budget Sensitivity
- Authors: Mohammadreza Rashidi
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:288814278
- Local PDF: [2605.30686_depth_dependent_indirect_prompt_injection_in_tool_calling_react_agents_injection_depth_pay.pdf](2605.30686_depth_dependent_indirect_prompt_injection_in_tool_calling_react_agents_injection_depth_pay.pdf)
- Service relevance: 1/3; local decision: Design support.
- Method / relevance / limitation: Depth and framing can confound ASR through non-encounter; log exposure and fixed insertion position.
- Identifiers: {"ArXiv": "2605.30686", "DBLP": "journals/corr/abs-2605-30686", "DOI": "10.48550/arXiv.2605.30686", "CorpusId": 288814278}

## 77. CoDeL: Co-Evolutionary Defense against Indirect Prompt Injection in LLM-based Agents
- Authors: Xiao Yang, Yang-Chen Ou, Yu-Han Gao, Le Wang, Zong-Hao Ying, Ai-Shan Liu
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:292436383
- Local PDF: [2609.34463_codel_co_evolutionary_defense_against_indirect_prompt_injection_in_llm_based_agents.pdf](2609.34463_codel_co_evolutionary_defense_against_indirect_prompt_injection_in_llm_based_agents.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Co-evolving adversarial training changes the model; training direction pruned.
- Identifiers: {"ArXiv": "2609.34463", "CorpusId": 292436383}

## 78. ASPI: Seeking Ambiguity Clarification Amplifies Prompt Injection Vulnerability in LLM Agents
- Authors: Udari Madhushani Sehwag, Zhengyang Shan, Heming Liu, Dileepa Lakshan, Joseph Brandifino, Max Fenkell
- Year: 2026; source: https://www.semanticscholar.org/paper/83499754304da8eede7d57b4d17a8104520a391d
- Local PDF: [2605.17324_aspi_seeking_ambiguity_clarification_amplifies_prompt_injection_vulnerability_in_llm_agent.pdf](2605.17324_aspi_seeking_ambiguity_clarification_amplifies_prompt_injection_vulnerability_in_llm_agent.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Matched ambiguity/clarification states illustrate channel confounding; our user task remains fully specified.
- Identifiers: {"ArXiv": "2605.17324", "DBLP": "journals/corr/abs-2605-17324", "DOI": "10.48550/arXiv.2605.17324", "CorpusId": 288651364}
- Code referenced by abstract (not necessarily cloned): https://github.com/scaleapi/aspi.

## 79. NOMOS: Compiling Written Policies into Statically Verified Tool-Call Gates for LLM Agents
- Authors: Min-Young Yu, Tony Kim, Janghong Choi
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:292733172
- Local PDF: [2610.11030_nomos_compiling_written_policies_into_statically_verified_tool_call_gates_for_llm_agents.pdf](2610.11030_nomos_compiling_written_policies_into_statically_verified_tool_call_gates_for_llm_agents.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Compiles policies to tool-call gates; illustrates authorized-action blockage and argument-level constraints.
- Identifiers: {"ArXiv": "2610.11030", "DOI": "10.5281/zenodo.22123420", "CorpusId": 292733172}

## 80. IPI-proxy: An Intercepting Proxy for Red-Teaming Web-Browsing AI Agents Against Indirect Prompt Injection
- Authors: Chia-Pei Chen, Kentaroh Toyoda, A. Lai, Alex Leung
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:288256128
- Local PDF: [2605.11868_ipi_proxy_an_intercepting_proxy_for_red_teaming_web_browsing_ai_agents_against_indirect_pr.pdf](2605.11868_ipi_proxy_an_intercepting_proxy_for_red_teaming_web_browsing_ai_agents_against_indirect_pr.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Proxy injects into live web responses; a browser deployment toolkit, not needed for local fixtures.
- Identifiers: {"DBLP": "journals/corr/abs-2605-11868", "ArXiv": "2605.11868", "DOI": "10.48550/arXiv.2605.11868", "CorpusId": 288256128}

## 81. A Trace-Based Assurance Framework for Agentic AI Orchestration: Contracts, Testing, and Governance
- Authors: C. Paduraru, Petru-Liviu Bouruc, Alin Stefanescu
- Year: 2026; source: https://www.semanticscholar.org/paper/e7eee295a7aba7ce0aef3b83a1b964e6bd10169d
- Local PDF: [2603.18096_a_trace_based_assurance_framework_for_agentic_ai_orchestration_contracts_testing_and_gover.pdf](2603.18096_a_trace_based_assurance_framework_for_agentic_ai_orchestration_contracts_testing_and_gover.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Trace contracts support replay and stateful assurance; broad design context.
- Identifiers: {"ArXiv": "2603.18096", "DBLP": "conf/enase/PaduraruBS26", "DOI": "10.5220/0014840300004015", "CorpusId": 286669624}

## 82. Dissecting Adversarial Robustness of Multimodal LM Agents
- Authors: Chen Henry Wu, R. Shah, Jing Yu Koh, R. Salakhutdinov, Daniel Fried, Aditi Raghunathan
- Year: 2024; source: https://www.semanticscholar.org/paper/4f27fc2ea3d3491deded642a5de247d167a03d15
- Local PDF: [2406.12814_dissecting_adversarial_robustness_of_multimodal_lm_agents.pdf](2406.12814_dissecting_adversarial_robustness_of_multimodal_lm_agents.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Multimodal agent decomposition separates component attacks; outside text-only experiment.
- Identifiers: {"DBLP": "conf/iclr/WuSKSFR25", "ArXiv": "2406.12814", "CorpusId": 270562791}
- Code referenced by abstract (not necessarily cloned): https://github.com/ChenWu98/agent-attack

## 83. [Short Paper] Forensic Analysis of Indirect Prompt Injection Attacks on LLM Agents
- Authors: M. Chernyshev, Zubair A. Baig, Robin Doss
- Year: 2024; source: https://www.semanticscholar.org/paper/9aa8ef5683aa8f81d3e0a826c076b45ff0f2d270
- PDF unavailable: no_open_pdf; retry: No PDF from alternate/retry source
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Forensic log analysis using LLMs; full PDF unavailable, screened from service abstract only.
- Identifiers: {"DBLP": "conf/tpsisa/ChernyshevBD24", "DOI": "10.1109/TPS-ISA62245.2024.00053", "CorpusId": 275585584}

## 84. MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers
- Authors: Zhi-Qiang Wang, Yi-Chao Gao, Yan-Ting Wang, Suyuan Liu, Haifeng Sun, Hao-Ran Cheng, Guanquan Shi, Haohua Du, Xiangyang Li
- Year: 2025; source: https://api.semanticscholar.org/CorpusId:280699834
- Local PDF: [2508.14925_mcptox_a_benchmark_for_tool_poisoning_attack_on_real_world_mcp_servers.pdf](2508.14925_mcptox_a_benchmark_for_tool_poisoning_attack_on_real_world_mcp_servers.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Poisons tool metadata at registration; different attack surface from a returned tool result.
- Identifiers: {"ArXiv": "2508.14925", "DBLP": "conf/aaai/WangGWLSCSDL26", "DOI": "10.1609/aaai.v40i42.40895", "CorpusId": 280699834}

## 85. Rethinking Indirect Prompt Injection as a Test-Time Search Problem
- Authors: D. M. Nguyen, Joon Sik Kim, Blazej Manczak, Vaikkunth Mugunthan
- Year: 2026; source: https://www.semanticscholar.org/paper/b0b57629b1ffc5eea81aaac53e83202af7dcc4e6
- Local PDF: [2609.04495_rethinking_indirect_prompt_injection_as_a_test_time_search_problem.pdf](2609.04495_rethinking_indirect_prompt_injection_as_a_test_time_search_problem.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Treats attack generation as budgeted search; motivates prespecifying attack budget and payloads.
- Identifiers: {"ArXiv": "2609.04495", "CorpusId": 291767782}

## 86. pikit: A Composable Toolkit for Indirect Prompt Injection Research and Evaluation
- Authors: Zong-Hao Ying, Xiang-Fan Wu, Bo Yang, Hui-Yu Wu, Xing Zheng, Hua Cheng, Xiao-Rong Shi, Jing Guo
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:292441038
- Local PDF: [2609.36817_pikit_a_composable_toolkit_for_indirect_prompt_injection_research_and_evaluation.pdf](2609.36817_pikit_a_composable_toolkit_for_indirect_prompt_injection_research_and_evaluation.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Composable research toolkit spans many carriers/defenses; existing two repositories suffice for this narrow task.
- Identifiers: {"ArXiv": "2609.36817", "CorpusId": 292441038}
- Code referenced by abstract (not necessarily cloned): https://github.com/Tencent/AI-Infra-Guard/tree/main/Research/pikit.

## 87. Execution-Aware Stage-Wise Evaluation Framework for Indirect Prompt Injection in LLM-Based Email Agents
- Authors: Hyeonjin Jang, EunSeong Lee, Kyungbaek Kim, Misoo Kim
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:291162592
- PDF unavailable: failed; retry: No PDF from alternate/retry source
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Execution-aware email evaluation distinguishes tool calls from delivered outcomes; live email execution not selected.
- Identifiers: {"DBLP": "journals/access/JangLKK26", "DOI": "10.1109/ACCESS.2026.3723800", "CorpusId": 291162592}

## 88. Kill-Chain Canaries: Stage-Level Tracking of Prompt Injection Across Attack Surfaces and Five Production LLMs
- Authors: H. Wang, Ze-Chen Zhang
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:292487415
- Local PDF: [2603.28013_kill_chain_canaries_stage_level_tracking_of_prompt_injection_across_attack_surfaces_and_fi.pdf](2603.28013_kill_chain_canaries_stage_level_tracking_of_prompt_injection_across_attack_surfaces_and_fi.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Stage markers distinguish exposure, propagation and execution; evidence from different surfaces is not interchangeable.
- Identifiers: {"ArXiv": "2603.28013", "CorpusId": 292487415}
- Code referenced by abstract (not necessarily cloned): https://github.com/KevinChunye/prompt_injection

## 89. Security Attack and Defense Strategies for Autonomous Agent Frameworks: A Layered Review with OpenClaw as a Case Study
- Authors: Luyao Xu, Xiang Chen
- Year: 2026; source: https://www.semanticscholar.org/paper/00ac10c09f78b7e6d2a78698107769825daaab6f
- Local PDF: [2604.27464_security_attack_and_defense_strategies_for_autonomous_agent_frameworks_a_layered_review_wi.pdf](2604.27464_security_attack_and_defense_strategies_for_autonomous_agent_frameworks_a_layered_review_wi.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Layered agent-security review; background outside the bounded causal question.
- Identifiers: {"ArXiv": "2604.27464", "DBLP": "journals/corr/abs-2604-27464", "DOI": "10.48550/arXiv.2604.27464", "CorpusId": 287915005}

## 90. Trustworthy Agentic AI: Failure Modes, Mitigation Strategies, and a Lifecycle Framework for Autonomous LLM Systems
- Authors: Fayeq Jeelani Syed, Rehan Ahmad, Ali Al Bataineh, A. Adhikari
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:292220620
- Local PDF: [2609.22712_trustworthy_agentic_ai_failure_modes_mitigation_strategies_and_a_lifecycle_framework_for_a.pdf](2609.22712_trustworthy_agentic_ai_failure_modes_mitigation_strategies_and_a_lifecycle_framework_for_a.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Unvalidated lifecycle framework synthesizes governance; not independent experimental evidence.
- Identifiers: {"ArXiv": "2609.22712", "CorpusId": 292220620}

## 91. AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents
- Authors: Maksym Andriushchenko, Alexandra Souly, Mateusz Dziemian, Derek Duenas, Maxwell Lin, Justin Wang, Dan Hendrycks, Andy Zou, Zico Kolter, Matt Fredrikson, Eric Winsor, Jerome Wynne, Yarin Gal, Xander Davies
- Year: 2024; source: https://www.semanticscholar.org/paper/716c6f6a6e653bebfa676402b887fe2927e06c73
- Local PDF: [2410.09024_agentharm_a_benchmark_for_measuring_harmfulness_of_llm_agents.pdf](2410.09024_agentharm_a_benchmark_for_measuring_harmfulness_of_llm_agents.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Direct harmful-user task benchmark; authorization and harmless indirect injection are different questions.
- Identifiers: {"ArXiv": "2410.09024", "DBLP": "conf/iclr/AndriushchenkoS25", "DOI": "10.48550/arXiv.2410.09024", "CorpusId": 273323256}

## 92. Identifying the Risks of LM Agents with an LM-Emulated Sandbox
- Authors: Yangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris J. Maddison, Tatsunori B. Hashimoto
- Year: 2023; source: https://www.semanticscholar.org/paper/0a893657e00fe8ecfadcc65c63bf293e70cb1564
- Local PDF: [2309.15817_identifying_the_risks_of_lm_agents_with_an_lm_emulated_sandbox.pdf](2309.15817_identifying_the_risks_of_lm_agents_with_an_lm_emulated_sandbox.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: LLM-emulated tools improve scale but simulator/judge contamination motivates deterministic local execution.
- Identifiers: {"DBLP": "conf/iclr/RuanDWPZBDMH24", "ArXiv": "2309.15817", "DOI": "10.48550/arXiv.2309.15817", "CorpusId": 262944419}

## 93. MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection Attacks
- Authors: Georgios Syros, Evan Rose, Brian Grinstead, Christoph Kerschbaumer, William K. Robertson, Cristina Nita-Rotaru, Alina Oprea
- Year: 2026; source: https://www.semanticscholar.org/paper/0ba8da7bad04313c39bb9cb45d946645b22c6872
- Local PDF: [2602.09222_muzzle_adaptive_agentic_red_teaming_of_web_agents_against_indirect_prompt_injection_attack.pdf](2602.09222_muzzle_adaptive_agentic_red_teaming_of_web_agents_against_indirect_prompt_injection_attack.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Adaptive web-agent attack discovery; browser deployment and search are outside selected directions.
- Identifiers: {"DBLP": "journals/corr/abs-2602-09222", "ArXiv": "2602.09222", "DOI": "10.48550/arXiv.2602.09222", "CorpusId": 285463272}

## 94. AgentBreaker: Evaluating Context-Aware Indirect Prompt Injection Risks in Modern Web Agents
- Authors: Yong-Bi Son, Changoo Lee, Dongwon Shin, Byoungyoung Lee, Sanghyun Hong, Sooel Son
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:292524013
- PDF unavailable: failed; retry: No PDF from alternate/retry source
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: DOM-context attacks against web agents; full PDF inaccessible, not selected for implementation.
- Identifiers: {"DOI": "10.1145/3832165", "CorpusId": 292524013}

## 95. Temporal Dynamics of Memory Poisoning in Web3-Style LLM Agents
- Authors: Abbas Yazdinejad, Hadis Karimipour
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:288352752
- PDF unavailable: failed; retry: No PDF from alternate/retry source
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Persistent memory trajectories study delayed activation, beyond the single-return contrast.
- Identifiers: {"DBLP": "journals/access/YazdinejadK26", "DOI": "10.1109/ACCESS.2026.3693560", "CorpusId": 288352752}

## 96. Securing Tool-Using AI Agents Against Injection and Authority Misuse
- Authors: Hasan Kanaker, Hussam N. Fakhouri, Nader Abdel Karim, M. Abuhamdeh, Nurul Halimatul Asmak Ismail, Sandi N. Fakhouri
- Year: 2026; source: https://www.semanticscholar.org/paper/df3245c5642552df6b683939795b92d42be481f2
- Local PDF: [paper_95_securing_tool_using_ai_agents_against_injection_and_authority_misuse.pdf](paper_95_securing_tool_using_ai_agents_against_injection_and_authority_misuse.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Assumption-driven Monte Carlo simulation, not deployed-model incident rates; full abstract recovered from PDF.
- Identifiers: {"DBLP": "journals/computation/KanakerFKAIF26", "DOI": "10.3390/computation14050098", "CorpusId": 290088696}

## 97. Agent libOS: A Runtime Substrate for Capability-Controlled Self-Evolving LLM Agents
- Authors: Yingqi Zhang
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:288904174
- Local PDF: [2606.03895_agent_libos_a_runtime_substrate_for_capability_controlled_self_evolving_llm_agents.pdf](2606.03895_agent_libos_a_runtime_substrate_for_capability_controlled_self_evolving_llm_agents.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Capability-controlled agent runtime separates visibility and authority; infrastructure direction not selected.
- Identifiers: {"ArXiv": "2606.03895", "DBLP": "journals/corr/abs-2606-03895", "DOI": "10.48550/arXiv.2606.03895", "CorpusId": 288904174}

## 98. DriftNet: A Dual-Head Trajectory Transformer for Detecting and Localizing Prompt Injection in LLM Agents
- Authors: Asif Pinjari, Mithun Paul Saint-Germain
- Year: 2026; source: https://www.semanticscholar.org/paper/b3a7674ec672f4d48cb4b8e40c82f509b87b5518
- Local PDF: [2609.10892_driftnet_a_dual_head_trajectory_transformer_for_detecting_and_localizing_prompt_injection_.pdf](2609.10892_driftnet_a_dual_head_trajectory_transformer_for_detecting_and_localizing_prompt_injection_.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Trajectory detector trained on AgentDrift; synthetic regularities and template leakage limit transfer claims.
- Identifiers: {"ArXiv": "2609.10892", "CorpusId": 291902015}

## 99. The LLMbda Calculus: AI Agents, Conversations, and Information Flow
- Authors: Zac Garby, Andrew D. Gordon, David Sands
- Year: 2026; source: https://www.semanticscholar.org/paper/327f2df80cccd89a10934eef495b06af949b0feb
- Local PDF: [2602.20064_the_llmbda_calculus_ai_agents_conversations_and_information_flow.pdf](2602.20064_the_llmbda_calculus_ai_agents_conversations_and_information_flow.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Formal information-flow calculus and verified harness; proof engineering is outside this empirical contrast.
- Identifiers: {"DBLP": "journals/corr/abs-2602-20064", "ArXiv": "2602.20064", "DOI": "10.48550/arXiv.2602.20064", "CorpusId": 285972888}

## 100. Amplify, Don't Create: Temporal Accumulation for Slow-Burn Prompt Injection
- Authors: J. A. Corll
- Year: 2026; source: https://api.semanticscholar.org/CorpusId:289628291
- Local PDF: [2606.20746_amplify_don_t_create_temporal_accumulation_for_slow_burn_prompt_injection.pdf](2606.20746_amplify_don_t_create_temporal_accumulation_for_slow_burn_prompt_injection.pdf)
- Service relevance: 1/3; local decision: Design support.
- Method / relevance / limitation: Matched benign shams and clustered uncertainty already appear in related work; warns against pseudoreplication.
- Identifiers: {"DBLP": "journals/corr/abs-2606-20746", "ArXiv": "2606.20746", "DOI": "10.48550/arXiv.2606.20746", "CorpusId": 289628291}

## 101. Security Architecture for Agentic AI in Enterprise Cloud Environments: A Zero-Trust Framework for Secure Autonomous Systems
- Authors: S. Suryawanshi
- Year: 2026; source: https://www.semanticscholar.org/paper/6aade4a0ce26fae2654ee9bbb04c5bca7164531f
- Local PDF: [paper_security_architecture_for_agentic_ai_in_enterprise_cloud_environments_a_zero_trust_framewo.pdf](paper_security_architecture_for_agentic_ai_in_enterprise_cloud_environments_a_zero_trust_framewo.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Conceptual enterprise zero-trust architecture; coverage scores are not measured attack prevention.
- Identifiers: {"DOI": "10.38124/ijisrt/26aug1168", "CorpusId": 291706293}

## 102. Maris: A Formally Verifiable Privacy Policy Enforcement Paradigm for Multi-Agent Collaboration Systems
- Authors: Jian Cui, Zi-Chuan Li, Chi Wang, Lu-Yi Xing, Xiao-Jing Liao
- Year: 2025; source: https://www.semanticscholar.org/paper/b99bf346a634338688ffe89878505bdc07bfe1c6
- Local PDF: [2505.04799_maris_a_formally_verifiable_privacy_policy_enforcement_paradigm_for_multi_agent_collaborat.pdf](2505.04799_maris_a_formally_verifiable_privacy_policy_enforcement_paradigm_for_multi_agent_collaborat.pdf)
- Service relevance: 1/3; local decision: Context only; outside implementation scope.
- Method / relevance / limitation: Multi-agent message-flow policy enforcement; outside single-agent experimental scope.
- Identifiers: {"ArXiv": "2505.04799", "CorpusId": 278394678}

## Supplemental citation-chased papers

### Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection
- Authors: Greshake, Kai; Abdelnabi, Sahar; Mishra, Shailesh; Endres, Christoph; Holz, Thorsten; Fritz, Mario
- Source: https://arxiv.org/abs/2302.12173
- File: [2302.12173_indirect_prompt_injection.pdf](2302.12173_indirect_prompt_injection.pdf)
- Reading: abstract/opening-section screening; see main review for contribution and limitations.

### Defeating Prompt Injections by Design
- Authors: Debenedetti, Edoardo; Shumailov, Ilia; Fan, Tianqi; Hayes, Jamie; Carlini, Nicholas; Fabian, Daniel; Kern, Christoph; Shi, Chongyang; Terzis, Andreas; Tramèr, Florian
- Source: https://arxiv.org/abs/2503.18813
- File: [2503.18813_camel.pdf](2503.18813_camel.pdf)
- Reading: abstract/opening-section screening; see main review for contribution and limitations.
