# Lesson 1 demos

Material for the live demos in Lesson 1 of *Agentic AI for Economic Research*.
The folder is part of the course repo:

https://github.com/MarcoLeMoglie/Agentic_Economic_Research/tree/main/demos/lesson1

`code/analysis.do` contains a deliberate bug. Do not fix it before the lesson.

| Demo | What we do | What to watch |
|------|------------|---------------|
| Chat vs agent | Paste the do-file into a chat window and ask for the bug. Then give the same request to an agent in this folder. | The chat guesses. The agent runs Stata, reads `analysis.log`, edits, reruns. |
| Context and compaction | Long session, then `/compact`. | The context meter before and after, and what the summary keeps. |
| MCP and skills | Ask for "a regression table" with the skill in `.agents/skills/` available. | The agent loads `SKILL.md` only when the request matches. |
| Cruscotto Italia | In the OpenCode app, connect `https://cruscotto-italia-mcp.agid.workers.dev/mcp`. Ask for one comune, a small dataset and two charts. | The numbers come from the server. No key. |
| Model swap | Same task in OpenCode, first with one model, then with another via `-m`. | Same harness, same tools, different model: speed, cost, result. |

## Requirements

Stata 17 or later with `esttab` (`ssc install estout`). One of: ChatGPT desktop with Codex, Claude Code, Cursor, OpenCode.
