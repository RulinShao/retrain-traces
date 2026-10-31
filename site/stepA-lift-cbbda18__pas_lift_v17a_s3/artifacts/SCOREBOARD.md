# SCOREBOARD

playbook: nogit-58e9eacc
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | liftA |
|---|---|---|
| lift | 67/100 = 67% | 77/100 = 77% (base 67% = 67.0/100) |

GPU-hours: 4.506 spent, 0.593 remaining of 8.0 (1 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: liftA
Submitted: base + liftA (sha 4ec215e3daea) (turn 17, token 742645; confirmed in turn 19)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| liftA | base | 10 | spec_liftA.json | trained |

## History (latest 30)

- train liftA (init base, steps 10): trained
- eval liftA on lift: 77/100
- load liftA
- finish: submitted liftA (token 742645, job 10)
- finish: confirmed liftA (token 742645)
