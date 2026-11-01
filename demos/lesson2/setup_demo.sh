#!/usr/bin/env bash
# Build ~/Documents/SecondBrain-Lecture-Demo from seed, with a short git history.
# Refuses to overwrite an existing folder. No remote, no push.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
DEST="${DEMO_DEST:-${HOME}/Documents/SecondBrain-Lecture-Demo}"
if [[ -e "$DEST" ]]; then
  echo "Refusing to overwrite ${DEST}" >&2
  echo "Run reset_demo.sh, or remove the folder yourself." >&2
  exit 1
fi
python3 "$ROOT/build_seed.py"
mkdir -p "$(dirname "$DEST")"
cp -R "$ROOT/seed" "$DEST"
chmod +x "$DEST"/areas/Research/transit-jobs/skills/check-synthetic-panel/scripts/check_panel.py \
  "$DEST"/scripts/*.py \
  "$DEST"/areas/Research/transit-jobs/code/*.py || true

cd "$DEST"
git init -b main
# Dates are synthetic. Identity comes from the machine's existing git config.

commit_tree() {
  local when="$1" msg="$2"
  git add -A
  GIT_AUTHOR_DATE="$when" GIT_COMMITTER_DATE="$when" git commit -m "$msg"
}

PROJ="areas/Research/transit-jobs"
FINAL="$(mktemp -d)"
cp -R "$PROJ" "$FINAL/transit-jobs"

# Commit 1: vault without the project body.
rm -rf "$PROJ"
commit_tree "2026-09-01T09:00:00+0100" "init: lecture vault, routing files, and skills"

# Commit 2: project text only, first decision, correct link, no data or wiki.
mkdir -p "$PROJ"
cp "$FINAL/transit-jobs/"*.md "$PROJ/"
rm -rf "$PROJ/wiki" "$PROJ/raw" "$PROJ/data" "$PROJ/code" "$PROJ/skills"
mkdir -p "$PROJ/skills" "$PROJ/data" "$PROJ/code"
python3 - <<PY
from pathlib import Path
p = Path("$PROJ/transit-jobs_DECISIONS.md")
head, _, _ = p.read_text().partition("## 2026-09-14")
p.write_text(head.rstrip() + "\n")
s = Path("$PROJ/transit-jobs_CURRENT_STATE.md")
text = s.read_text().replace("[[transit-jobs_DECISION]]", "[[transit-jobs_DECISIONS]]")
text = text.replace("Last updated: 2026-10-30.", "Last updated: 2026-09-02.")
s.write_text(text)
Path("$PROJ/transit-jobs_LOG.md").write_text("# Log\n\n## 2026-09-02\n- First clustering note: tract.\n")
PY
commit_tree "2026-09-02T11:00:00+0100" "decision: cluster standard errors by tract"

# Commit 3: district decision. September note stays unmarked.
cp "$FINAL/transit-jobs/transit-jobs_DECISIONS.md" "$PROJ/transit-jobs_DECISIONS.md"
commit_tree "2026-09-14T11:00:00+0100" "decision: cluster by district; September note left unmarked"

# Commit 4: synthetic panel and code. Link still correct.
mkdir -p "$PROJ/data" "$PROJ/code"
cp "$FINAL/transit-jobs/data/synthetic_panel.csv" "$PROJ/data/"
cp "$FINAL/transit-jobs/code/"*.py "$PROJ/code/"
commit_tree "2026-10-01T11:00:00+0100" "data: synthetic panel, seed 2026, and lecture code"

# Commit 5: wiki and canvas, including the page that is not in the index.
cp -R "$FINAL/transit-jobs/wiki" "$PROJ/wiki"
cp "$FINAL/transit-jobs/paper-map.canvas" "$PROJ/paper-map.canvas"
rm -rf "$PROJ/skills"
mkdir -p "$PROJ/skills"
cp -R "$FINAL/transit-jobs/skills/." "$PROJ/skills/"
commit_tree "2026-10-15T11:00:00+0100" "wiki: staggered design notes; one page left off the index"

# Commit 6: broken wikilink and the undistilled call.
cp "$FINAL/transit-jobs/transit-jobs_CURRENT_STATE.md" "$PROJ/transit-jobs_CURRENT_STATE.md"
mkdir -p "$PROJ/raw/chats"
cp -R "$FINAL/transit-jobs/raw/." "$PROJ/raw/"
cp "$FINAL/transit-jobs/transit-jobs_LOG.md" "$PROJ/transit-jobs_LOG.md"
cp "$FINAL/transit-jobs/transit-jobs_NEXT_ACTIONS.md" "$PROJ/transit-jobs_NEXT_ACTIONS.md"
commit_tree "2026-10-28T16:00:00+0100" "note: coauthor call filed under raw; state link typo left in"

rm -rf "$FINAL"
git tag pre-audit

git checkout -b final-verified
python3 scripts/lint_demo_brain.py --apply 1,2,3 --distill 5
python3 scripts/validate_demo_brain.py
git add -A
GIT_AUTHOR_DATE="2026-10-31T18:00:00+0100" GIT_COMMITTER_DATE="2026-10-31T18:00:00+0100" \
  git commit -m "audit: index wiki page, fix link, mark superseded decision"
git checkout main

echo "Demo vault: ${DEST}"
echo "HEAD $(git rev-parse --short HEAD)  tag pre-audit  branch final-verified"
echo "No remote. Do not push."
