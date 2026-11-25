#!/usr/bin/env bash
# validate.sh — structural, registration, link, and wiki-index validation.
# Usage: bash .infra/scripts/validate.sh
# Exit code: 0 = no errors, 1 = at least one error. Warnings do not fail the run.

set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT" || { echo "cannot enter vault root"; exit 1; }

ERRORS=0
WARNINGS=0
CHECKS=0

section() { printf '\n%s\n' "$1"; }
ok()      { CHECKS=$((CHECKS + 1)); printf '  ok    %s\n' "$1"; }
fail()    { CHECKS=$((CHECKS + 1)); ERRORS=$((ERRORS + 1)); printf '  FAIL  %s\n' "$1"; }
warn()    { CHECKS=$((CHECKS + 1)); WARNINGS=$((WARNINGS + 1)); printf '  WARN  %s\n' "$1"; }

printf 'Second Brain validation\nvault: %s\ndate:  %s\n' "$ROOT" "$(date '+%Y-%m-%d %H:%M')"

# ---------------------------------------------------------------- directories
section '1. Required directories'
for d in \
  general \
  general/agent \
  general/capabilities \
  general/capabilities/skills \
  general/templates \
  areas \
  areas/Research \
  areas/Teaching \
  areas/Personal \
  .agents \
  .agents/skills \
  .infra \
  .infra/scripts
do
  if [ -d "$d" ]; then ok "directory $d"; else fail "missing directory $d"; fi
done

# ---------------------------------------------------------------- global files
section '2. Required global files'
for f in \
  README.md \
  AGENTS.md \
  .gitignore \
  general/INDEX.md \
  general/MEMORY.md \
  general/GLOBAL_DECISIONS.md \
  general/agent/BOOTSTRAP.md \
  general/agent/SESSION_CLOSE.md \
  general/agent/MEMORY_POLICY.md \
  general/agent/WIKI_WORKFLOW.md \
  general/capabilities/skills/research-literature-synthesis/SKILL.md \
  areas/INDEX.md \
  areas/Research/INDEX.md \
  areas/Teaching/INDEX.md \
  areas/Personal/INDEX.md \
  .infra/scripts/validate.sh \
  .infra/scripts/new-project.sh
do
  if [ -f "$f" ]; then ok "file $f"; else fail "missing file $f"; fi
done

if [ -f .agents/skills/research-literature-synthesis/SKILL.md ]; then
  ok 'skill adapter .agents/skills/research-literature-synthesis resolves'
else
  fail 'skill adapter .agents/skills/research-literature-synthesis/SKILL.md missing or broken'
fi

# ---------------------------------------------------------------- templates
section '3. Project templates (11)'
TEMPLATE_COUNT=0
for suffix in \
  INDEX PROJECT_BRIEF CURRENT_STATE NEXT_ACTIONS AGENT_MEMORY DECISIONS \
  TECHNICAL_NOTES SOURCES LOG PROMPTS SESSION_SUMMARIES
do
  f="general/templates/project-slug-$suffix.md"
  if [ -f "$f" ]; then
    TEMPLATE_COUNT=$((TEMPLATE_COUNT + 1))
  else
    fail "missing template $f"
  fi
done
[ "$TEMPLATE_COUNT" -eq 11 ] && ok 'all 11 templates present'

# ---------------------------------------------------------------- projects
section '4. Project folders and core files'
CORE_FILES="INDEX.md PROJECT_BRIEF.md CURRENT_STATE.md NEXT_ACTIONS.md AGENT_MEMORY.md DECISIONS.md TECHNICAL_NOTES.md SOURCES.md LOG.md PROMPTS.md SESSION_SUMMARIES.md"

PROJECT_DIRS=""
for d in areas/*/*; do
  [ -d "$d" ] || continue
  PROJECT_DIRS="$PROJECT_DIRS $d"
done

if [ -z "$PROJECT_DIRS" ]; then
  fail 'no project folders found under areas/<Area>/<slug>/'
else
  for d in $PROJECT_DIRS; do
    slug="$(basename "$d")"
    area="$(basename "$(dirname "$d")")"
    if [ ! -f "$d/INDEX.md" ]; then
      warn "directory $d has no INDEX.md (not counted as a project)"
      continue
    fi
    missing=0
    for f in $CORE_FILES; do
      [ -f "$d/$f" ] || { fail "$d missing core file $f"; missing=1; }
    done
    [ "$missing" -eq 0 ] && ok "project $area/$slug has all 11 core files"

    for page in "$d"/wiki/*.md; do
      [ -e "$page" ] || continue
      name="$(basename "$page")"
      if grep -Fq "wiki/$name" "$d/INDEX.md"; then
        ok "wiki page indexed: $area/$slug/wiki/$name"
      else
        fail "wiki page not linked from project INDEX: $d/wiki/$name"
      fi
    done

    if grep -Fq "$slug" "areas/$area/INDEX.md" 2>/dev/null; then
      ok "area index mentions $slug"
    else
      warn "area index areas/$area/INDEX.md does not mention project $slug"
    fi
  done
fi

# ---------------------------------------------------------------- registry
section '5. MEMORY.md project registry'
REG_LINKS="$(grep -oE '\]\(\.\./areas/[^)]*INDEX\.md\)' general/MEMORY.md | sed -e 's/^](//' -e 's/)$//')"
if [ -z "$REG_LINKS" ]; then
  fail 'general/MEMORY.md contains no project entry links'
else
  for rel in $REG_LINKS; do
    target="general/$rel"
    if [ -f "$target" ]; then
      ok "registry entry resolves: $rel"
      parent="$(dirname "$target")"
      if [ -f "$parent/PROJECT_BRIEF.md" ]; then
        ok "registry entry is a project: $parent"
      else
        fail "registry entry is not a project folder (no PROJECT_BRIEF.md): $parent"
      fi
    else
      fail "registry entry does not resolve: $rel"
    fi
  done
fi

for d in $PROJECT_DIRS; do
  [ -f "$d/INDEX.md" ] || continue
  if grep -Fq "$d/INDEX.md" general/MEMORY.md; then
    ok "project registered in MEMORY.md: $d"
  else
    fail "project missing from MEMORY.md registry: $d"
  fi
done

if [ "$(wc -l < general/MEMORY.md | tr -d ' ')" -gt 140 ]; then
  warn 'general/MEMORY.md is over 140 lines; keep the router compact'
fi

# ---------------------------------------------------------------- links
section '6. Relative Markdown links'
LINK_ERRORS=0
LINK_COUNT=0
while IFS= read -r f; do
  base="$(dirname "$f")"
  links="$(awk '
    /^[[:space:]]*```/ { fence = !fence; next }
    fence { next }
    { print }
  ' "$f" | sed -e 's/`[^`]*`//g' | grep -oE '\]\([^)]*\)' | sed -e 's/^](//' -e 's/)$//')"
  [ -z "$links" ] && continue
  while IFS= read -r link; do
    [ -z "$link" ] && continue
    case "$link" in
      \#*|http://*|https://*|mailto:*|tel:*|\<*) continue ;;
    esac
    case "$link" in
      *'{{'*) continue ;;
    esac
    target="${link%%#*}"
    [ -z "$target" ] && continue
    LINK_COUNT=$((LINK_COUNT + 1))
    case "$target" in
      /*)
        fail "absolute link in $f: $link"
        LINK_ERRORS=$((LINK_ERRORS + 1))
        ;;
      */)
        if [ ! -d "$base/$target" ]; then
          fail "broken directory link in $f: $link"
          LINK_ERRORS=$((LINK_ERRORS + 1))
        fi
        ;;
      *)
        if [ ! -e "$base/$target" ]; then
          fail "broken link in $f: $link"
          LINK_ERRORS=$((LINK_ERRORS + 1))
        fi
        ;;
    esac
  done <<EOF
$links
EOF
done <<EOF
$(find . -name '*.md' -not -path './.git/*' -not -path './general/templates/*' | sort)
EOF
[ "$LINK_ERRORS" -eq 0 ] && ok "$LINK_COUNT relative links resolve"

# ---------------------------------------------------------------- frontmatter
section '7. Frontmatter sanity'
NO_FM=0
while IFS= read -r f; do
  first="$(head -n 1 "$f")"
  if [ "$first" != "---" ]; then
    warn "missing YAML frontmatter: $f"
    NO_FM=$((NO_FM + 1))
  else
    case "$f" in
      */skills/*) key='^name:' ;;
      *)          key='^title:' ;;
    esac
    if ! sed -n '1,12p' "$f" | grep -q "$key"; then
      warn "frontmatter without title/name: $f"
      NO_FM=$((NO_FM + 1))
    fi
  fi
done <<EOF
$(find general areas -name '*.md' -not -path 'general/templates/*' 2>/dev/null | sort)
EOF
[ "$NO_FM" -eq 0 ] && ok 'all vault notes have frontmatter with a title'

# ---------------------------------------------------------------- secrets
section '8. Secret scan'
SECRET_HITS="$(grep -rInE \
  '(AKIA[0-9A-Z]{16}|-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----|sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,})' \
  --include='*.md' --include='*.sh' . 2>/dev/null || true)"
if [ -z "$SECRET_HITS" ]; then
  ok 'no credential-shaped strings found'
else
  printf '%s\n' "$SECRET_HITS"
  warn 'possible credential material found; inspect the lines above'
fi

# ---------------------------------------------------------------- summary
section 'Summary'
printf 'checks: %s   errors: %s   warnings: %s\n' "$CHECKS" "$ERRORS" "$WARNINGS"
if [ "$ERRORS" -eq 0 ]; then
  printf 'RESULT: PASS\n'
  exit 0
else
  printf 'RESULT: FAIL\n'
  exit 1
fi
