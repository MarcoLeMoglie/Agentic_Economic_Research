#!/usr/bin/env bash
# Optional: replace bundled illustrative fallback assets with screenshots
# already present in the user's existing Agentic_Economic_Research course.
# This script writes ONLY into the extracted Lesson-2 package.
set -euo pipefail
cd "$(dirname "$0")"
SRC="${1:-$HOME/Library/CloudStorage/Dropbox/Applicazioni/Overleaf/Agentic_Economic_Research/assets/lesson2/screens}"
DEST="assets/screens"
if [[ ! -d "$SRC" ]]; then
  echo "Screenshot folder unavailable: $SRC" >&2
  echo 'Bundled illustrated fallback images remain available; build.sh will still work.' >&2
  exit 1
fi
mkdir -p "$DEST"
count=0
for file in obsidian-interface.png obsidian-file-explorer.png obsidian-graph-view.png obsidian-canvas.png obsidian-git-history.png obsidian-git-diff.png; do
  if [[ -f "$SRC/$file" ]]; then
    cp "$SRC/$file" "$DEST/$file"
    printf 'Imported %s\n' "$file"
    count=$((count+1))
  else
    printf 'Not found (fallback kept): %s\n' "$file"
  fi
done
printf 'Imported %s screenshot(s). Run ./build.sh to recompile.\n' "$count"
