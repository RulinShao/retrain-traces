# SCOREBOARD

playbook: 3246dddf-df764206
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | p1_nr | p2_rvs | p3_rvs | p3_nr | p4_rvs | p3_rvs+p3_nr | p4_rvs+p3_nr |
|---|---|---|---|---|---|---|---|---|
| nut | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) | untested | untested | untested | untested | untested | untested |
| restack | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) | untested | untested | untested | untested | 0/100 = 0% (base 0% = 0.0/100) | untested |
| revstack | 1/100 = 1% | untested | 0/100 = 0% (base 1% = 1.0/100) | 2/100 = 2% (base 1% = 1.0/100) | untested | untested | 4/100 = 4% (base 1% = 1.0/100) | 1/100 = 1% (base 1% = 1.0/100) |

GPU-hours: 15.190 spent, 0.810 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: p3_rvs+p3_nr
Submitted: base + p3_rvs (sha 0178f9ccf799) + p3_nr (sha fad992952ae3) (turn 26, token dfa470; confirmed in turn 27)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| p1_nr | base | 10 | spec_p1.json | trained |
| p2_rvs | base | 10 | spec_p2.json | trained |
| p3_rvs | p2_rvs | 15 | spec_p3rvs.json | trained |
| p3_nr | p1_nr | 12 | spec_p3nr.json | trained |
| p4_rvs | p3_rvs | 12 | spec_p4rvs.json | trained |

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- nut: 16 failures in adapters/p1_nr/failures.jsonl; stages none:16
- restack: 16 failures in adapters/p1_nr/failures.jsonl; stages none:15 unstack the green off the red:1
- revstack: 16 failures in adapters/p2_rvs/failures.jsonl; stages none:13 grasp the green_cube:2 lift the green_cube:1
- revstack: 16 failures in adapters/p3_rvs/failures.jsonl; stages none:12 lift the green_cube:3 grasp the green_cube:1
- restack: 16 failures in adapters/p3_nr/failures.jsonl; stages none:16
- revstack: 16 failures in adapters/p4_rvs/failures.jsonl; stages grasp the green_cube:8 none:5 reach the green_cube:3

## Magic ladder (DEV practice; oracle rows: upper bound / doability, counts only)

- ladder restack (policy suffix) over seeds 800025-800032: k=0 grasp 0/8
- ladder restack (oracle suffix, upper bound / doability) over seeds 800025-800032: k=0 grasp 8/8
- ladder revstack (policy suffix) over seeds 800033-800040: k=0 grasp 0/8
- ladder revstack (oracle suffix, upper bound / doability) over seeds 800033-800040: k=0 grasp 8/8
- ladder nut (policy suffix) over seeds 800041-800048: k=0 grasp 0/8
- ladder nut (oracle suffix, upper bound / doability) over seeds 800041-800048: k=0 grasp 8/8

## History (latest 30)

- rollout base on restack: 8 seeds -> rollouts/1.jsonl; stages reached: unstack the green off the red 5/8, grasp the red 0/8, lift the red 0/8, align the red over the green 0/8, place the red on the green 0/8; distinct values over 8 rows: task_completed 1, sim_reward 8, stage unstack the green off the red 2, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1
- rollout base on revstack: 8 seeds -> rollouts/2.jsonl; stages reached: reach the green_cube 7/8, grasp the green_cube 5/8, lift the green_cube 1/8, align the green_cube over the red_cube 0/8, place the green_cube on the red_cube 0/8; distinct values over 8 rows: task_completed 1, sim_reward 8, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 1, stage place the green_cube on the red_cube 1
- rollout base on nut: 8 seeds -> rollouts/3.jsonl; stages reached: reach the handle 0/8, grasp the nut 0/8, align the nut over the peg 0/8, insert the nut 0/8; distinct values over 8 rows: task_completed 1, sim_reward 2, stage reach the handle 1, stage grasp the nut 1, stage align the nut over the peg 1, stage insert the nut 1
- rollout base on restack: 8 seeds -> rollouts/5.jsonl; stages reached: unstack the green off the red 8/8, grasp the red 8/8, lift the red 0/8, align the red over the green 0/8, place the red on the green 0/8; distinct values over 8 rows: task_completed 1, sim_reward 1, stage unstack the green off the red 1, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1; magic prefix:grasp the red 0/8, valid 8/8; ladder restack: k=0 grasp 0/8 (policy suffix, valid 8/8); ladder restack (policy suffix) over seeds 800025-800032: k=0 grasp 0/8
- ladder restack: k=0 grasp 8/8 (oracle suffix, upper bound / doability, valid 8/8); ladder restack (oracle suffix, upper bound / doability) over seeds 800025-800032: k=0 grasp 8/8
- rollout base on revstack: 8 seeds -> rollouts/7.jsonl; stages reached: reach the green_cube 8/8, grasp the green_cube 8/8, lift the green_cube 0/8, align the green_cube over the red_cube 0/8, place the green_cube on the red_cube 0/8; distinct values over 8 rows: task_completed 1, sim_reward 1, stage reach the green_cube 1, stage grasp the green_cube 1, stage lift the green_cube 1, stage align the green_cube over the red_cube 1, stage place the green_cube on the red_cube 1; magic prefix:grasp the green_cube 0/8, valid 8/8; ladder revstack: k=0 grasp 0/8 (policy suffix, valid 8/8); ladder revstack (policy suffix) over seeds 800033-800040: k=0 grasp 0/8
- ladder revstack: k=0 grasp 8/8 (oracle suffix, upper bound / doability, valid 8/8); ladder revstack (oracle suffix, upper bound / doability) over seeds 800033-800040: k=0 grasp 8/8
- rollout base on nut: 8 seeds -> rollouts/9.jsonl; stages reached: reach the handle 8/8, grasp the nut 8/8, align the nut over the peg 0/8, insert the nut 0/8; distinct values over 8 rows: task_completed 1, sim_reward 5, stage reach the handle 1, stage grasp the nut 1, stage align the nut over the peg 1, stage insert the nut 1; magic prefix:grasp the nut 0/8, valid 8/8; ladder nut: k=0 grasp 0/8 (policy suffix, valid 8/8); ladder nut (policy suffix) over seeds 800041-800048: k=0 grasp 0/8
- ladder nut: k=0 grasp 8/8 (oracle suffix, upper bound / doability, valid 8/8); ladder nut (oracle suffix, upper bound / doability) over seeds 800041-800048: k=0 grasp 8/8
- train p1_nr (init base, steps 10): trained
- train p2_rvs (init base, steps 10): trained
- eval p1_nr on restack: 0/100
- eval p1_nr on nut: 0/100
- eval p2_rvs on revstack: 0/100
- cancel job 18
- cancel job 19
- cancel job 20
- eval p1_nr+p2_rvs cancelled: eval cancelled; charged 0.000 GPU-h
- eval p1_nr+p2_rvs cancelled: eval cancelled; charged 0.000 GPU-h
- eval p1_nr+p2_rvs cancelled: eval cancelled; charged 0.000 GPU-h
- train p3_rvs (init p2_rvs, steps 15): trained
- train p3_nr (init p1_nr, steps 12): trained
- eval p3_rvs on revstack: 2/100
- eval p3_rvs+p3_nr on revstack: 4/100
- eval p3_rvs+p3_nr on restack: 0/100
- train p4_rvs (init p3_rvs, steps 12): trained
- eval p4_rvs+p3_nr on revstack: 1/100
- load p3_rvs+p3_nr
- finish: submitted p3_rvs+p3_nr (token dfa470, job 37)
- finish: confirmed p3_rvs+p3_nr (token dfa470)
