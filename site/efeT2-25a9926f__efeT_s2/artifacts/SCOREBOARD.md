# SCOREBOARD

playbook: nogit-2bb30ac2
agent: local
mode: dev
dev seeds: from 800001
policy: tinker:Qwen/Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | pw10 | mt15 |
|---|---|---|---|
| metaworldplus-push-wall | 3/20 = 15% | 7/20 = 35% (base 15% = 3.0/20) | 5/20 = 25% (base 15% = 3.0/20) |
| metaworldplus-pick-place | 7/20 = 35% | 10/20 = 50% (base 35% = 7.0/20) | 13/20 = 65% (base 35% = 7.0/20) |
| metaworldplus-door-lock | 10/20 = 50% | 16/20 = 80% (base 50% = 10.0/20) | 12/20 = 60% (base 50% = 10.0/20) |

GPU-hours: 24.056 spent, 16.813 remaining of 48.0 (1 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.72, 10 steps 6.35, 50 steps 31.35) GPU-h; eval.py per task (5 seeds 0.30, 20 seeds 1.18, 100 seeds 5.82) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)
Job 17 (train mt25): queued (not started), 0 min in queue

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| pw10 | base | 10 | spec1.json | trained |
| mt15 | base | 15 | spec2.json | trained |

## History (latest 30)

- eval base on metaworldplus-push-wall: 3/20
- eval base on metaworldplus-pick-place: 7/20
- eval base on metaworldplus-door-lock: 10/20
- train pw10 (init base, steps 10): trained
- train mt15 (init base, steps 15): trained
- eval pw10 on metaworldplus-push-wall: 7/20
- eval pw10 on metaworldplus-pick-place: 10/20
- eval pw10 on metaworldplus-door-lock: 16/20
- eval mt15 on metaworldplus-push-wall: 5/20
- eval mt15 on metaworldplus-pick-place: 13/20
- eval mt15 on metaworldplus-door-lock: 12/20
