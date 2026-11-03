#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if ! test -d .git; then echo 'Run scripts/setup_git.sh first' >&2; exit 1; fi
printf '%s\n' 'WARNING: reset will discard all UNCOMMITTED CHANGES in this synthetic demo vault only.'
read -r -p 'Type RESET-DEMO to continue: ' confirm
if test "$confirm" != RESET-DEMO; then exit 1; fi
git reset --hard demo-baseline
rm -f outputs/dataset-audit.md
printf '%s\n' 'Restored synthetic baseline. Never run this against the real Brain.'
