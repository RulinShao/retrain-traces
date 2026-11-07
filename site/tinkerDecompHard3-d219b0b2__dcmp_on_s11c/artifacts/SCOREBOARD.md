# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | b_revstack | a_nutrestack | a_nutrestack+b_revstack |
|---|---|---|---|---|
| nut | 0/100 = 0% | untested | 0/20 = 0% (base 0% = 0.0/20) | untested |
| restack | 0/100 = 0% | untested | 0/20 = 0% (base 0% = 0.0/20) | untested |
| revstack | 1/100 = 1% | 0/20 = 0% (base 1% = 0.2/20) | untested | 0/20 = 0% (base 1% = 0.2/20) |

GPU-hours: 9.209 spent, 6.481 remaining of 16.0 (2 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)
Job 27 (preset diag5_rev): queued (not started), 1 min in queue

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| b_revstack | base | 20 | spec_b.json | trained |
| a_nutrestack | base | 20 | spec_a.json | trained |

- train job 5 (a_nutrestack): note set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim
- train job 6 (b_revstack): note set: part of the training prompt only; every eval, including the final score, uses tasks/revstack/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- job 1: rollout base on nut: 5 seeds -> rollouts/1.jsonl; self-reward mean 0.0 over 5 seeds (reward_shape.py); stages reached: reach the handle 0/5, grasp the nut 0/5, align the nut over the peg 0/5, insert the nut 0/5; distinct values over 5 rows: task_completed 1, sim_reward 4, stage reach the handle 1, stage grasp the nut 1, stage align the nut over the peg 1, stage insert the nut 1
- job 2: rollout base on restack: 5 seeds -> rollouts/2.jsonl; self-reward mean 0.0 over 5 seeds (reward_shape.py); stages reached: unstack the green off the red 3/5, grasp the red 0/5, lift the red 0/5, align the red over the green 0/5, place the red on the green 0/5; distinct values over 5 rows: task_completed 1, sim_reward 5, stage unstack the green off the red 2, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1
- job 3: rollout base on revstack: 5 seeds -> rollouts/3.jsonl; self-reward mean 0.27 over 5 seeds (reward_shape.py); stages reached: reach the green_cube 2/5, grasp the green_cube 2/5, lift the green_cube 1/5, align the green_cube over the red_cube 0/5, place the green_cube on the red_cube 0/5; distinct values over 5 rows: task_completed 1, sim_reward 4, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 1, stage place the green_cube on the red_cube 1

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- revstack: 16 failures in adapters/b_revstack/failures.jsonl; stages none:10 grasp the green_cube:4 reach the green_cube:2
- nut: 16 failures in adapters/a_nutrestack/failures.jsonl; stages none:15 grasp the nut:1
- restack: 16 failures in adapters/a_nutrestack/failures.jsonl; stages none:16

## History (latest 30)

- rollout base on nut: 5 seeds -> rollouts/1.jsonl; self-reward mean 0.0 over 5 seeds (reward_shape.py); stages reached: reach the handle 0/5, grasp the nut 0/5, align the nut over the peg 0/5, insert the nut 0/5; distinct values over 5 rows: task_completed 1, sim_reward 4, stage reach the handle 1, stage grasp the nut 1, stage align the nut over the peg 1, stage insert the nut 1
- rollout base on restack: 5 seeds -> rollouts/2.jsonl; self-reward mean 0.0 over 5 seeds (reward_shape.py); stages reached: unstack the green off the red 3/5, grasp the red 0/5, lift the red 0/5, align the red over the green 0/5, place the red on the green 0/5; distinct values over 5 rows: task_completed 1, sim_reward 5, stage unstack the green off the red 2, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1
- rollout base on revstack: 5 seeds -> rollouts/3.jsonl; self-reward mean 0.27 over 5 seeds (reward_shape.py); stages reached: reach the green_cube 2/5, grasp the green_cube 2/5, lift the green_cube 1/5, align the green_cube over the red_cube 0/5, place the green_cube on the red_cube 0/5; distinct values over 5 rows: task_completed 1, sim_reward 4, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 1, stage place the green_cube on the red_cube 1
- train a_nutrestack failed: train: note edit one task's training prompt; a spec naming several tasks cannot set them
- train b_revstack (init base, steps 20): trained
- train a_nutrestack (init base, steps 20): trained
- eval a_nutrestack on nut: 0/20
- eval a_nutrestack on restack: 0/20
- eval b_revstack on revstack: 0/20
- eval a_nutrestack+b_revstack on revstack: 0/20
- preset diag_rev on revstack: 8 seeds -> presets/diag_rev.json
- preset diag2_rev on revstack: 8 seeds -> presets/diag2_rev.json
- preset diag3_rev on revstack: 8 seeds -> presets/diag3_rev.json
- preset diag4_rev on revstack: 8 seeds -> presets/diag4_rev.json
- cancel job 27
