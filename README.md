![Agentic AI for Economic Research](assets/banner.png)

# Agentic AI for Economic Research

**Instructor:** Marco Le Moglie, Catholic University of the Sacred Heart

I teach this to PhD students and faculty in economics. Four lessons of two hours, eight hours in total, in English, on a video call.

A paper is still the same job: read, get the data in shape, estimate, write, answer the referee. An agent can take a piece of that job inside the project folder. It opens the files, runs Stata, and changes the line that failed. The course is how you point it at the right files, what you let it change, and how you check the result.

**Lesson 1. Vocabulary.** What the pieces are, and what you do with them. The model writes the next text. The harness runs the session, calls the tools, and stops for permission. You learn what a run costs, which data can leave the machine, and how you tell a bad output. You leave able to point an agent at the project folder and say what it may change.

**Lesson 2. Second brain.** A brain is this project written in files the next session can open: where the work stands, which decisions were taken, and why. You use it so the agent acts on that memory instead of starting from the chat. The lesson shows what belongs in it, what you ask it to do, and the brain behind this research.

**Lesson 3. Automations and control.** An automation is a job that starts when you are not in the session, on a schedule, an event, or a condition, and only within the changes you allowed. Control is the check before a result stays: the source next to the value, the diff, and a second pass. A methodological choice stays only when you can explain it.

**Lesson 4. Your project.** You bring an agent you tried on your own paper. It need not be finished. Show what you built, what failed, and how you checked it. Each person has 10–15 minutes. There is no slide deck for this lesson. 

## Slides

| Lesson | PDF |
|--------|-----|
| 1. Vocabulary | [`lesson1/lesson1.pdf`](lesson1/lesson1.pdf) |
| 2. Second brain | [`lesson2/lesson2.pdf`](lesson2/lesson2.pdf) |
| 3. Automations and control | [`lesson3/lesson3.pdf`](lesson3/lesson3.pdf) |
| 4. Your project | No slides. You present the agent you tried on your own paper. |

One-page outline: [`syllabus.pdf`](syllabus.pdf).

The slides, the syllabus, and the demo files in this repository were built with AI agents.

## Class files

### `demos/lesson1/`

Live material for Lesson 1. The slides point here:

https://github.com/MarcoLeMoglie/Agentic_Economic_Research/tree/main/demos/lesson1

| Path | What it is |
|------|------------|
| `README.md` | What each demo does, and what to have installed. |
| `AGENTS.md` | Rules file the agent reads at the start of a session. |
| `code/analysis.do` | Stata do-file with a deliberate bug (`ln(prise)`). Do not fix it before class. |
| `data/auto.dta` | Stata's `auto` dataset, the input to that do-file. |
| `.agents/skills/regression-table/SKILL.md` | Skill the agent should load when asked for a regression table. |
| `output/` | Where the agent writes the table. Empty in the repo. |

### `demos/lesson2/`

The vault from the end of Lesson 2. Open this folder on its own:

https://github.com/MarcoLeMoglie/Agentic_Economic_Research/tree/main/demos/lesson2

| Path | What it is |
|------|------------|
| `README.md` | How to open the vault, and the two commands. |
| `AGENTS.md` | The contract the agent reads first. |
| `general/` | Shared index, protocols, the eleven templates, and the skill. |
| `areas/Research/public-transport-employment/` | The synthetic project a new session reopens. |

## Licence

Third-party material in the slides is used under fair use for non-commercial teaching.
