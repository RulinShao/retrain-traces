# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | sftv1 | probe1 | probe2 | g1rev | g2nr | g1rev2 | g3rest |
|---|---|---|---|---|---|---|---|---|
| nut | 0/100 = 0% | untested | untested | untested | untested | 0/100 = 0% (base 0% = 0.0/100) | untested | untested |
| restack | 0/100 = 0% | untested | untested | untested | untested | 0/100 = 0% (base 0% = 0.0/100) | untested | untested |
| revstack | 1/100 = 1% | untested | untested | untested | 1/100 = 1% (base 1% = 1.0/100) | untested | untested | untested |

GPU-hours: 15.642 spent, 0.358 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: g1rev2+g2nr
Submitted: base + g1rev2 (sha 8ed3cce4d220) + g2nr (sha 05be13147319) (turn 110, token d472a9; confirmed in turn 111)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| sftv1 | base | None | spec_sft.json | trained |
| probe1 | base | None | spec_sft_probe.json | trained |
| probe2 | probe1 | None | spec_sft_probe2.json | trained |
| g1rev | base | 20 | spec_g1rev.json | trained |
| g2nr | base | 20 | spec_g2nr.json | trained |
| g1rev2 | g1rev | 12 | spec_g1b.json | trained |
| g3rest | base | 12 | spec_g3r.json | trained |

- train job 34 (g1rev): note set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim
- train job 51 (g1rev2): note set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim
- train job 52 (g3rest): note set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- revstack: 16 failures in adapters/g1rev/failures.jsonl; stages none:11 grasp the green_cube:5
- nut: 16 failures in adapters/g2nr/failures.jsonl; stages none:14 reach the handle:2
- restack: 16 failures in adapters/g2nr/failures.jsonl; stages none:16
- revstack: 16 failures in adapters/g1rev2/failures.jsonl; stages none:12 grasp the green_cube:2 lift the green_cube:2
- restack: 16 failures in adapters/g3rest/failures.jsonl; stages none:14 grasp the red:1 unstack the green off the red:1

## History (latest 30)

- rollout base on restack: 20 seeds -> rollouts/2.jsonl; stages reached: unstack the green off the red 12/20, grasp the red 0/20, lift the red 0/20, align the red over the green 0/20, place the red on the green 0/20; distinct values over 20 rows: task_completed 1, sim_reward 18, stage unstack the green off the red 2, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1
- rollout base on revstack: 20 seeds -> rollouts/3.jsonl; stages reached: reach the green_cube 18/20, grasp the green_cube 12/20, lift the green_cube 3/20, align the green_cube over the red_cube 2/20, place the green_cube on the red_cube 0/20; distinct values over 20 rows: task_completed 1, sim_reward 18, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 2, stage place the green_cube on the red_cube 1
- preset rev_v1 on revstack: 8 seeds -> presets/rev_v1.json
- preset rev_v2 on revstack: 8 seeds -> presets/rev_v2.json
- preset nut_v1 on nut: 8 seeds -> presets/nut_v1.json
- preset rst_v1 on restack: 8 seeds -> presets/rst_v1.json
- preset diag2 on revstack: 2 seeds -> presets/diag2.json
- cancel job 14
- preset diag1 cancelled: preset diag1 cancelled; no preset kept (a preset needs every seed's state); charged 0.000 GPU-h
- train sftv1 failed: train: data line 1: not a JSON object
- train sftv1 (init base, steps None): trained
- load sftv1
- rollout sftv1 on revstack: 5 seeds -> rollouts/24.jsonl; stages reached: reach the green_cube 3/5, grasp the green_cube 1/5, lift the green_cube 0/5, align the green_cube over the red_cube 0/5, place the green_cube on the red_cube 0/5; distinct values over 5 rows: task_completed 1, sim_reward 5, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 1, stage align the green_cube over the red_cube 1, stage place the green_cube on the red_cube 1
- train probe1 (init base, steps None): trained
- rollout probe1 on revstack: 3 seeds -> rollouts/28.jsonl; stages reached: reach the green_cube 1/3, grasp the green_cube 1/3, lift the green_cube 1/3, align the green_cube over the red_cube 0/3, place the green_cube on the red_cube 0/3; distinct values over 3 rows: task_completed 1, sim_reward 3, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 1, stage place the green_cube on the red_cube 1
- train probe2 (init probe1, steps None): trained
- rollout probe2 on revstack: 4 seeds -> rollouts/32.jsonl; stages reached: reach the green_cube 0/4, grasp the green_cube 0/4, lift the green_cube 0/4, align the green_cube over the red_cube 0/4, place the green_cube on the red_cube 0/4; distinct values over 4 rows: task_completed 1, sim_reward 4, stage reach the green_cube 1, stage grasp the green_cube 1, stage lift the green_cube 1, stage align the green_cube over the red_cube 1, stage place the green_cube on the red_cube 1
- train g1rev (init base, steps 20): trained
- train g2nr (init base, steps 20): trained
- eval g1rev on revstack: 1/100
- eval g2nr on nut: 0/100
- cancel job 42
- eval g2nr cancelled: eval cancelled; charged 0.053 GPU-h
- rollout g1rev on revstack: 20 seeds -> rollouts/48.jsonl; stages reached: reach the green_cube 16/20, grasp the green_cube 13/20, lift the green_cube 2/20, align the green_cube over the red_cube 1/20, place the green_cube on the red_cube 0/20; distinct values over 20 rows: task_completed 1, sim_reward 16, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 2, stage place the green_cube on the red_cube 1
- eval g2nr on restack: 0/100
- train g1rev2 (init g1rev, steps 12): trained
- train g3rest (init base, steps 12): trained
- load g1rev2+g2nr
- finish: submitted g1rev2+g2nr (token d472a9, job 58)
- finish: confirmed g1rev2+g2nr (token d472a9)
