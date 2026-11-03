#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if git rev-parse --show-toplevel >/dev/null 2>&1; then
  echo 'This folder is already inside a git repo. Copy it out (for example to ~/Documents) before running setup_git.sh.' >&2
  exit 1
fi
if test -d .git; then echo 'Git already initialized'; exit 0; fi
git init -b demo-main
git add README.md .gitignore general areas scripts .agents
git -c user.name='Second Brain Teaching Demo' -c user.email='demo@example.invalid' commit -m 'demo: initial synthetic Brain with known maintenance defects'
git tag demo-baseline
echo 'Baseline tagged demo-baseline; repo is local only. No remote configured.'
