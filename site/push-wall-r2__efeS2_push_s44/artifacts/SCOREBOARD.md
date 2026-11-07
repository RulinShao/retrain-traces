# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: tinker:Qwen/Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | pw-sh1 | pw-sh2 |
|---|---|---|---|
| metaworldplus-push-wall | 0/20 = 0% | 0/20 = 0% (base 0% = 0.0/20) | 1/20 = 5% (base 0% = 0.0/20) |

GPU-hours: 1.993 spent, 0.007 remaining of 2.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.18, 10 steps 1.32, 50 steps 6.41) GPU-h; eval.py per task (5 seeds 0.02, 20 seeds 0.04, 100 seeds 0.12) GPU-h
Loaded on your serving endpoint: pw-sh2
Submitted: base + pw-sh2 (sha 5eba1d37ef1f) (turn 16, token 3272cf; confirmed in turn 17)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| pw-sh1 | base | 10 | train1.yaml | trained |
| pw-sh2 | pw-sh1 | 4 | train2.yaml | trained |

## History (latest 30)

- eval base on metaworldplus-push-wall: 0/20
- train pw-sh1 (init base, steps 10): trained
- eval pw-sh1 on metaworldplus-push-wall: 0/20
- train pw-sh2 (init pw-sh1, steps 4): trained
- eval pw-sh2 on metaworldplus-push-wall: 1/20
- load pw-sh2
- finish: submitted pw-sh2 (token 3272cf, job 11)
- finish: confirmed pw-sh2 (token 3272cf)
