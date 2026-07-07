![Agentic AI for Economic Research](assets/banner.png)

# Agentic AI for Economic Research

**Four-hour mini-course** for PhD students and faculty in economics.

**Instructor:** Marco Le Moglie · Catholic University of the Sacred Heart

## Overleaf

Overleaf compiles **`main.tex`** at repo root by default. Set the session on line 11 (single line — change the number only):

```latex
\newcommand{\CompileSession}{2}  % 1 = Session 1 | 2 = Session 2
```

**Recompile** → `main.pdf`

| Method | Main document | PDF output |
|--------|---------------|------------|
| Default (switch in `main.tex`) | `main.tex` | `main.pdf` |
| Session 1 direct | `session1/session1.tex` | `session1/session1.pdf` |
| Session 2 direct | `session2/session2.tex` | `session2/session2.pdf` |

`main.tex` is a thin Overleaf stub; all slide content lives under `session1/` and `session2/`.

## Repository layout

```
Agentic_Economic_Research/
├── main.tex                 # Overleaf stub (session switch)
├── preamble.tex             # shared Beamer theme
├── bibliography.bib
├── assets/
│   ├── banner.png
│   ├── real/                # interface screenshots (Session 1)
│   └── mafia-culture/       # Session 2 success-story assets
├── recordings/session1/     # lecture video (unchanged across deck commits)
├── session1/
│   ├── session1.tex
│   ├── sections/00–08
│   ├── session1.pdf         # compiled Session 1 deck
│   └── OVERLEAF.md
└── session2/
    ├── session2.tex
    ├── BASELINE.md          # frozen restart point (2026-07-07)
    ├── sections/
    ├── reports/             # mafia-culture PDFs for slide hyperlinks
    ├── session2.pdf         # compiled Session 2 deck
    └── OVERLEAF.md
```

## Session baselines

| Session | Baseline | PDF |
|---------|----------|-----|
| 1 | Git `a7f8590` lineage → `session1/` | [`session1/session1.pdf`](session1/session1.pdf) |
| 2 | **Frozen 2026-07-07** → `session2/BASELINE.md` | [`session2/session2.pdf`](session2/session2.pdf) |

Session 2 slides: Marco edits are canonical. Agents must not rewrite `.tex` files without explicit instruction.

## Local build

```bash
# Session 1 (+ bib)
pdflatex -output-directory=session1 session1/session1.tex
bibtex session1/session1
pdflatex -output-directory=session1 session1/session1.tex
pdflatex -output-directory=session1 session1/session1.tex

# Session 2
pdflatex -output-directory=session2 session2/session2.tex
```

Docker: `texlive/texlive:latest` if local TeX is too old.

## Recording (Session 1)

[`recordings/session1/session1_trimmed_softsubs.mp4`](recordings/session1/session1_trimmed_softsubs.mp4) — not modified by slide/deck commits.
