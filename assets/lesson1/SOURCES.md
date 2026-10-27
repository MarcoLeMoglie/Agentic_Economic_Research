# Lesson 1: sources for every number, chart and screenshot

All pages accessed on 26 Oct 2026 unless noted. Re-check the starred items the
day before teaching: they move weekly.

## Charts

| File | Slide | Source | Notes |
|------|-------|--------|-------|
| `charts/data/aa_index_2026-10.csv` * | One independent index | Artificial Analysis, LLM Leaderboard, Intelligence Index v4.3.2, https://artificialanalysis.ai/leaderboards/models | Best setting per model. "open" = weights downloadable today. Kimi K3.1 Pro is labelled closed: Moonshot promises weights by 4 Nov 2026, none public yet (https://www.kimi.ai/blog/kimi-k3-1-pro). gpt-oss-120b kept as a US open-weight reference. |
| `charts/data/price_vs_index.csv` * | Intelligence per dollar | Same page, column "Cost per Task USD" | Cost to run the index tasks once, not list price per token. Log x-axis. |
| `charts/data/openrouter_share_2026-10-19.csv` * | What people actually use | OpenRouter Rankings, Market Share, week beginning 19 Oct 2026, https://openrouter.ai/rankings | Share of text requests, not users or spend. Data CC BY 4.0, attribution "OpenRouter". |
| `charts/data/context_windows.csv` | Context window and tokens | Vendor model pages: OpenAI GPT-6.1 Sol (1,050,000) https://developers.openai.com/api/docs/models/gpt-6.1-sol; xAI Grok 4.7 (500,000) https://docs.x.ai/developers/grok-4-7; AA leaderboard context column for Opus 5.5, Gemini 4 Argon, DeepSeek V4.1 Flash, Qwen3.8 27B; GPT-4 8,192 (OpenAI, Mar 2023); Claude 2.1 200,000 (Anthropic, Nov 2023) | Log x-axis. |

## Numbers quoted in text

| Claim | Source |
|-------|--------|
| Open-weight models above 62% of OpenRouter tokens since July 2026; 79% peak early July; Chinese labs 69% of tokens | OpenRouter, "The Token State of Play", Inferred 01, 22 Sep 2026, https://openrouter.ai/data/newsletter/the-token-state-of-play |
| OpenRouter weekly tokens 0.5T (Jan 2025) to 128.4T (Sep 2026) | same |
| METR time-horizon page no longer updated (8 Sep 2026); estimates above 16 h unreliable; tasks are software, ML, cybersecurity | https://metr.org/time-horizons/ |
| GPT-6.1 Sol $2 / $10 per 1M tokens; above 272k input, 2x input and 1.5x output | https://developers.openai.com/api/docs/pricing |
| GPT-6 Astra $10 / $50; GPT-6 Luna $0.10 / $0.50 | same |
| Gemini 4 Argon $2 / $10 until 30 Nov 2026, then $4 / $20 | https://ai.google.dev/gemini-api/docs/pricing |
| Grok 4.7: 21 Sep 2026, 500k context, $2 / $6 | https://docs.x.ai/developers/release-notes |
| Kimi K3.1 Pro: 23 Oct 2026, $2 / $10, weights promised by 4 Nov | https://www.kimi.ai/resources/kimi-k3-1-pro-pricing |
| Claude Opus 5.5 $4 / $20; cache reads $0.20; released 22 Sep 2026 | https://platform.claude.com/docs/en/models/opus-5-5/overview |
| Muse Wonder: 12 Oct 2026, $4 / $20 | https://about.fb.com/news/2026/10/introducing-muse-wonder-models/ |
| DeepSeek V4.1 Flash 1017 $0.02 / $1.00 on OpenRouter (26 Oct 2026; plan said $0.15 / $0.60, superseded) | https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017 |
| Codex app launch 2 Feb 2026 | https://openai.com/index/introducing-the-codex-app/ |
| One Codex harness behind CLI, IDE, app and web (App Server, JSON-RPC) | https://openai.com/index/unlocking-the-codex-harness/ |
| Claude Chat and Cowork unified, 16 Sep 2026 | https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude |
| Compaction definition | Anthropic, "Effective context engineering for AI agents", https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| Agent Skills format (SKILL.md, progressive disclosure) | https://agentskills.io/specification |
| MCP definition | https://modelcontextprotocol.io/specification |
| Harness definition | Macedo, arXiv:2606.10106, https://arxiv.org/abs/2606.10106 |
| "Agent = model + harness" | arXiv:2609.00006, https://arxiv.org/abs/2609.00006 |

## Screenshots

Every file in `screens/` is listed here with origin and capture date. Only real
captures or vendor press images with attribution. No mock-ups.

| File | Origin | Date |
|------|--------|------|
| `metr_time_horizon.png` | Chart element captured from https://metr.org/time-horizons/ | 26 Oct 2026 |
| `codex_cli.png`, `codex_vscode.png`, `codex_web.png` | OpenAI, "Unlocking the Codex harness", article images, https://openai.com/index/unlocking-the-codex-harness/ | 26 Oct 2026 |
| `codex_permission_prompt.png` | same article | 26 Oct 2026 |
| `chatgpt_app_*.png` | Video posters on https://learn.chatgpt.com/docs/app (ChatGPT desktop app with Chat, Work, Codex; Codex app merged into it on 9 Jul 2026, https://openai.com/index/chatgpt-for-your-most-ambitious-work/) | 26 Oct 2026 |
| `mcp_simple_diagram.png` | https://modelcontextprotocol.io/docs/getting-started/intro | 26 Oct 2026 |
| `agentskills_spec.png` | Viewport of https://agentskills.io/specification | 26 Oct 2026 |
| `claude_unified_article.png` | Viewport of https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude | 26 Oct 2026 |
| `claude_code_terminal.png` | Product image from https://www.anthropic.com/claude-code (Welcome to Claude Code). Cropped to the terminal window. | 27 Oct 2026 |
| `context_rot_boolean_related.png` | Boolean, "Context Rot Quantified", related-context chart, https://www.boolean.ai/blog/context-rot-quantified | 27 Oct 2026 |
| `../traces/opencode_fix_bug_2026-10-26.txt` | Real run: `opencode run --pure --auto -m opencode/deepseek-v4.1-flash-free` on a copy of `demo-lesson1`, 22 s, exit 0 | 26 Oct 2026 |
| `assets/real/antigravity_ide.png` | Earlier capture, reused | 2026 |

Not captured: native Claude desktop and Cursor windows (this machine has no
screen-recording permission and no Claude app). Swap in your own captures if
you want them; keep file names and the slides pick them up.

## Logos

None used. The deck names vendors in text.
