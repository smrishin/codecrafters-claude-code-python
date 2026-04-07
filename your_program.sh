#!/bin/sh
set -e # Exit early if any commands fail

SCRIPT_DIR="$(dirname "$0")"
PYTHONSAFEPATH=1 PYTHONPATH="$SCRIPT_DIR" exec python -m app.main "$@"
