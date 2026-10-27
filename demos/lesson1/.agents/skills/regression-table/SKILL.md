---
name: regression-table
description: Turn stored Stata estimates into a paper-ready LaTeX
  table with esttab. Use when the user asks for a regression table,
  a results table, or to export estimates to LaTeX.
---

# Regression table

1. Check that `esttab` is installed: `which esttab`.
   If missing, stop and ask.
2. Store each model with `estimates store mN` right after
   the regression.
3. Export with:

   esttab m1 m2 using "output/table1.tex", replace ///
       se label booktabs star(* 0.10 ** 0.05 *** 0.01) ///
       stats(N r2, labels("Observations" "R-squared"))

4. Open the `.tex` file and check: one column per model,
   standard errors in parentheses, observations in the last rows.
5. Tell the user which file was written and how many columns
   it has.
