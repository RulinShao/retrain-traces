# SCOREBOARD

playbook: nogit-2bb30ac2
agent: local
mode: dev
dev seeds: from 800001
policy: tinker:Qwen/Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | probe_shaped |
|---|---|---|
| metaworldplus-push-wall | 6/20 = 30% | 9/20 = 45% (base 30% = 6.0/20) |
| metaworldplus-pick-place | 5/20 = 25% | 8/20 = 40% (base 25% = 5.0/20) |
| metaworldplus-door-lock | 7/20 = 35% | 14/20 = 70% (base 35% = 7.0/20) |

GPU-hours: 13.400 spent, 28.250 remaining of 48.0 (1 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.72, 10 steps 6.35, 50 steps 31.35) GPU-h; eval.py per task (5 seeds 0.30, 20 seeds 1.18, 100 seeds 5.82) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)
Job 15 (train success_v1): running, step 5/10, mean reward 0.562, rollouts with reward > 0 0.56, 3.23 GPU-h so far

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| probe_shaped | base | 10 | spec_probe.json | trained |

## History (latest 30)

- eval base on metaworldplus-push-wall: 6/20
- eval base on metaworldplus-pick-place: 5/20
- eval base on metaworldplus-door-lock: 7/20
- train probe_shaped (init base, steps 10): trained
- eval probe_shaped on metaworldplus-push-wall: 9/20
- eval probe_shaped on metaworldplus-pick-place: 8/20
- eval probe_shaped on metaworldplus-door-lock: 14/20
