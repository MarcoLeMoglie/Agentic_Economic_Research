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
├── main.tex                 # Overleaf entry point; switches Session 1 / 2
├── preamble.tex             # Shared Beamer theme, colours, macros
├── bibliography.bib         # References cited in Session 1
├── syllabus.tex             # One-page English course outline (8-hour hands-on format)
├── assets/                  # Images used by the slide decks
├── recordings/              # Trimmed lecture videos + subtitles (see recordings/README.md)
├── session1/                # Session 1 deck — concepts, tools, architecture
└── session2/                # Session 2 deck — live demos and case studies
```

## File guide

Short description of each major file or folder — what it is, not when it was committed.

### Root

| Path | What it is |
|------|------------|
| `main.tex` | Overleaf stub: sets `\CompileSession` and inputs the chosen session deck. |
| `preamble.tex` | Shared Beamer preamble — fonts, palette, frame templates, custom commands. |
| `bibliography.bib` | BibTeX database for citations in Session 1. |
| `syllabus.tex` | One-page English syllabus for the expanded 8-hour hands-on course. |
| `README.md` | This file — repo map and file descriptions. |
| `.gitattributes` | Git LFS rules for large video files under `recordings/`. |

### `assets/`

| Path | What it is |
|------|------------|
| `banner.png` | Repository header image shown at the top of this README. |
| `real/` | Screenshots of agent interfaces (Codex, Antigravity, NotebookLM, etc.) used in Session 1. |
| `mafia-culture/` | Figures for the Mafia Culture success-story slides in Session 2. |

### `recordings/`

See [`recordings/README.md`](recordings/README.md) for per-file descriptions of videos, VTT captions, and transcripts.

| Path | What it is |
|------|------------|
| `session1/session1_trimmed_softsubs.mp4` | Session 1 lecture video with toggleable English soft subtitles. |
| `session2/session2_trimmed_hardsubs.mp4` | Session 2 lecture video with burned-in English subtitles. |

### `session1/` — concepts and tools (hours 1–2)

| Path | What it is |
|------|------------|
| `session1.tex` | Main Beamer document for Session 1. |
| `session1.pdf` | Compiled Session 1 slide deck. |
| `sections/00_opening.tex` | Title, roadmap, course scope. |
| `sections/01_why_now.tex` | Why agentic AI matters for research now. |
| `sections/02_concepts.tex` | Core vocabulary: agents, context, tokens, tool use. |
| `sections/03_interfaces.tex` | Desktop apps, IDEs, CLIs, browser tools — interface families. |
| `sections/04_cost_privacy.tex` | Pricing, tokens, privacy, institutional constraints. |
| `sections/05_reliability.tex` | Hallucinations, automation bias, verification gates. |
| `sections/06_architecture.tex` | Rules, MCP, memory, skills, hooks, agent loops. |
| `sections/07_case_studies.tex` | Teaser for Session 2 live examples. |
| `sections/08_closing.tex` | Wrap-up, references, GitHub link. |
| `course_abstract_bio_onepage.tex` | One-page course abstract + instructor bio (admin/distribution). |
| `OVERLEAF.md` | Overleaf compile notes for Session 1. |

### `session2/` — live demos and case studies (hours 3–4)

| Path | What it is |
|------|------------|
| `session2.tex` | Main Beamer document for Session 2. |
| `session2.pdf` | Compiled Session 2 slide deck. |
| `BASELINE.md` | Frozen restart point for the Session 2 deck (2026-07-07). |
| `sections/00_opening.tex` | Title and roadmap for the practical session. |
| `sections/03_success_stories.tex` | Live success stories: YouTube, ASSIST, Mafia Culture. |
| `sections/04_brain_and_wip.tex` | Second-brain setup and work-in-progress demo. |
| `sections/05_success_stories_extra.tex` | Additional demos: `/referaggio`, Purge. |
| `OVERLEAF.md` | Overleaf compile notes for Session 2. |

## Session baselines

| Session | Baseline | PDF |
|---------|----------|-----|
| 1 | Git `a7f8590` lineage → `session1/` | [`session1/session1.pdf`](session1/session1.pdf) |
| 2 | **Frozen 2026-07-07** → `session2/BASELINE.md` | [`session2/session2.pdf`](session2/session2.pdf) |

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

## Recordings

| Session | Video | Trim window |
|---------|-------|-------------|
| 1 | [`recordings/session1/session1_trimmed_softsubs.mp4`](recordings/session1/session1_trimmed_softsubs.mp4) | `00:11:20` → `02:19:40` |
| 2 | [`recordings/session2/session2_trimmed_hardsubs.mp4`](recordings/session2/session2_trimmed_hardsubs.mp4) | `00:07:30` → `02:29:23` |

Captions and plain-text transcripts are in the same folders. Details: [`recordings/README.md`](recordings/README.md).

Large `.mp4` files use **Git LFS** — run `git lfs install` before cloning.

## Licence

Third-party screenshots are used under fair use for non-commercial teaching.
Replace with institutional captures or live demos before public distribution if
required by your institution.
