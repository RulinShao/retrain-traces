# SCOREBOARD

playbook: nogit-a57a4058
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | wipe1 |
|---|---|---|
| wipe | 16/100 = 16% | untested |

GPU-hours: 6.838 spent, 0.682 remaining of 8.0 (1 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: wipe1
Submitted: none (python3 finish.py submits a policy)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| wipe1 | base | 30 | spec_wipe1.json | trained |

## History (latest 30)

- train wipe1 (init base, steps 30): trained
- load wipe1
