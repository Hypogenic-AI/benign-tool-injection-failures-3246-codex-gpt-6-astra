# Development debugging

First Qwen development invocation failed before requests: Inspect passed base_url twice. Removed redundant model_args.base_url and used LOCAL_BASE_URL. No subject episode collected and no payload/analysis changes.

Before main collection, redirected Inspect internal cache/data paths into workspace .cache using XDG_DATA_HOME/XDG_CACHE_HOME. The first debug trace file in the default user data directory was empty.
