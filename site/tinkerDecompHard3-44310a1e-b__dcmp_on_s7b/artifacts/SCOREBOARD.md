# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | g1 | g2 |
|---|---|---|---|
| nut | 0/100 = 0% | 0/20 = 0% (base 0% = 0.0/20) | 0/20 = 0% (base 0% = 0.0/20) |
| restack | 0/100 = 0% | 0/20 = 0% (base 0% = 0.0/20) | 0/20 = 0% (base 0% = 0.0/20) |
| revstack | 1/100 = 1% | untested | 1/20 = 5% (base 1% = 0.2/20) |

GPU-hours: 4.626 spent, 11.374 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| g1 | base | 18 | spec_g1.json | trained |
| g2 | base | 10 | spec_g2.json | trained |

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- nut: 16 failures in adapters/g1/failures.jsonl; stages none:16
- restack: 16 failures in adapters/g1/failures.jsonl; stages none:15 unstack the green off the red:1
- revstack: 16 failures in adapters/g2/failures.jsonl; stages unavailable:16

## History (latest 30)

- rollout base on restack: 5 seeds -> rollouts/1.jsonl
- rollout base on revstack: 5 seeds -> rollouts/2.jsonl
- rollout base on nut: 5 seeds -> rollouts/3.jsonl
- train g1 (init base, steps 18): trained
- train g2 (init base, steps 10): trained
- eval g1 on nut: 0/20
- eval g1 on restack: 0/20
- eval g2 on restack: 0/20
- eval g2 on revstack: 1/20
- eval g2 on nut: 0/20
- train g4 failed: train: init adapter not found: …/adapters/g3
- train g3 failed: train: init_mode branch (weights only, fresh optimizer) is not available on this trainer, which restores full state or nothing; use resume, or fresh
