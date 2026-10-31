# SCOREBOARD

playbook: nogit-1fa162df
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | l1 |
|---|---|---|
| lift | 67/100 = 67% | 78/100 = 78% (base 67% = 67.0/100) |

GPU-hours: 4.506 spent, 3.494 remaining of 8.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: l1
Submitted: base + l1 (sha 56697bcd0ee9) (turn 14, token 2acf72; confirmed in turn 15)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| l1 | base | 10 | r1_lift10.json | trained |

## History (latest 30)

- train l1 (init base, steps 10): trained
- eval l1 on lift: 78/100
- load l1
- finish: submitted l1 (token 2acf72, job 7)
- finish: confirmed l1 (token 2acf72)
