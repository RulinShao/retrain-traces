# SCOREBOARD

playbook: nogit-f1700b86
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | rs1 | rev1 | cn2 | cn3 | cn4 | cn5 |
|---|---|---|---|---|---|---|---|
| nut | 0/100 = 0% | untested | untested | 0/100 = 0% (base 0% = 0.0/100) | untested | 0/100 = 0% (base 0% = 0.0/100) | untested |
| restack | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) | untested | 0/100 = 0% (base 0% = 0.0/100) | untested | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) |
| revstack | 1/100 = 1% | untested | 1/100 = 1% (base 1% = 1.0/100) | 4/200 = 2% (base 1% = 2.0/200) | untested | 1/100 = 1% (base 1% = 1.0/100) | 4/200 = 2% (base 1% = 2.0/200) |

GPU-hours: 45.755 spent, 2.245 remaining of 48.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: cn5
Submitted: base + cn5 (sha 6d2f1a67f355) (turn 39, token 363386; confirmed in turn 40)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| rs1 | base | 20 | spec_rs1.json | trained |
| rev1 | base | 15 | spec_rev1.json | trained |
| cn2 | rev1 | 20 | spec_cn2.json | trained |
| cn3 | cn2 | 20 | spec_cn3.json | trained |
| cn4 | cn3 | 20 | spec_cn4.json | trained |
| cn5 | cn2 | 20 | spec_cn5.json | trained |

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- restack: 16 failures in adapters/rs1/failures.jsonl; stages none:16
- revstack: 16 failures in adapters/rev1/failures.jsonl; stages lift the green_cube:8 none:6 align the green_cube over the red_cube:1 grasp the green_cube:1
- restack: 16 failures in adapters/cn2/failures.jsonl; stages none:8 unstack the green off the red:6 align the red over the green:1 unavailable:1
- nut: 16 failures in adapters/cn2/failures.jsonl; stages none:11 grasp the nut:5
- restack: 16 failures in adapters/cn3/failures.jsonl; stages none:12 align the red over the green:2 unstack the green off the red:2
- nut: 16 failures in adapters/cn3/failures.jsonl; stages none:14 grasp the nut:2
- restack: 16 failures in adapters/cn4/failures.jsonl; stages unstack the green off the red:10 none:5 align the red over the green:1
- nut: 16 failures in adapters/cn4/failures.jsonl; stages none:14 grasp the nut:1 reach the handle:1
- revstack: 16 failures in adapters/cn5/failures.jsonl; stages none:8 lift the green_cube:5 grasp the green_cube:2 align the green_cube over the red_cube:1

## History (latest 30)

- rollout base on restack: 16 seeds -> rollouts/1.jsonl; stages reached: unstack the green off the red 12/16, grasp the red 0/16, lift the red 1/16, align the red over the green 4/16, place the red on the green 0/16; distinct values over 16 rows: task_completed 1, sim_reward 16, stage unstack the green off the red 2, stage grasp the red 1, stage lift the red 2, stage align the red over the green 2, stage place the red on the green 1
- rollout base on revstack: 16 seeds -> rollouts/2.jsonl; stages reached: reach the green_cube 14/16, grasp the green_cube 10/16, lift the green_cube 2/16, align the green_cube over the red_cube 1/16, place the green_cube on the red_cube 0/16; distinct values over 16 rows: task_completed 1, sim_reward 16, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 2, stage place the green_cube on the red_cube 1
- rollout base on nut: 16 seeds -> rollouts/3.jsonl; stages reached: reach the handle 1/16, grasp the nut 1/16, align the nut over the peg 0/16, insert the nut 0/16; distinct values over 16 rows: task_completed 1, sim_reward 6, stage reach the handle 2, stage grasp the nut 2, stage align the nut over the peg 1, stage insert the nut 1
- train rs1 (init base, steps 20): trained
- eval rs1 on restack: 0/100
- rollout rs1 on restack: 16 seeds -> rollouts/8.jsonl; stages reached: unstack the green off the red 14/16, grasp the red 1/16, lift the red 0/16, align the red over the green 6/16, place the red on the green 0/16; distinct values over 16 rows: task_completed 1, sim_reward 16, stage unstack the green off the red 2, stage grasp the red 2, stage lift the red 1, stage align the red over the green 2, stage place the red on the green 1
- train cn1 failed: train: your reward function raised ModuleNotFoundError: No module named 'rewards' (reward.py line 5); no rollout could be scored, so the trainer stopped. reward(r) gets the simulator reply: task_completed, reward, sandbox_rc, seed, secs, wall_s, log_tail, task, stdout_tail, stages, final_state, trace
- train rev1 (init base, steps 15): trained
- train cn2 (init rev1, steps 20): trained
- eval rev1 on revstack: 1/100
- eval cn2 on restack: 0/100
- eval cn2 on nut: 0/100
- eval cn2 on revstack: 4/100
- train cn3 (init cn2, steps 20): trained
- train cn4 (init cn3, steps 20): trained
- eval cn4 on restack: 0/100
- eval cn4 on nut: 0/100
- eval cn4 on revstack: 1/100
- train cn5 (init cn2, steps 20): trained
- eval cn5 on revstack: 3/100
- eval cn5 on restack: 0/100
- eval cn2 on revstack: 4/200
- eval cn5 on revstack: 4/200
- load cn5
- finish: submitted cn5 (token 363386, job 37)
- finish: confirmed cn5 (token 363386)
