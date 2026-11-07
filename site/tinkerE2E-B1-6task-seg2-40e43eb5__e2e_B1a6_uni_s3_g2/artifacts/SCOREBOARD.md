# SCOREBOARD

playbook: none
agent: scripted:e2e-rl+6task-uniform-seg2
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base |
|---|---|
| lift | untested |
| stack | untested |
| wipe | untested |
| nut | untested |
| restack | untested |
| revstack | untested |

GPU-hours: 0.000 spent, 4.684 remaining of 16.0 (1 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.44, 10 steps 2.42, 50 steps 11.23) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|

## History (latest 30)

