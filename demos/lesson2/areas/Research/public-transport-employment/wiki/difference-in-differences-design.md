# Difference-in-Differences with Staggered Adoption

**Scope:** a working reference for the design chosen in D-001. It covers the estimand, assumptions, why the naive two-way fixed-effects (TWFE) coefficient is not automatically a causal effect under staggered timing, and the diagnostics this project must report. It is not a literature review and cites no papers; the methodological source (S-002) has not been acquired.

## Summary

With staggered adoption, units start treatment in different periods. A single TWFE coefficient averages many 2×2 comparisons — already-treated units can serve as controls, and effects that change over time receive misleading weights. The defensible approach is to estimate cohort-by-period effects against a clean comparison group (not-yet-treated or never-treated), then aggregate them into an event-study path and a summary effect. The design is credible only if parallel trends holds for those comparisons, treatment timing is not driven by anticipated outcomes, and the treatment definition is fixed before estimation.

## Estimand

For district *i*, treatment cohort *g* (the period of first treatment), and period *t*:

```text
ATT(g, t) = E[Y_it(g) - Y_it(0) | G_i = g]
```

Estimated by comparing the change in treated cohort *g* from a pre-period baseline to period *t* with the change over the same window in districts not yet treated at *t* (or never treated, if a credible pool exists).

Aggregations used here:

- **Event study:** `ATT(g, t)` averaged across cohorts at event time `e = t - g`. Used for pre-trends and dynamics.
- **Overall ATT:** a weighted average over post-treatment `(g, t)` cells, with weights reported. Weights are a design choice, not a detail.

## Assumptions, and how each can fail here

| Assumption | Meaning | Failure mode in this project |
|---|---|---|
| Parallel trends | Absent treatment, treated and comparison cohorts would have followed the same outcome path | Rollout targets districts already growing; a pre-trend test has low power with few clusters |
| No anticipation | Outcomes do not respond before revenue service | Construction begins years earlier; firms and residents may anticipate |
| Consistency / SUTVA | A district's outcome depends only on its own treatment | Network spillovers across district boundaries; commuters cross districts |
| Correct treatment definition | The coded treatment date matches the economically relevant access change | First station opening ≠ usable network (Q-01) |
| Stable composition | The outcome is measured for a comparable population | Residential sorting changes who lives in a district (H-03) |

Parallel trends is not testable in the treatment period; a flat pre-trend is supporting evidence, not proof. With 24 districts and 11 treated, the test has limited power, so a failure to reject is weak evidence.

## Why not plain TWFE

Under staggered timing with heterogeneous or time-varying effects, the TWFE coefficient is a weighted average of:

- treated-versus-not-yet-treated comparisons (the intended ones),
- later-treated versus earlier-treated comparisons, where already-treated units act as controls,
- timing comparisons contaminated by treatment effects.

When effects grow with exposure, the later-versus-earlier comparisons can carry negative weights and reverse the sign of the aggregate. The problem is not fixed by adding covariates or clustering; it comes from the weighting. TWFE is therefore reported here only as a descriptive benchmark, as required by D-001.

## Practical sequence

1. **Fix the treatment definition** and write it down before seeing outcomes. Record partial-rollout rules explicitly.
2. **Build the cohort variable** and count pre-periods per cohort. Cohorts with fewer than four pre-quarters are excluded from the main estimate (D-003).
3. **Check the comparison pool.** For late periods there may be no not-yet-treated districts. Decide in advance how the last cohort is handled; never let software choose silently.
4. **Estimate `ATT(g, t)`** with district and period fixed effects, using a not-yet-treated comparison.
5. **Inspect pre-trends** cohort by cohort, not only in aggregate. Report confidence intervals, not just point estimates.
6. **Aggregate** to an event-study path and an overall ATT; state the weights.
7. **Stress test:** alternative treatment definitions, with/without partial-rollout districts, alternative event windows, and a small-cluster inference check (e.g. wild cluster bootstrap or randomization inference).
8. **Report null and negative results** with the same prominence as positive ones.

## Diagnostics checklist

- [ ] Cohort sizes and treatment dates table, with pre-period counts.
- [ ] Comparison group used in each period, including the last cohort's handling.
- [ ] Event-study plot with pre-treatment coefficients and intervals.
- [ ] Sensitivity to treatment definition (Q-01) and to Q-02 districts.
- [ ] Sensitivity to the population denominator (sorting, H-03).
- [ ] Small-cluster inference, not only conventional clustered standard errors.
- [ ] Placebo outcome and placebo treatment date, where feasible.
- [ ] Explicit statement of what the design cannot identify (mechanisms, metro-wide effects).

## Limits and open questions

- District-level data cannot separate access improvements from residential sorting; the design estimates a net district-level effect, not a structural mechanism.
- Local effects may coexist with zero metro-wide effects if firms relocate (H-04). The estimand is local.
- The method family is evolving; estimator choice should be justified against the actual cohort structure, not by convention.
- This page records standard practice as understood at the time of writing, without a verified citation. Treat it as a design aid, not an authority.

## Related

- [Project index](../INDEX.md)
- [Project brief](../PROJECT_BRIEF.md)
- [Decisions D-001 to D-003](../DECISIONS.md)
- [Current state](../CURRENT_STATE.md)
