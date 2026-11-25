#!/usr/bin/env bash
# new-project.sh — scaffold a project from the 11 global templates.
# Usage: bash .infra/scripts/new-project.sh <Area> <slug> "<Title>"
# Example: bash .infra/scripts/new-project.sh Research my-new-project "My New Project"
#
# This script is intentionally conservative: it refuses to overwrite, and it does
# not edit MEMORY.md or the area index. Registration stays a deliberate act.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

if [ "$#" -ne 3 ]; then
  echo "usage: bash .infra/scripts/new-project.sh <Area> <slug> \"<Title>\"" >&2
  exit 2
fi

AREA="$1"
SLUG="$2"
TITLE="$3"
DATE="$(date '+%Y-%m-%d')"

if [ ! -d "areas/$AREA" ]; then
  echo "error: area 'areas/$AREA' does not exist. Choose Research, Teaching, Personal, or create the area index first." >&2
  exit 1
fi

case "$SLUG" in
  *[!a-z0-9-]*|'')
    echo "error: slug must be lowercase kebab-case (a-z, 0-9, hyphens)." >&2
    exit 1
    ;;
esac

case "$SLUG" in
  -*|*-|*--*)
    echo "error: slug must not start/end with a hyphen or contain '--'." >&2
    exit 1
    ;;
esac

if [ -z "$TITLE" ]; then
  echo "error: title must not be empty." >&2
  exit 1
fi

DEST="areas/$AREA/$SLUG"
if [ -e "$DEST" ]; then
  echo "error: '$DEST' already exists. Refusing to overwrite." >&2
  exit 1
fi

mkdir -p "$DEST/raw"

for tpl in general/templates/project-slug-*.md; do
  name="$(basename "$tpl")"
  out="${name#project-slug-}"
  cp "$tpl" "$DEST/$out"
done

TITLE="$TITLE" SLUG="$SLUG" AREA="$AREA" DATE="$DATE" \
  perl -pi -e 's/\{\{title\}\}/$ENV{TITLE}/g; s/\{\{slug\}\}/$ENV{SLUG}/g; s/\{\{area\}\}/$ENV{AREA}/g; s/\{\{date\}\}/$ENV{DATE}/g' \
  "$DEST"/*.md

cat > "$DEST/raw/README.md" <<EOF
# raw/ — Original Sources

Original documents for **$TITLE**. Read-only: never edit, reformat, or "clean" a capture.

## Rules

1. Name captures \`YYYY-MM-DD-short-slug.ext\`.
2. Add a provenance header (type, author, date, acquired, locator, synthetic yes/no).
3. Register every file in [SOURCES.md](../SOURCES.md) with an ID (\`S-xxx\`).
4. Mark fictional or illustrative material **SYNTHETIC** on its first line.
5. Do not store secrets, sensitive credentials, or unnecessary personal data.

## Current contents

_None yet._
EOF

echo "Created $DEST"
echo
echo "Next steps (manual, deliberate):"
echo "  1. Add a row to general/MEMORY.md with the link ../$DEST/INDEX.md"
echo "  2. Add a row to areas/$AREA/INDEX.md"
echo "  3. Fill in PROJECT_BRIEF.md, then set 2-3 actions in NEXT_ACTIONS.md"
echo "  4. Run: bash .infra/scripts/validate.sh"
