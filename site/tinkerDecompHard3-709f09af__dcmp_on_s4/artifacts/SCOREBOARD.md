# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | r1 | v1 | n1 | pp1 | pp3 | pp1+v1 |
|---|---|---|---|---|---|---|---|
| nut | untested | untested | 0/20 = 0% | untested | untested | untested | 0/20 = 0% |
| restack | untested | 0/20 = 0% | 0/20 = 0% | untested | untested | untested | 0/20 = 0% |
| revstack | untested | untested | 0/20 = 0% | untested | untested | untested | untested |

GPU-hours: 15.971 spent, 0.029 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: pp3+v1
Submitted: base + pp3 (sha ae665504c149) + v1 (sha d09a25ef52ad) (turn 44, token f41d35; confirmed in turn 45)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| r1 | base | 10 | specs/r1.json | trained |
| v1 | base | 10 | specs/v1.json | trained |
| n1 | base | 10 | specs/n1.json | trained |
| pp1 | base | 28 | specs/pp1.json | trained |
| pp3 | base | 19 | specs/pp3.json | trained |

- train job 5 (r1): note set: part of the training prompt only; every eval, including the final score, uses tasks/restack/eval_prompt.txt verbatim
- train job 6 (v1): note set: part of the training prompt only; every eval, including the final score, uses tasks/revstack/eval_prompt.txt verbatim
- train job 10 (n1): note set: part of the training prompt only; every eval, including the final score, uses tasks/nut/eval_prompt.txt verbatim
- train job 12 (pp1): note set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim
- train job 13 (v2): note set: part of the training prompt only; every eval, including the final score, uses tasks/revstack/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- restack: 16 failures in adapters/r1/failures.jsonl; stages none:15 unavailable:1
- revstack: 16 failures in adapters/v1/failures.jsonl; stages unavailable:16
- nut: 16 failures in adapters/n1/failures.jsonl; stages none:16
- restack: 16 failures in adapters/pp1/failures.jsonl; stages none:16
- nut: 16 failures in adapters/pp1/failures.jsonl; stages none:16
- restack: 16 failures in adapters/pp3/failures.jsonl; stages none:15 unstack the green off the red:1
- nut: 16 failures in adapters/pp3/failures.jsonl; stages none:16

## History (latest 30)

- rollout base on nut: 5 seeds -> rollouts/1.jsonl
- rollout base on restack: 5 seeds -> rollouts/2.jsonl
- rollout base on revstack: 5 seeds -> rollouts/3.jsonl
- train r1 (init base, steps 10): trained
- train v1 (init base, steps 10): trained
- eval r1 on restack: 0/20
- eval v1 on revstack: 0/20
- train n1 (init base, steps 10): trained
- train pp1 failed: train: note edit one task's training prompt; a spec naming several tasks cannot set them
- train v2 failed: train: init_mode branch (weights only, fresh optimizer) is not available on this trainer, which restores full state or nothing; use resume, or fresh
- train pp1 (init base, steps 28): trained
- eval v1 on restack: 0/20
- eval pp1+v1 on restack: 0/20
- eval v1 on nut: 0/20
- eval pp1+v1 on nut: 0/20
- train pp3 (init base, steps 19): trained
- load pp3+v1
- finish: submitted pp3+v1 (token f41d35, job 24)
- finish: confirmed pp3+v1 (token f41d35)
