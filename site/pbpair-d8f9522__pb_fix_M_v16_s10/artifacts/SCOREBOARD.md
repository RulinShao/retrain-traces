# SCOREBOARD

playbook: 7b74a5fa-a57a4058
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | stack_v1 |
|---|---|---|
| lift | 67/100 = 67% | 78/100 = 78% (base 67% = 67.0/100) |
| stack | 51/100 = 51% | 51/100 = 51% (base 51% = 51.0/100) |
| nut | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) |
| wipe | 16/100 = 16% | 20/100 = 20% (base 16% = 16.0/100) |
| restack | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) |
| twolift | 1/100 = 1% | 0/100 = 0% (base 1% = 1.0/100) |
| handover | 2/100 = 2% | 0/100 = 0% (base 2% = 2.0/100) |
| revstack | 0/100 = 0% | 1/100 = 1% (base 0% = 0.0/100) |
| stackv2 | 1/100 = 1% | 1/100 = 1% (base 1% = 1.0/100) |

GPU-hours: 9.752 spent, 6.248 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: stack_v1
Submitted: base + stack_v1 (sha 0133ce37ecff) (turn 50, token 5c697c; confirmed in turn 51)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| stack_v1 | base | 20 | specs/stack_v1.json | trained |

## History (latest 30)

- train stack_v1 (init base, steps 20): trained
- load stack_v1
- eval stack_v1 on lift: 78/100
- eval stack_v1 on stack: 51/100
- eval stack_v1 on stackv2: 1/100
- eval stack_v1 on nut: 0/100
- eval stack_v1 on wipe: 20/100
- eval stack_v1 on restack: 0/100
- eval stack_v1 on twolift: 0/100
- eval stack_v1 on handover: 0/100
- eval stack_v1 on revstack: 1/100
- finish: submitted stack_v1 (token 5c697c, job 44)
- finish: confirmed stack_v1 (token 5c697c)
