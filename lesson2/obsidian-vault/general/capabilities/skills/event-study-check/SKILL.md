---
name: event-study-check
description: Check an event-study or staggered DiD estimate before it goes into a draft.
---

# Event-study check

## When to use
Before any event-study figure or DiD table is reported in the paper or a reply.

## Steps
1. Confirm the treatment timing variable against [[education-labor-supply_DECISIONS]].
2. Plot leads and lags; report the joint test on the leads.
3. Re-estimate with a heterogeneity-robust estimator (Callaway and Sant'Anna or Sun and Abraham).
4. Drop one cohort at a time; flag any cohort that moves the estimate.
5. Write the result and the commands into TECHNICAL_NOTES.

## Output
A short note with the figure path, the lead test and any warning.
