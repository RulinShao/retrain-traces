# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | broad1 |
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

GPU-hours: 5.784 spent, 2.806 remaining of 16.0 (10 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| broad1 | base | 15 | specs/round1_broad.json | trained |

## History (latest 30)

- train broad1 (init base, steps 15): trained
