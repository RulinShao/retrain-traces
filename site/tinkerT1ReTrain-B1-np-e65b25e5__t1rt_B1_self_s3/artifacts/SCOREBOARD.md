# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | m1 | r1 |
|---|---|---|---|
| lift | 13/20 = 65% | 15/20 = 75% (base 65% = 13.0/20) | untested |
| stack | 11/20 = 55% | 10/20 = 50% (base 55% = 11.0/20) | untested |
| wipe | 2/20 = 10% | 14/20 = 70% (base 10% = 2.0/20) | untested |
| nut | 0/20 = 0% | 0/20 = 0% (base 0% = 0.0/20) | untested |
| restack | 0/20 = 0% | 0/20 = 0% (base 0% = 0.0/20) | untested |
| revstack | 0/20 = 0% | untested | 1/20 = 5% (base 0% = 0.0/20) |

GPU-hours: 8.695 spent, 29.847 remaining of 48.0 (3 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.44, 10 steps 2.42, 50 steps 11.23) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| m1 | base | 15 | spec_m1.json | trained |
| r1 | base | 15 | spec_r1.json | trained |

- train job 21 (rs_probe): note set: part of the training prompt only; every eval, including the final score, uses tasks/restack/eval_prompt.txt verbatim

## History (latest 30)

- eval base on lift: 13/20
- eval base on stack: 11/20
- eval base on wipe: 2/20
- eval base on nut: 0/20
- eval base on restack: 0/20
- eval base on revstack: 0/20
- train m1 (init base, steps 15): trained
- train r1 (init base, steps 15): trained
- eval m1 on lift: 15/20
- eval m1 on stack: 10/20
- eval m1 on wipe: 14/20
- eval m1 on nut: 0/20
- eval m1 on restack: 0/20
- eval r1 on revstack: 1/20
- train m2 failed: train: batch 8 does not split equally across 3 tasks ['lift', 'stack', 'wipe']; use a multiple of 3
