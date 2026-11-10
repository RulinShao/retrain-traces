# SCOREBOARD

playbook: nogit-db86b5a3
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | g2b | g3a | g4r | g5r | g6s | g7s | g8 | g9 |
|---|---|---|---|---|---|---|---|---|---|
| nut | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) | untested |
| restack | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) | untested |
| revstack | 1/100 = 1% | 6/100 = 6% (base 1% = 1.0/100) | 12/100 = 12% (base 1% = 1.0/100) | 10/100 = 10% (base 1% = 1.0/100) | 11/100 = 11% (base 1% = 1.0/100) | 0/100 = 0% (base 1% = 1.0/100) | 3/100 = 3% (base 1% = 1.0/100) | 23/100 = 23% (base 1% = 1.0/100) | 22/100 = 22% (base 1% = 1.0/100) |
| restack_tail (unit of restack) | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| nut_tail (unit of nut) | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| restack_tail2 (unit of restack) | untested | untested | untested | untested | untested | untested | untested | untested | untested |

GPU-hours: 45.629 spent, 2.371 remaining of 48.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: g8
Submitted: base + g8 (sha 6e6a72c3fb9e) (turn 57, token 91c474; confirmed in turn 58)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| g2b | preset | None | preset (operator) | trained |
| g3a | g2b | 60 | spec_g3a.json | trained |
| g4r | g3a | 40 | spec_g4r.json | trained |
| g5r | g3a | 40 | spec_g5r.json | trained |
| g6s | g3a | None | spec_g6s.json | trained |
| g7s | g3a | None | spec_g7s.json | trained |
| g8 | g3a | 40 | spec_g8.json | trained |
| g9 | g8 | 25 | spec_g9.json | trained |

- train job 47 (g6s): prompt in 96 data row(s) set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim
- train job 55 (g7s): prompt in 120 data row(s) set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- job 22: rollout g3a on nut: 8 seeds -> rollouts/22.jsonl; self-reward mean 0.0 over 8 seeds (rewards/staged_g2b.py); stages reached: reach the handle 0/8, grasp the nut 0/8, align the nut over the peg 0/8, insert the nut 0/8; distinct values over 8 rows: task_completed 1, sim_reward 4, stage reach the handle 1, stage grasp the nut 1, stage align the nut over the peg 1, stage insert the nut 1
- job 34: rollout g3a on restack: 32 seeds -> rollouts/34.jsonl; self-reward mean 0.0 over 32 seeds (rewards/staged_g2b.py); stages reached: unstack the green off the red 32/32, grasp the red 32/32, lift the red 32/32, align the red over the green 2/32, place the red on the green 0/32; distinct values over 32 rows: task_completed 1, sim_reward 30, stage unstack the green off the red 1, stage grasp the red 1, stage lift the red 1, stage align the red over the green 2, stage place the red on the green 1; magic prefix:grasp the red 0/32, valid 32/32
- job 35: rollout g3a on nut: 32 seeds -> rollouts/35.jsonl; self-reward mean 0.0 over 32 seeds (rewards/staged_g2b.py); stages reached: no stages recorded; distinct values over 32 rows: task_completed 1, sim_reward 1; magic prefix:grasp the nut 0/32, valid 0/32
- job 38: rollout g3a on restack_tail2: 8 seeds -> rollouts/38.jsonl; self-reward mean 0.0 over 8 seeds (rewards/staged_g2b.py); stages reached: unstack the green off the red 0/8, grasp the red 0/8, lift the red 0/8, align the red over the green 0/8, place the red on the green 0/8; distinct values over 8 rows: task_completed 1, sim_reward 8, stage unstack the green off the red 1, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1
- job 39: rollout g3a on restack_tail: 8 seeds -> rollouts/39.jsonl; self-reward mean 0.0 over 8 seeds (rewards/staged_g2b.py); stages reached: unstack the green off the red 0/8, grasp the red 0/8, lift the red 0/8, align the red over the green 0/8, place the red on the green 0/8; distinct values over 8 rows: task_completed 1, sim_reward 1, stage unstack the green off the red 1, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- revstack: 16 failures in adapters/g3a/failures.jsonl; stages none:10 grasp the green_cube:4 lift the green_cube:1 reach the green_cube:1
- restack: 16 failures in adapters/g4r/failures.jsonl; stages unstack the green off the red:8 none:7 align the red over the green:1
- restack: 16 failures in adapters/g5r/failures.jsonl; stages none:11 unstack the green off the red:5
- revstack: 16 failures in adapters/g8/failures.jsonl; stages grasp the green_cube:6 reach the green_cube:6 lift the green_cube:2 none:2
- revstack: 16 failures in adapters/g9/failures.jsonl; stages none:13 grasp the green_cube:2 reach the green_cube:1

## Magic ladder (DEV practice; oracle rows: upper bound / doability, counts only)

- ladder restack (oracle suffix, upper bound / doability) over seeds 800901-800908: k=0 grasp 8/8
- ladder restack (policy suffix) over seeds 800901-800908: k=0 grasp 0/8
- ladder nut (oracle suffix, upper bound / doability) over seeds 800909-800916: k=0 grasp 8/8
- ladder nut (policy suffix) over seeds 800909-800916: k=0 grasp 0/8

## History (latest 30)

- unit restack_tail registered on restack (privileged practice (magic))
- unit nut_tail registered on nut (privileged practice (magic))
- rollout g3a on restack: 32 seeds -> rollouts/34.jsonl; self-reward mean 0.0 over 32 seeds (rewards/staged_g2b.py); stages reached: unstack the green off the red 32/32, grasp the red 32/32, lift the red 32/32, align the red over the green 2/32, place the red on the green 0/32; distinct values over 32 rows: task_completed 1, sim_reward 30, stage unstack the green off the red 1, stage grasp the red 1, stage lift the red 1, stage align the red over the green 2, stage place the red on the green 1; magic prefix:grasp the red 0/32, valid 32/32
- rollout g3a on nut: 32 seeds -> rollouts/35.jsonl; self-reward mean 0.0 over 32 seeds (rewards/staged_g2b.py); stages reached: no stages recorded; distinct values over 32 rows: task_completed 1, sim_reward 1; magic prefix:grasp the nut 0/32, valid 0/32
- unit restack_tail2 registered on restack (privileged practice (magic))
- rollout g3a on restack_tail2: 8 seeds -> rollouts/38.jsonl; self-reward mean 0.0 over 8 seeds (rewards/staged_g2b.py); stages reached: unstack the green off the red 0/8, grasp the red 0/8, lift the red 0/8, align the red over the green 0/8, place the red on the green 0/8; distinct values over 8 rows: task_completed 1, sim_reward 8, stage unstack the green off the red 1, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1
- rollout g3a on restack_tail: 8 seeds -> rollouts/39.jsonl; self-reward mean 0.0 over 8 seeds (rewards/staged_g2b.py); stages reached: unstack the green off the red 0/8, grasp the red 0/8, lift the red 0/8, align the red over the green 0/8, place the red on the green 0/8; distinct values over 8 rows: task_completed 1, sim_reward 1, stage unstack the green off the red 1, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1
- train g5r (init g3a, steps 40): trained
- eval g5r on restack: 0/100
- eval g5r on revstack: 11/100
- eval g5r on nut: 0/100
- train g6s (init g3a, steps None): trained
- eval g6s on restack: 0/100
- eval g6s on revstack: 0/100
- eval g6s on nut: 0/100
- rollout g6s on revstack: 4 seeds -> rollouts/53.jsonl; stages reached: reach the green_cube 2/4, grasp the green_cube 1/4, lift the green_cube 1/4, align the green_cube over the red_cube 1/4, place the green_cube on the red_cube 1/4; distinct values over 4 rows: task_completed 2, sim_reward 4, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 2, stage place the green_cube on the red_cube 2
- train g7s (init g3a, steps None): trained
- eval g7s on revstack: 3/100
- eval g7s on restack: 0/100
- eval g7s on nut: 0/100
- train g8 failed: train: init_mode branch (weights only, fresh optimizer) is not available on this trainer, which restores full state or nothing; use resume, or fresh
- train g8 (init g3a, steps 40): trained
- eval g8 on revstack: 23/100
- eval g8 on restack: 0/100
- eval g8 on nut: 0/100
- train g9 (init g8, steps 25): trained
- eval g9 on revstack: 22/100
- load g8
- finish: submitted g8 (token 91c474, job 74)
- finish: confirmed g8 (token 91c474)
