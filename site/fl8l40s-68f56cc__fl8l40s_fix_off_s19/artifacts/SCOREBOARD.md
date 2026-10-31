# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 900001
policy: Qwen3-8B+init:79fbddb55dd8

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | st | rk | rv | wp |
|---|---|---|---|---|---|
| lift | 89/100 = 89% | 86/100 = 86% (base 89% = 89.0/100) | untested | untested | 90/100 = 90% (base 89% = 89.0/100) |
| stack | 57/100 = 57% | 58/100 = 58% (base 57% = 57.0/100) | untested | untested | 58/100 = 58% (base 57% = 57.0/100) |
| nut | 0/100 = 0% | untested | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |
| wipe | 22/100 = 22% | untested | untested | untested | 71/100 = 71% (base 22% = 22.0/100) |
| restack | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |
| twolift | 0/100 = 0% | untested | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |
| handover | 0/100 = 0% | untested | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |
| revstack | 2/100 = 2% | 1/100 = 1% (base 2% = 2.0/100) | untested | untested | 1/20 = 5% (base 2% = 0.4/20) |
| stackv2 | 1/100 = 1% | 4/100 = 4% (base 1% = 1.0/100) | untested | untested | 0/20 = 0% (base 1% = 0.2/20) |

GPU-hours: 11.896 spent, 4.104 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.47, 10 steps 0.70, 50 steps 1.70) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: wp
Submitted: base + wp (sha a6582e6c90e3) (turn 37, token c387ce; confirmed in turn 38)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| st | base | 40 | specs/st.json | trained |
| rk | base | 40 | specs/rk.json | trained |
| rv | base | 40 | specs/rv.json | trained |
| wp | base | 40 | specs/wp.json | trained |

- train job 1 (st): note set: part of the training prompt only; every eval, including the final score, uses tasks/stack/eval_prompt.txt verbatim
- train job 2 (rk): note set: part of the training prompt only; every eval, including the final score, uses tasks/restack/eval_prompt.txt verbatim
- train job 3 (rv): note set: part of the training prompt only; every eval, including the final score, uses tasks/revstack/eval_prompt.txt verbatim
- train job 4 (wp): note set: part of the training prompt only; every eval, including the final score, uses tasks/wipe/eval_prompt.txt verbatim

## History (latest 30)

- train st (init base, steps 40): trained
- eval st on stack: 58/100
- eval st on lift: 86/100
- eval st on stackv2: 4/100
- eval st on revstack: 1/100
- eval st on restack: 0/100
- train rk (init base, steps 40): trained
- train rv (init base, steps 40): trained
- train wp (init base, steps 40): trained
- load wp
- eval wp on lift: 90/100
- eval wp on nut: 0/20
- eval wp on restack: 0/20
- eval wp on twolift: 0/20
- eval wp on handover: 0/20
- eval wp on stack: 58/100
- eval wp on wipe: 71/100
- eval wp on revstack: 1/20
- eval wp on stackv2: 0/20
- finish: submitted wp (token c387ce, job 44)
- finish: confirmed wp (token c387ce)
