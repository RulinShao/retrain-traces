# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | multi1 | rev1 |
|---|---|---|---|
| lift | 13/20 = 65% | 16/20 = 80% (base 65% = 13.0/20) | untested |
| stack | 11/20 = 55% | 11/20 = 55% (base 55% = 11.0/20) | untested |
| wipe | 2/20 = 10% | 17/20 = 85% (base 10% = 2.0/20) | untested |
| nut | 0/20 = 0% | 0/20 = 0% (base 0% = 0.0/20) | untested |
| restack | 0/20 = 0% | 0/20 = 0% (base 0% = 0.0/20) | untested |
| revstack | 0/20 = 0% | untested | 1/20 = 5% (base 0% = 0.0/20) |

GPU-hours: 14.641 spent, 19.492 remaining of 48.0 (2 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.44, 10 steps 2.42, 50 steps 11.23) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| multi1 | base | 30 | spec_multi.json | trained |
| rev1 | base | 30 | spec_rev.json | trained |

## History (latest 30)

- eval base on lift: 13/20
- eval base on stack: 11/20
- eval base on wipe: 2/20
- eval base on nut: 0/20
- eval base on restack: 0/20
- eval base on revstack: 0/20
- train multi1 (init base, steps 30): trained
- train rev1 (init base, steps 30): trained
- eval multi1 on lift: 16/20
- eval multi1 on stack: 11/20
- eval multi1 on restack: 0/20
- eval multi1 on wipe: 17/20
- eval multi1 on nut: 0/20
- eval rev1 on revstack: 1/20
- train mega3 failed: train: batch 12 does not split equally across 5 tasks ['lift', 'stack', 'restack', 'wipe', 'nut']; use a multiple of 5
