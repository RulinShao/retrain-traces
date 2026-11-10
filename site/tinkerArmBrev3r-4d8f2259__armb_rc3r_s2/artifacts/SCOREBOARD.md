# SCOREBOARD

playbook: 3246dddf-df764206
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | rc_a_t1 | rc_a_t3 | rc_full_t1 | rc_rev_t1 | rc_rev_t2 |
|---|---|---|---|---|---|---|
| nut | 0/100 = 0% | untested | untested | untested | untested | untested |
| restack | 0/100 = 0% | 0/20 = 0% (base 0% = 0.0/20) | untested | 0/50 = 0% (base 0% = 0.0/50) | 0/20 = 0% (base 0% = 0.0/20) | 0/20 = 0% (base 0% = 0.0/20) |
| revstack | 1/100 = 1% | untested | untested | 0/50 = 0% (base 1% = 0.5/50) | 2/30 = 7% (base 1% = 0.3/30) | 1/30 = 3% (base 1% = 0.3/30) |
| rc_align_u (unit of restack) | untested | untested | untested | untested | untested | untested |
| rc_a1 (unit of restack) | untested | untested | untested | untested | untested | untested |
| rc_l1 (unit of restack) | untested | untested | untested | untested | untested | untested |
| rc_a_dense (unit of restack) | untested | untested | untested | untested | untested | untested |
| rc_a2 (unit of restack) | untested | untested | untested | untested | untested | untested |

GPU-hours: 14.267 spent, 1.733 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: rc_rev_t1
Submitted: base + rc_rev_t1 (sha 284e5317bf7b) (turn 54, token b22128; confirmed in turn 56)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| rc_a_t1 | base | 10 | spec_rc_a.json | trained |
| rc_a_t3 | rc_a_t1 | 12 | spec_rc_a2.json | trained |
| rc_full_t1 | rc_a_t3 | 14 | spec_rc_full1.json | trained |
| rc_rev_t1 | base | 12 | spec_rev1.json | trained |
| rc_rev_t2 | rc_rev_t1 | 14 | spec_rev2.json | trained |

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- restack: 16 failures in adapters/rc_a_t1/failures.jsonl; stages unstack the green off the red:12 align the red over the green:2 grasp the red:1 lift the red:1
- restack: 16 failures in adapters/rc_a_t3/failures.jsonl; stages unstack the green off the red:7 align the red over the green:5 grasp the red:2 lift the red:2
- restack: 16 failures in adapters/rc_full_t1/failures.jsonl; stages none:14 unstack the green off the red:2
- revstack: 16 failures in adapters/rc_rev_t1/failures.jsonl; stages reach the green_cube:7 grasp the green_cube:6 none:3
- revstack: 16 failures in adapters/rc_rev_t2/failures.jsonl; stages grasp the green_cube:7 none:7 reach the green_cube:2

## Magic ladder (DEV practice; oracle rows: upper bound / doability, counts only)

- ladder restack (oracle suffix, upper bound / doability) over seeds 800009-800016: k=2 align 8/8
- ladder restack (policy suffix) over seeds 800009-800016: k=1 lift 0/8, k=2 align 0/8; no jump of 25% or more between measured cuts
- ladder revstack (policy suffix) over seeds 800145-800148: k=1 lift 0/4

## History (latest 30)

- rollout base on restack: 8 seeds -> rollouts/1.jsonl; stages reached: unstack the green off the red 6/8, grasp the red 0/8, lift the red 0/8, align the red over the green 0/8, place the red on the green 0/8; distinct values over 8 rows: task_completed 1, sim_reward 8, stage unstack the green off the red 2, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1
- ladder restack: k=2 align 8/8 (oracle suffix, upper bound / doability, valid 8/8); ladder restack (oracle suffix, upper bound / doability) over seeds 800009-800016: k=2 align 8/8
- rollout base on restack: 8 seeds -> rollouts/7.jsonl; stages reached: unstack the green off the red 8/8, grasp the red 8/8, lift the red 8/8, align the red over the green 8/8, place the red on the green 0/8; distinct values over 8 rows: task_completed 1, sim_reward 6, stage unstack the green off the red 1, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1; magic prefix:align the red over the green 0/8, valid 8/8; ladder restack: k=2 align 0/8 (policy suffix, valid 8/8); ladder restack (policy suffix) over seeds 800009-800016: k=2 align 0/8
- unit rc_align_u registered on restack (privileged practice (magic))
- rollout base on restack: 8 seeds -> rollouts/9.jsonl; stages reached: unstack the green off the red 8/8, grasp the red 8/8, lift the red 8/8, align the red over the green 0/8, place the red on the green 0/8; distinct values over 8 rows: task_completed 1, sim_reward 6, stage unstack the green off the red 1, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1; magic prefix:lift the red 0/8, valid 8/8; ladder restack: k=1 lift 0/8 (policy suffix, valid 8/8); ladder restack (policy suffix) over seeds 800009-800016: k=1 lift 0/8, k=2 align 0/8; no jump of 25% or more between measured cuts
- unit rc_a1 registered on restack (privileged practice (magic))
- unit rc_l1 registered on restack (privileged practice (magic))
- unit rc_a_dense registered on restack (privileged practice (magic))
- unit rc_a2 registered on restack (privileged practice (magic))
- train rc_a_t1 (init base, steps 10): trained
- eval rc_a_t1 on restack: 0/20
- rollout rc_a_t1 on restack: 8 seeds -> rollouts/27.jsonl; stages reached: unstack the green off the red 8/8, grasp the red 8/8, lift the red 8/8, align the red over the green 8/8, place the red on the green 0/8; distinct values over 8 rows: task_completed 1, sim_reward 8, stage unstack the green off the red 1, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1; magic prefix:align the red over the green 0/8, valid 8/8; ladder restack: k=2 align 0/8 (policy suffix, valid 8/8); ladder restack (policy suffix) over seeds 800009-800016: k=1 lift 0/8, k=2 align 0/8; no jump of 25% or more between measured cuts
- train rc_a_t2 failed: train: init_mode branch (weights only, fresh optimizer) is not available on this trainer, which restores full state or nothing; use resume, or fresh
- train rc_a_t3 (init rc_a_t1, steps 12): trained
- rollout rc_a_t3 on restack: 8 seeds -> rollouts/33.jsonl; stages reached: unstack the green off the red 8/8, grasp the red 8/8, lift the red 8/8, align the red over the green 8/8, place the red on the green 0/8; distinct values over 8 rows: task_completed 1, sim_reward 8, stage unstack the green off the red 1, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1; magic prefix:align the red over the green 0/8, valid 8/8; ladder restack: k=2 align 0/8 (policy suffix, valid 8/8); ladder restack (policy suffix) over seeds 800009-800016: k=1 lift 0/8, k=2 align 0/8; no jump of 25% or more between measured cuts
- train rc_full_t1 (init rc_a_t3, steps 14): trained
- train rc_sft1 failed: train: objective '…/workspace/sft': this site trains with objective 'grpo' only
- eval rc_full_t1 on restack: 0/50
- eval rc_full_t1 on revstack: 0/50
- rollout base on revstack: 8 seeds -> rollouts/43.jsonl; stages reached: reach the green_cube 6/8, grasp the green_cube 2/8, lift the green_cube 0/8, align the green_cube over the red_cube 0/8, place the green_cube on the red_cube 0/8; distinct values over 8 rows: task_completed 1, sim_reward 8, stage reach the green_cube 2, stage grasp the green_cube 2, stage lift the green_cube 1, stage align the green_cube over the red_cube 1, stage place the green_cube on the red_cube 1
- rollout base on revstack: 4 seeds -> rollouts/45.jsonl; stages reached: reach the green_cube 4/4, grasp the green_cube 4/4, lift the green_cube 4/4, align the green_cube over the red_cube 0/4, place the green_cube on the red_cube 0/4; distinct values over 4 rows: task_completed 1, sim_reward 3, stage reach the green_cube 1, stage grasp the green_cube 1, stage lift the green_cube 1, stage align the green_cube over the red_cube 1, stage place the green_cube on the red_cube 1; magic prefix:lift the green_cube 0/4, valid 4/4; ladder revstack: k=1 lift 0/4 (policy suffix, valid 4/4); ladder revstack (policy suffix) over seeds 800145-800148: k=1 lift 0/4
- train rc_rev_t1 (init base, steps 12): trained
- eval rc_rev_t1 on revstack: 2/30
- eval rc_rev_t1 on restack: 0/20
- load rc_rev_t1
- train rc_rev_t2 (init rc_rev_t1, steps 14): trained
- eval rc_rev_t2 on revstack: 1/30
- eval rc_rev_t2 on restack: 0/20
- finish: submitted rc_rev_t1 (token b22128, job 61)
- finish: confirmed rc_rev_t1 (token b22128)
