#!/usr/bin/env bash
# Return the lecture demo to the pre-audit tag. Refuses any other folder.
set -euo pipefail
DEST="${DEMO_DEST:-${HOME}/Documents/SecondBrain-Lecture-Demo}"
if [[ ! -f "$DEST/.demo-brain" ]]; then
  echo "No .demo-brain marker in ${DEST}. Refusing." >&2
  exit 1
fi
if [[ "$(basename "$DEST")" != "SecondBrain-Lecture-Demo" ]]; then
  echo "Folder name is not SecondBrain-Lecture-Demo. Refusing." >&2
  exit 1
fi
cd "$DEST"
git checkout main
git reset --hard pre-audit
git clean -fd
echo "Reset to pre-audit. Branch final-verified is unchanged."
git status -sb
git log --oneline -6
