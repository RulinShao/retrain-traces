# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | t1_shaped_rev | t1_shaped_nutr | probe_restack | t2_revstack |
|---|---|---|---|---|---|
| nut | untested | untested | 0/20 = 0% | untested | untested |
| restack | untested | untested | 0/20 = 0% | untested | untested |
| revstack | untested | 0/20 = 0% | untested | untested | 0/20 = 0% |

GPU-hours: 13.229 spent, 2.771 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: t2_revstack
Submitted: base + t2_revstack (sha aa34f89dd73f) (turn 49, token d5481f; confirmed in turn 50)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| t1_shaped_rev | base | 16 | specB.json | trained |
| t1_shaped_nutr | base | 24 | specA.json | trained |
| probe_restack | base | None | specsft_restack.json | trained |
| t2_revstack | t1_shaped_rev | 22 | specD.json | trained |

- train job 17 (probe_restack): prompt in 1 data row(s) set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- revstack: 16 failures in adapters/t1_shaped_rev/failures.jsonl; stages none:10 grasp the green_cube:4 lift the green_cube:2
- nut: 16 failures in adapters/t1_shaped_nutr/failures.jsonl; stages none:14 grasp the nut:1 reach the handle:1
- restack: 16 failures in adapters/t1_shaped_nutr/failures.jsonl; stages none:16
- revstack: 16 failures in adapters/t2_revstack/failures.jsonl; stages none:8 unavailable:4 grasp the green_cube:2 lift the green_cube:1 reach the green_cube:1

## History (latest 30)

- rollout base on nut: 8 seeds -> rollouts/1.jsonl; stages reached: reach the handle 0/8, grasp the nut 0/8, align the nut over the peg 0/8, insert the nut 0/8; distinct values over 8 rows: task_completed 1, sim_reward 4, stage reach the handle 1, stage grasp the nut 1, stage align the nut over the peg 1, stage insert the nut 1
- rollout base on restack: 8 seeds -> rollouts/2.jsonl; stages reached: unstack the green off the red 3/8, grasp the red 0/8, lift the red 0/8, align the red over the green 1/8, place the red on the green 1/8; distinct values over 8 rows: task_completed 2, sim_reward 6, stage unstack the green off the red 2, stage grasp the red 1, stage lift the red 1, stage align the red over the green 2, stage place the red on the green 2
- rollout base on revstack: 8 seeds -> rollouts/3.jsonl; stages reached: reach the green_cube 4/8, grasp the green_cube 3/8, lift the green_cube 1/8, align the green_cube over the red_cube 1/8, place the green_cube on the red_cube 0/8; distinct values over 8 rows: task_completed 1, sim_reward 8, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 2, stage place the green_cube on the red_cube 1
- train t1_shaped_all failed: train: task 'revstack' runs its simulator under a scene shift (capx_suite_scene_shift) and practises alone; name it in a spec of its own
- train t1_shaped_rev (init base, steps 16): trained
- train t1_shaped_nutr (init base, steps 24): trained
- eval t1_shaped_rev on revstack: 1/20
- preset restack_probe1 on restack: 6 seeds -> presets/restack_probe1.json
- preset restack_diag on restack: 4 seeds -> presets/restack_diag.json
- train probe_restack (init base, steps None): trained
- rollout probe_restack on restack: 6 seeds -> rollouts/19.jsonl; stages reached: unstack the green off the red 2/6, grasp the red 0/6, lift the red 0/6, align the red over the green 0/6, place the red on the green 0/6; distinct values over 6 rows: task_completed 1, sim_reward 5, stage unstack the green off the red 2, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1
- eval t1_shaped_nutr on restack: 0/20
- eval t1_shaped_nutr on nut: 0/20
- train t2_restack failed: train: reward must be 'task_completed', 'shaped' or the path of a .py file defining reward(result) -> float
- load t1_shaped_rev
- train t2_revstack (init t1_shaped_rev, steps 22): trained
- eval t2_revstack on revstack: 0/20
- eval t1_shaped_rev on revstack: 0/20
- load t2_revstack
- finish: submitted t2_revstack (token d5481f, job 35)
- finish: confirmed t2_revstack (token d5481f)
