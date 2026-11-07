# SCOREBOARD

playbook: none
agent: scripted:e2e-rl-uniform
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | e2e_c1 |
|---|---|---|
| stack | untested | untested |

GPU-hours: 2.203 spent, 5.797 remaining of 8.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: e2e_c1
Submitted: base + e2e_c1 (sha 85d955294cd8) (turn 3, token 107d9f; confirmed in turn 4)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| e2e_c1 | base | 38 | specs/e2e_c1.json | trained |

## History (latest 30)

- train e2e_c1 (init base, steps 38): trained
- load e2e_c1
- finish: submitted e2e_c1 (token 107d9f, job 4)
- finish: confirmed e2e_c1 (token 107d9f)
