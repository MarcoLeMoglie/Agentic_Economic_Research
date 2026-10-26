#!/usr/bin/env bash
# Taste-skill pre-flight, Beamer subset, for lesson1/sections/*.tex.
# Exit 1 on any hard failure.
set -u
cd "$(dirname "$0")/.." || exit 1
fail=0
files=(lesson1/sections/*.tex)

strip() { sed -e 's/%.*$//' "$1"; }

for f in "${files[@]}"; do
  body="$(strip "$f")"
  if printf '%s' "$body" | grep -nE '—|–' >/dev/null; then
    echo "FAIL em/en dash character: $f"; printf '%s\n' "$body" | grep -nE '—|–'; fail=1
  fi
  if printf '%s' "$body" | grep -nE '[^-!<]--[^->]' | grep -vE 'tikz|\\draw|->|<-|--\s*\(|\)\s*--|\{-\}|\[-' >/dev/null; then
    echo "FAIL TeX dash (-- or ---) in text: $f"
    printf '%s\n' "$body" | grep -nE '[^-!<]--[^->]' | grep -vE 'tikz|\\draw|->|<-|--\s*\(|\)\s*--|\{-\}|\[-'; fail=1
  fi
  if printf '%s' "$body" | grep -nE '(Part|Case|Step|Stage|Phase|Term) [0-9]+' >/dev/null; then
    echo "FAIL numbered label: $f"; printf '%s\n' "$body" | grep -nE '(Part|Case|Step|Stage|Phase|Term) [0-9]+'; fail=1
  fi
  if printf '%s' "$body" | grep -nE 'soft(blue|orange|green|purple)|\\bigpoint|\\midpoint' >/dev/null; then
    echo "FAIL legacy pastel or shout macro: $f"; fail=1
  fi
  if printf '%s' "$body" | grep -niE 'seamless|unleash|revolutioni[sz]e|elevate|next-gen|game.?changer' >/dev/null; then
    echo "FAIL filler verb: $f"; fail=1
  fi
done

echo "frames per file:"
for f in "${files[@]}"; do printf '  %-48s %s\n' "$f" "$(grep -c 'begin{frame}' "$f")"; done
[ $fail -eq 0 ] && echo "PRE-FLIGHT OK" || echo "PRE-FLIGHT FAILED"
exit $fail
