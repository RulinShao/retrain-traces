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
| nut | 0/100 = 0% |
| restack | 0/100 = 0% |
| revstack | 1/100 = 1% |

GPU-hours: 0.915 spent, 14.942 remaining of 16.0 (1 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## History (latest 30)

- rollout base on restack: 10 seeds -> rollouts/1.jsonl; stages reached: unstack the green off the red 8/10, grasp the red 0/10, lift the red 0/10, align the red over the green 0/10, place the red on the green 0/10; distinct values over 10 rows: task_completed 1, sim_reward 10, stage unstack the green off the red 2, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1
- rollout base on revstack: 10 seeds -> rollouts/2.jsonl; stages reached: reach the green_cube 6/10, grasp the green_cube 6/10, lift the green_cube 1/10, align the green_cube over the red_cube 0/10, place the green_cube on the red_cube 0/10; distinct values over 10 rows: task_completed 1, sim_reward 8, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 1, stage place the green_cube on the red_cube 1
- rollout base on nut: 10 seeds -> rollouts/3.jsonl; stages reached: reach the handle 0/10, grasp the nut 0/10, align the nut over the peg 0/10, insert the nut 0/10; distinct values over 10 rows: task_completed 1, sim_reward 4, stage reach the handle 1, stage grasp the nut 1, stage align the nut over the peg 1, stage insert the nut 1
- preset probe_rev1 on revstack: 4 seeds -> presets/probe_rev1.json
- preset probe_rev2 on revstack: 4 seeds -> presets/probe_rev2.json
- preset probe_rev3 on revstack: 4 seeds -> presets/probe_rev3.json
