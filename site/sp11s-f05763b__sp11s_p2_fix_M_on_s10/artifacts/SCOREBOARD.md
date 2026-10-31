# SCOREBOARD

playbook: e9fea0d6-a57a4058
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | stk | stk2 |
|---|---|---|---|
| lift | 67/100 = 67% | 74/100 = 74% (base 67% = 67.0/100) | 16/20 = 80% (base 67% = 13.4/20) |
| stack | 51/100 = 51% | 66/100 = 66% (base 51% = 51.0/100) | 13/20 = 65% (base 51% = 10.2/20) |
| nut | 0/100 = 0% | untested | 0/20 = 0% (base 0% = 0.0/20) |
| wipe | 16/100 = 16% | 27/100 = 27% (base 16% = 16.0/100) | 6/20 = 30% (base 16% = 3.2/20) |
| restack | 0/100 = 0% | untested | 0/20 = 0% (base 0% = 0.0/20) |
| twolift | 1/100 = 1% | untested | 0/20 = 0% (base 1% = 0.2/20) |
| handover | 2/100 = 2% | untested | 0/20 = 0% (base 2% = 0.4/20) |
| revstack | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) | 0/20 = 0% (base 0% = 0.0/20) |
| stackv2 | 1/100 = 1% | 1/100 = 1% (base 1% = 1.0/100) | 0/20 = 0% (base 1% = 0.2/20) |

GPU-hours: 15.242 spent, 0.758 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: stk2
Submitted: base + stk2 (sha 2e5aa1009860) (turn 22, token 96ccf3; confirmed in turn 23)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| stk | base | 20 | specs/stk.json | trained |
| stk2 | stk | 10 | specs/stk2.json | trained |

## History (latest 30)

- train stk (init base, steps 20): trained
- eval stk on stack: 66/100
- eval stk on lift: 74/100
- eval stk on wipe: 27/100
- eval stk on stackv2: 1/100
- eval stk on revstack: 0/100
- load stk
- train stk2 (init stk, steps 10): trained
- eval stk2 on lift: 16/20
- eval stk2 on stack: 13/20
- eval stk2 on nut: 0/20
- eval stk2 on wipe: 6/20
- eval stk2 on restack: 0/20
- eval stk2 on twolift: 0/20
- eval stk2 on handover: 0/20
- eval stk2 on revstack: 0/20
- eval stk2 on stackv2: 0/20
- load stk2
- finish: submitted stk2 (token 96ccf3, job 24)
- finish: confirmed stk2 (token 96ccf3)
