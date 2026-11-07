# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | diag |
|---|---|---|
| nut | 0/100 = 0% | untested |
| restack | 0/100 = 0% | untested |
| revstack | 1/100 = 1% | untested |

GPU-hours: 2.568 spent, 13.153 remaining of 16.0 (2 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)
Job 23 (preset diag_observe): queued (not started), 258 min in queue; held by the lab's shared-GPU reserve queue (a guard that keeps this project's running jobs on the lab-owned GPU pool at or under a cap and releases held jobs in its own order as running jobs finish): position 386 of 483 held as of 2026-11-06T01:04:52Z, re-planned every 10 min; a cancelled job leaves this queue; a resubmission is a new job with a later submit time, which the guard plans at its next pass and orders behind the waiting jobs of its priority class submitted before it

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| diag | base | None | spec_diag.json | trained |

- train job 26 (diag): note set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## History (latest 30)

- rollout base on revstack: 8 seeds -> rollouts/2.jsonl; stages reached: reach the green_cube 5/8, grasp the green_cube 5/8, lift the green_cube 1/8, align the green_cube over the red_cube 0/8, place the green_cube on the red_cube 0/8; distinct values over 8 rows: task_completed 1, sim_reward 7, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 1, stage place the green_cube on the red_cube 1
- rollout base on restack: 8 seeds -> rollouts/1.jsonl; stages reached: unstack the green off the red 5/8, grasp the red 0/8, lift the red 0/8, align the red over the green 1/8, place the red on the green 0/8; distinct values over 8 rows: task_completed 1, sim_reward 8, stage unstack the green off the red 2, stage grasp the red 1, stage lift the red 1, stage align the red over the green 2, stage place the red on the green 1
- rollout base on nut: 8 seeds -> rollouts/3.jsonl; stages reached: reach the handle 0/8, grasp the nut 0/8, align the nut over the peg 0/8, insert the nut 0/8; distinct values over 8 rows: task_completed 1, sim_reward 3, stage reach the handle 1, stage grasp the nut 1, stage align the nut over the peg 1, stage insert the nut 1
- preset restack_cand on restack: 8 seeds -> presets/restack_cand.json
- preset revstack_cand on revstack: 16 seeds -> presets/revstack_cand.json
- preset nut_cand on nut: 16 seeds -> presets/nut_cand.json
- preset diag_restack on restack: 4 seeds -> presets/diag_restack.json
- preset revstack_cand2 on revstack: 16 seeds -> presets/revstack_cand2.json
- preset nut_cand2 on nut: 16 seeds -> presets/nut_cand2.json
- preset revstack_v3 on revstack: 16 seeds -> presets/revstack_v3.json
- preset restack_v3 failed: preset: the reached state could not be restored on seeds [800117, 800119, 800121, 800122, 800123, 800129, 800130, 800131] (seed 800117: ValueError: executing action in terminated episode; seed 800119: ValueError: executing action in terminated episode; seed 800121: ValueError: executing action in terminated episode; seed 800122: ValueError: executing action in terminated episode; seed 800123: ValueError: executing action in terminated episode; seed 800129: ValueError: executing action in terminated episode; seed 800130: ValueError: executing action in terminated episode; seed 800131: ValueError: executing action in terminated episode); no preset was saved
- preset nut_v3 on nut: 16 seeds -> presets/nut_v3.json
- rollout base on revstack: 5 seeds -> rollouts/20.jsonl; stages reached: reach the green_cube 3/5, grasp the green_cube 2/5, lift the green_cube 0/5, align the green_cube over the red_cube 0/5, place the green_cube on the red_cube 0/5; distinct values over 5 rows: task_completed 1, sim_reward 5, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 1, stage align the green_cube over the red_cube 1, stage place the green_cube on the red_cube 1
- preset diag_cam2 on revstack: 3 seeds -> presets/diag_cam2.json
- train diag failed: train: field(s) ['note'] have no meaning with objective 'sft'; an sft spec reads only: objective, data, name, epochs, batch, lr, min_reward, init, time
- train diag (init base, steps None): trained
- cancel job 23
