# SCOREBOARD

playbook: 7b74a5fa-a57a4058
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | wipe30 | stack30 | wipe30+stack30 |
|---|---|---|---|---|
| lift | 67/100 = 67% | untested | untested | 73/100 = 73% (base 67% = 67.0/100) |
| stack | 51/100 = 51% | untested | untested | 54/100 = 54% (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | untested | untested |
| wipe | 16/100 = 16% | untested | untested | 74/100 = 74% (base 16% = 16.0/100) |
| restack | 0/100 = 0% | untested | untested | untested |
| twolift | 1/100 = 1% | untested | untested | untested |
| handover | 2/100 = 2% | untested | untested | untested |
| revstack | 0/100 = 0% | untested | untested | untested |
| stackv2 | 1/100 = 1% | untested | untested | untested |

GPU-hours: 15.116 spent, 0.884 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: wipe30+stack30
Submitted: base + wipe30 (sha 69dff07c5a2f) + stack30 (sha 0455b7a12388) (turn 18, token 0ce443; confirmed in turn 19)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| wipe30 | base | 30 | specs/wipe30.json | trained |
| stack30 | base | 30 | specs/stack30.json | trained |

## History (latest 30)

- train wipe30 (init base, steps 30): trained
- train stack30 (init base, steps 30): trained
- load wipe30+stack30
- eval wipe30+stack30 on lift: 73/100
- eval wipe30+stack30 on stack: 54/100
- eval wipe30+stack30 on wipe: 74/100
- finish: submitted wipe30+stack30 (token 0ce443, job 15)
- finish: confirmed wipe30+stack30 (token 0ce443)
