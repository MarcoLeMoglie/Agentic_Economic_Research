# Agentic AI for Economic Research

Beamer slide deck for the four-hour mini-course **Agentic AI for Economic
Research** taught by Marco Le Moglie (Catholic University of the Sacred Heart).
This deck covers hours 1-2 (concepts, vocabulary, interfaces, governance,
architecture). Hours 3-4 (applied case studies from Marco's own research) live
in a separate, forthcoming deck.

## Build

LaTeX source compiles on Overleaf with **pdflatex**. Locally:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Layout

```
main.tex            entry point (\input each section)
preamble.tex        custom Beamer theme (deep blue + accent orange)
bibliography.bib    every cited source
sections/           one file per block (00..08)
assets/
  real/             real-world screenshots and product captures
  charts/           data-backed charts produced for the deck
  icons/            icon set used in the theme
  legacy/           reference materials (v1 deck PDF, v1 sources, legacy PNGs)
```

## Workflow

- Block-by-block writing with intermediate verification by Marco.
- Quality gates per block: `tools/prose-check` (Slopless + Vale) and the
  `bugbot` subagent.
- One `feat(block-N): ...` commit per block, pushed to `main`.
- Release with `git tag v1.0`.

## Brain integrations

Project notes and decisions live in the Marco Brain vault at
`02_AREAS/Teaching/AI_course/`. Memory layer: `memanto`, `hivemind`, `cavemem`.

## Licence

All third-party screenshots are used under fair use for non-commercial
teaching. Replace with institutional captures or live demos if needed.
