# Instructions for coding agents
[...]
## Layout

- `data/auto.dta`: raw data. Never modify or overwrite.
- `code/analysis.do`: the only analysis script.
- `output/`: generated tables. Safe to overwrite.
[...]
The log is written to `analysis.log` in the repository root.
Read it after every run: Stata reports errors there, not on
the terminal, and the exit code is 0 even when the do-file fails.

## Rules

1. Change the do-file, never the data.
2. Keep variable names short and lower case.
3. Report robust standard errors (`vce(robust)`) unless asked.
4. Before saying a task is done, run the do-file and show the
   last 20 lines of the log.
5. Do not install Stata packages without asking.
