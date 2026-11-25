# Log

Chronological, oldest first. One entry per session. Facts and decisions only; no transcripts or hidden reasoning.

## 2026-11-10 — Project kickoff (synthetic)

**Intent:** Create a realistic demonstration project for the Second Brain architecture.
**Did:** Scaffolded the 11 core files from the global templates; wrote the first version of [PROJECT_BRIEF.md](PROJECT_BRIEF.md) with the question, mechanisms H-01 to H-04, scope, and data needs; added the synthetic concept note to `raw/` and registered it as S-001 in [SOURCES.md](SOURCES.md).
**Learned:** The policy question only becomes researchable once the outcome is fixed and the treatment is defined at a consistent geographic level. Both were left open deliberately at kickoff.
**Decided:** none.
**Open:** design family, primary outcome, unit of analysis, treatment definition.
**Next:** run a design session and record binding choices.

## 2026-11-12 — Design session: estimator, outcome, panel

**Intent:** Convert the open design questions into decisions specific enough to write a data request against.
**Did:** Recorded D-001 (staggered DiD with group-time ATTs and not-yet-treated comparison), D-002 (formal employment rate as the only primary outcome), and D-003 (district × quarter panel, event time in quarters, ≥4 pre-periods) in [DECISIONS.md](DECISIONS.md). Wrote the stable method reference [wiki/difference-in-differences-design.md](wiki/difference-in-differences-design.md) and linked it from the project index. Updated [CURRENT_STATE.md](CURRENT_STATE.md).
**Learned:** With staggered timing and heterogeneous effects, a single TWFE coefficient is a weighted mix that can be misleading, so it is demoted to a descriptive benchmark. The treatment definition cannot be settled from the documents available: first station opening and 25% network coverage imply different cohorts, and partial rollouts are ambiguous.
**Decided:** D-001, D-002, D-003.
**Open:** Q-01 treatment definition; Q-02 handling of three partially served districts; Q-03 residence vs workplace measurement.
**Next:** draft the variable-level data request (A-01) and the specification grid (A-02).

## 2026-11-18 — [DEMO] Bootstrap and session-close simulation

**Intent:** Verify that a fresh agent can recover this project from Markdown alone, then exercise the close protocol without inventing research progress.
**Did:** Read the global layer (AGENTS, INDEX, MEMORY, GLOBAL_DECISIONS, BOOTSTRAP) and six project files (INDEX, PROJECT_BRIEF, CURRENT_STATE, NEXT_ACTIONS, DECISIONS, AGENT_MEMORY). Recovered the question, state, D-001, and actions A-01 to A-03 from 11 files / 734 lines. Ran `bash .infra/scripts/validate.sh` (41 checks, 0 errors). Added this labelled demonstration entry and updated `CURRENT_STATE.md`, `NEXT_ACTIONS.md`, `TECHNICAL_NOTES.md`, `AGENT_MEMORY.md`, and the summary.
**Learned:** The design is recoverable without reading `LOG.md`, `raw/`, or the wiki page. The validator catches unindexed wiki pages and broken links; both were tested, including a failing probe.
**Decided:** none. No research decision was made or confirmed in this session.
**Open:** Q-01 still blocks the final treatment definition; A-01 and A-02 are unchanged; no data exists.
**Next:** draft A-01, the variable-level data request.

## 2026-11-21 — [DEMO] Close protocol run

**Intent:** Run the close prompt end-to-end on the demo project without inventing research progress.
**Did:** Re-read `SESSION_CLOSE.md`, `CURRENT_STATE.md`, `NEXT_ACTIONS.md`, `AGENT_MEMORY.md`, and the last log entry. Confirmed no new research work and no new confirmed decision. Refreshed the state date, verification date, validation note, this log entry, and the session summary.
**Learned:** The protocol is safe on a no-op session: it records verification instead of manufacturing activity. Vault validation now covers two registered projects (46 checks) and still passes.
**Decided:** none.
**Open:** Q-01, Q-02, Q-03 unchanged; A-01 and A-02 open; A-03 blocked; no data exists.
**Next:** draft A-01.
