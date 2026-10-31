# SCOREBOARD

playbook: 7b74a5fa-a57a4058
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | wipe1 | stack1 | wipe1+stack1 |
|---|---|---|---|---|
| lift | 67/100 = 67% | 65/100 = 65% (base 67% = 67.0/100) | untested | 76/100 = 76% (base 67% = 67.0/100) |
| stack | 51/100 = 51% | 55/100 = 55% (base 51% = 51.0/100) | 36/100 = 36% (base 51% = 51.0/100) | 57/100 = 57% (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |
| wipe | 16/100 = 16% | 59/100 = 59% (base 16% = 16.0/100) | untested | 62/100 = 62% (base 16% = 16.0/100) |
| restack | 0/100 = 0% | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |
| twolift | 1/100 = 1% | untested | untested | 0/20 = 0% (base 1% = 0.2/20) |
| handover | 2/100 = 2% | untested | untested | 0/20 = 0% (base 2% = 0.4/20) |
| revstack | 0/100 = 0% | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |
| stackv2 | 1/100 = 1% | untested | untested | 1/20 = 5% (base 1% = 0.2/20) |

GPU-hours: 15.074 spent, 0.926 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: wipe1+stack1
Submitted: base + wipe1 (sha 4abef8643c83) + stack1 (sha 04de424500ac) (turn 23, token 02a818; confirmed in turn 24)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| wipe1 | base | 20 | specs/wipe1.json | trained |
| stack1 | base | 10 | specs/stack1.json | trained |

## History (latest 30)

- train wipe1 (init base, steps 20): trained
- train stack1 (init base, steps 10): trained
- eval wipe1 on wipe: 59/100
- eval wipe1 on stack: 55/100
- eval wipe1 on lift: 65/100
- eval stack1 on stack: 36/100
- eval wipe1+stack1 on wipe: 62/100
- eval wipe1+stack1 on stack: 57/100
- eval wipe1+stack1 on lift: 76/100
- load wipe1+stack1
- eval wipe1+stack1 on restack: 0/20
- eval wipe1+stack1 on nut: 0/20
- eval wipe1+stack1 on twolift: 0/20
- eval wipe1+stack1 on handover: 0/20
- eval wipe1+stack1 on revstack: 0/20
- eval wipe1+stack1 on stackv2: 1/20
- finish: submitted wipe1+stack1 (token 02a818, job 27)
- finish: confirmed wipe1+stack1 (token 02a818)
