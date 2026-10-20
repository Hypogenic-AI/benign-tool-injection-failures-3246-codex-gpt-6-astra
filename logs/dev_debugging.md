# Development debugging

First Qwen development invocation failed before requests: Inspect passed base_url twice. Removed redundant model_args.base_url and used LOCAL_BASE_URL. No subject episode collected and no payload/analysis changes.

Before main collection, redirected Inspect internal cache/data paths into workspace .cache using XDG_DATA_HOME/XDG_CACHE_HOME. The first debug trace file in the default user data directory was empty.

Qwen development retry completed six real episodes with correct state and valid action parsing; exact sampling parameters were confirmed in the Inspect model events. Main collection began after hash/replay verification. Inspect warned its optional control-surface Unix socket path was too long; evaluation continues without that optional UI service.

DeepSeek quoted-condition progress reported a cumulative HTTP-retry counter of 3 despite max_retries=0 in the Inspect generation config. The task and all completed episode traces have no infrastructure-failure flag. No explicit retry/error events appeared in the quoted Inspect log; throughput-counter evidence is saved in results/transport_retry_trace_records.json. Treat exact per-request retry attribution as unresolved; no manual outcome-driven episode reruns were performed.
