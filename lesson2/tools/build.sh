#!/usr/bin/env bash
# Run at the package root (works on macOS with MacTeX, and on Linux TeX Live).
set -euo pipefail
cd "$(dirname "$0")"
command -v pdflatex >/dev/null || { echo 'pdflatex missing; install MacTeX or TeX Live' >&2; exit 1; }
mkdir -p build
for i in 1 2; do
  pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build main.tex >"build/pdflatex-$i.log" 2>&1 || {
    tail -80 "build/pdflatex-$i.log" >&2; exit 1;
  }
done
cp build/main.pdf lesson2-second-brain.pdf
echo 'Compiled lesson2-second-brain.pdf'
