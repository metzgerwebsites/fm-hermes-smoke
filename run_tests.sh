#!/usr/bin/env bash
# Run the fm-hermes-smoke unittest suite.
#
# Usage: ./run_tests.sh [extra unittest args...]
# Stdlib only. No third-party dependencies and no installation step required.
set -euo pipefail

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$repo_root"

# Discovery inserts tests/ on sys.path, so export the repo root to make the
# fm_hermes_smoke package importable without installing it.
export PYTHONPATH="$repo_root${PYTHONPATH:+:$PYTHONPATH}"

exec python3 -m unittest discover -s tests -v "$@"