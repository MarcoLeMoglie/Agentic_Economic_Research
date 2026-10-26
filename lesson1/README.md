# Lesson 1: The vocabulary of agentic AI (8-hour course)

Entry point: `lesson1/lesson1.tex` (or `main.tex` with `\CompileSession{3}`).
Theme: `lesson1/preamble_v2.tex`. Sources for every figure and number:
`assets/lesson1/SOURCES.md`. Chart data: `assets/lesson1/charts/data/*.csv`.

## Design read

Redesign of a lecture deck for economics PhD students and faculty, watched over
a screen share, with a calm academic language, leaning toward a custom Beamer
theme: one ink colour (`#163A59`), one accent (`#D97706`), real screenshots and
data charts as the only visuals. Mode: preserve brand, overhaul layout.
Dials: variance 5, motion 1, density 4.

## Layout-family map

Families: D definition, S screenshot-led, C chart-led, T sparse table or grouped
columns, G diagram, F single statement or demo cue. Rule: never three frames of
the same family in a row, never more than two text/image splits in a row.

| # | Frame | Family |
|---|-------|--------|
| 1 | Title | title |
| 2 | The course in four lessons | G |
| 3 | Twelve words for today | T |
| - | Divider: From chat to agent | divider |
| 4 | Model + harness = agent | D |
| 5 | Chatbot vs agent | T |
| 6 | The loop, in a real trace | S |
| 7 | 2022-2026: from chat window to command center | G |
| 8 | How long a task can an agent finish? | S |
| - | Demo 1: chat vs agent | F |
| - | Demo 1 recorded result | S |
| - | Divider: Core vocabulary | divider |
| 9 | Prompt vs task | D |
| 10 | Context window and tokens | C |
| 11 | Compaction | G |
| 12 | Rules files | S |
| 13 | Tools, permissions, sandbox | G |
| 14 | MCP | D |
| 15 | Skills | S |
| 16 | Sub-agents and hooks | T |
| 17 | Memory has layers | G |
| - | Demo 2 and 3: context, MCP, skills | F |
| - | Demo 3 recorded result | S |
| - | Divider: Harnesses in 2026 | divider |
| 18 | Five surfaces, one idea | G |
| 19 | Chat became agent | S |
| 20 | One harness, many surfaces: Codex | G |
| 21 | CLI and open harnesses | S |
| 22 | IDE agents | S |
| 23 | Start from the task | T |
| - | Divider: Models and benchmarks | divider |
| 24 | Who builds frontier models | T |
| 25 | One independent index | C |
| 26 | How to read a benchmark | G |
| 27 | Intelligence per dollar | C |
| 28 | What people actually use | C |
| 29 | Open weights, open source, local | D |
| - | Demo 4: same harness, other model | F |
| - | Divider: Cost, data, reliability | divider |
| 30 | Subscription vs API | T |
| 31 | What a cost spike looks like | T |
| 32 | What data is risky | G |
| 33 | Reliability words | T |
| 34 | Twelve words, one line each | T |
| 35 | Before Lesson 2 | F |
| 36 | References | refs |

## Pre-flight (taste skill, Beamer subset)

Run `lesson1/preflight.sh` before each commit. It fails on em or en dashes and
on numbered section labels in visible text, and lists frames per family.
