#!/usr/bin/env bash
set -euo pipefail
pwd
test -d .git
.venv/bin/python scripts/prepare_datasets.py
.venv/bin/python scripts/prepare_models.py
.venv/bin/python scripts/build_pilot.py
.venv/bin/python scripts/validate_resources.py
