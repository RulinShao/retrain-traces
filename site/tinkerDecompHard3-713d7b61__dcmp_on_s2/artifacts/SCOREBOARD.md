# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base |
|---|---|
| nut | 0/20 = 0% |
| restack | 0/20 = 0% |
| revstack | 0/20 = 0% |

GPU-hours: 0.579 spent, 12.738 remaining of 16.0 (1 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)
Job 1 (train nr1): running, step 13/14, mean reward 0.000, rollouts with reward > 0 0.00, groups with zero reward variance 1.00, failed rollouts by stage: program 24; task 40, 2.51 GPU-h so far

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## History (latest 30)

- eval base on nut: 0/20
- eval base on restack: 0/20
- eval base on revstack: 0/20
- cancel job 1
