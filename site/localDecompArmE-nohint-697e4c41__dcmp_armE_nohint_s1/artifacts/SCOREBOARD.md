# SCOREBOARD

playbook: nogit-02604056
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base |
|---|---|
| nut | untested |
| restack | untested |
| revstack | untested |

GPU-hours: 0.540 spent, 43.720 remaining of 48.0 (1 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)
Job 3 (train r1): queued (not started), 180 min in queue

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## History (latest 30)

- rollout base on restack: 16 seeds -> rollouts/1.jsonl; stages reached: unstack the green off the red 9/16, grasp the red 0/16, lift the red 0/16, align the red over the green 3/16, place the red on the green 0/16; distinct values over 16 rows: task_completed 1, sim_reward 13, stage unstack the green off the red 2, stage grasp the red 1, stage lift the red 1, stage align the red over the green 2, stage place the red on the green 1
- rollout base on revstack: 16 seeds -> rollouts/4.jsonl; stages reached: reach the green_cube 15/16, grasp the green_cube 10/16, lift the green_cube 1/16, align the green_cube over the red_cube 0/16, place the green_cube on the red_cube 0/16; distinct values over 16 rows: task_completed 1, sim_reward 12, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 1, stage place the green_cube on the red_cube 1
- rollout base on nut: 16 seeds -> rollouts/5.jsonl; stages reached: reach the handle 2/16, grasp the nut 2/16, align the nut over the peg 1/16, insert the nut 0/16; distinct values over 16 rows: task_completed 1, sim_reward 13, stage reach the handle 2, stage grasp the nut 2, stage align the nut over the peg 2, stage insert the nut 1
