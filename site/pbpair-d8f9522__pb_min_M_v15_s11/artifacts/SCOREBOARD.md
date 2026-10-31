# SCOREBOARD

playbook: nogit-f045ba05
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | stack30 |
|---|---|---|
| lift | 67/100 = 67% | untested |
| stack | 51/100 = 51% | untested |
| nut | 0/100 = 0% | untested |
| wipe | 16/100 = 16% | untested |
| restack | 0/100 = 0% | untested |
| twolift | 1/100 = 1% | untested |
| handover | 2/100 = 2% | untested |
| revstack | 0/100 = 0% | untested |
| stackv2 | 1/100 = 1% | untested |

GPU-hours: 6.838 spent, 4.842 remaining of 16.0 (9 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)
Job 6 (eval stack30): queued (not started), 0 min in queue
Job 7 (eval stack30): queued (not started), 0 min in queue
Job 8 (eval stack30): queued (not started), 0 min in queue
Job 9 (eval stack30): queued (not started), 0 min in queue
Job 10 (eval stack30): queued (not started), 0 min in queue
Job 11 (eval stack30): queued (not started), 0 min in queue
Job 12 (eval stack30): queued (not started), 0 min in queue

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| stack30 | base | 30 | spec_stack30.json | trained |

## History (latest 30)

- train stack30 (init base, steps 30): trained
