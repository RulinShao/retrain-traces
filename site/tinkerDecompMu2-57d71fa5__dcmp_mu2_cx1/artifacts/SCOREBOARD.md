# SCOREBOARD

playbook: none
agent: codex:gpt-6-astra
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | joint10 | rev20 | rev_sft |
|---|---|---|---|---|
| nut | untested | untested | 0/40 = 0% | untested |
| restack | untested | untested | 0/40 = 0% | untested |
| revstack | untested | untested | 3/40 = 8% | untested |

GPU-hours: 8.276 spent, 7.724 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| joint10 | base | 10 | joint10.json | trained 10 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| rev20 | base | 20 | rev20.json | trained |
| rev_sft | rev20 | None | rev_sft.json | trained |

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- nut: 16 failures in adapters/joint10/failures.jsonl; stages none:16
- restack: 16 failures in adapters/joint10/failures.jsonl; stages none:16
- revstack: 16 failures in adapters/rev20/failures.jsonl; stages none:14 grasp the green_cube:2

## Magic ladder (DEV practice; oracle rows: upper bound / doability, counts only)

- ladder revstack (policy suffix) over seeds 800061-800065: k=2 align 0/5
- ladder revstack (oracle suffix, upper bound / doability) over seeds 800061-800065: k=2 align 4/5
- ladder restack (policy suffix) over seeds 800066-800070: k=2 align 0/5
- ladder restack (oracle suffix, upper bound / doability) over seeds 800066-800070: k=2 align 5/5
- ladder nut (policy suffix) over seeds 800071-800075: k=2 align 1/5
- ladder nut (oracle suffix, upper bound / doability) over seeds 800071-800075: k=2 align 5/5

## History (latest 30)

- rollout base on nut: 20 seeds -> rollouts/1.jsonl; stages reached: reach the handle 1/20, grasp the nut 1/20, align the nut over the peg 0/20, insert the nut 0/20; distinct values over 20 rows: task_completed 1, sim_reward 8, stage reach the handle 2, stage grasp the nut 2, stage align the nut over the peg 1, stage insert the nut 1
- rollout base on restack: 20 seeds -> rollouts/2.jsonl; stages reached: unstack the green off the red 13/20, grasp the red 0/20, lift the red 0/20, align the red over the green 1/20, place the red on the green 0/20; distinct values over 20 rows: task_completed 1, sim_reward 17, stage unstack the green off the red 2, stage grasp the red 1, stage lift the red 1, stage align the red over the green 2, stage place the red on the green 1
- rollout base on revstack: 20 seeds -> rollouts/3.jsonl; stages reached: reach the green_cube 17/20, grasp the green_cube 12/20, lift the green_cube 2/20, align the green_cube over the red_cube 1/20, place the green_cube on the red_cube 0/20; distinct values over 20 rows: task_completed 1, sim_reward 19, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 2, stage place the green_cube on the red_cube 1
- train joint10 (init base, steps 10): trained 10 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- rollout base on revstack: 5 seeds -> rollouts/7.jsonl; stages reached: reach the green_cube 4/5, grasp the green_cube 4/5, lift the green_cube 4/5, align the green_cube over the red_cube 4/5, place the green_cube on the red_cube 0/5; distinct values over 5 rows: task_completed 1, sim_reward 5, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 2, stage align the green_cube over the red_cube 2, stage place the green_cube on the red_cube 1; magic prefix:align the green_cube over the red_cube 0/5, valid 4/5; ladder revstack: k=2 align 0/5 (policy suffix, valid 4/5); ladder revstack (policy suffix) over seeds 800061-800065: k=2 align 0/5
- ladder revstack: k=2 align 4/5 (oracle suffix, upper bound / doability, valid 4/5); ladder revstack (oracle suffix, upper bound / doability) over seeds 800061-800065: k=2 align 4/5
- rollout base on restack: 5 seeds -> rollouts/9.jsonl; stages reached: unstack the green off the red 5/5, grasp the red 5/5, lift the red 5/5, align the red over the green 5/5, place the red on the green 0/5; distinct values over 5 rows: task_completed 1, sim_reward 3, stage unstack the green off the red 1, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1; magic prefix:align the red over the green 0/5, valid 5/5; ladder restack: k=2 align 0/5 (policy suffix, valid 5/5); ladder restack (policy suffix) over seeds 800066-800070: k=2 align 0/5
- ladder restack: k=2 align 5/5 (oracle suffix, upper bound / doability, valid 5/5); ladder restack (oracle suffix, upper bound / doability) over seeds 800066-800070: k=2 align 5/5
- rollout base on nut: 5 seeds -> rollouts/11.jsonl; stages reached: reach the handle 5/5, grasp the nut 5/5, align the nut over the peg 5/5, insert the nut 1/5; distinct values over 5 rows: task_completed 2, sim_reward 2, stage reach the handle 1, stage grasp the nut 1, stage align the nut over the peg 1, stage insert the nut 2; magic prefix:align the nut over the peg 1/5, valid 5/5; ladder nut: k=2 align 1/5 (policy suffix, valid 5/5); ladder nut (policy suffix) over seeds 800071-800075: k=2 align 1/5
- ladder nut: k=2 align 5/5 (oracle suffix, upper bound / doability, valid 5/5); ladder nut (oracle suffix, upper bound / doability) over seeds 800071-800075: k=2 align 5/5
- train rev20 (init base, steps 20): trained
- eval rev20 on nut: 0/40
- train rev_sft (init rev20, steps None): trained
- eval rev20 on revstack: 3/40
- eval rev20 on restack: 0/40
