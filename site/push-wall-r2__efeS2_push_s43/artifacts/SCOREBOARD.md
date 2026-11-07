# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: tinker:Qwen/Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | pw-shap1 | pw-shap2 |
|---|---|---|---|
| metaworldplus-push-wall | 0/20 = 0% | 0/20 = 0% (base 0% = 0.0/20) | 0/5 = 0% (base 0% = 0.0/5) |

GPU-hours: 1.978 spent, 0.022 remaining of 2.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.18, 10 steps 1.32, 50 steps 6.41) GPU-h; eval.py per task (5 seeds 0.02, 20 seeds 0.04, 100 seeds 0.12) GPU-h
Loaded on your serving endpoint: pw-shap1
Submitted: base + pw-shap1 (sha 03b6b6b89555) (turn 22, token 44c02a; unconfirmed; scored at the session end (CAPPED))

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| pw-shap1 | base | 10 | spec1.json | trained |
| pw-shap2 | pw-shap1 | 4 | spec2.json | trained |

## History (latest 30)

- eval base on metaworldplus-push-wall: 0/20
- train pw-shap1 (init base, steps 10): trained
- eval pw-shap1 on metaworldplus-push-wall: 0/20
- train pw-shap2 (init pw-shap1, steps 4): trained
- load pw-shap1
- eval pw-shap2 on metaworldplus-push-wall: 0/5
