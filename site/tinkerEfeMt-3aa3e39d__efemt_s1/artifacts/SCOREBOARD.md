# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: tinker:Qwen/Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | A | B |
|---|---|---|---|
| metaworldplus-push-wall | 1/5 = 20% | 3/10 = 30% (base 20% = 2.0/10) | 2/10 = 20% (base 20% = 2.0/10) |
| metaworldplus-pick-place | 1/5 = 20% | 6/10 = 60% (base 20% = 2.0/10) | 7/10 = 70% (base 20% = 2.0/10) |
| metaworldplus-door-lock | 2/5 = 40% | 4/10 = 40% (base 40% = 4.0/10) | 8/10 = 80% (base 40% = 4.0/10) |

GPU-hours: 15.800 spent, 0.200 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.72, 10 steps 6.35, 50 steps 31.35) GPU-h; eval.py per task (5 seeds 0.30, 20 seeds 1.18, 100 seeds 5.82) GPU-h
Loaded on your serving endpoint: B
Submitted: base + B (sha ef9001a51bc2) (turn 25, token 0df9a0; confirmed in turn 28)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| A | base | 6 | specA.json | trained |
| B | A | 6 | specB.json | trained |

## History (latest 30)

- eval base on metaworldplus-push-wall: 1/5
- eval base on metaworldplus-pick-place: 1/5
- eval base on metaworldplus-door-lock: 2/5
- train A (init base, steps 6): trained
- eval A on metaworldplus-push-wall: 3/5
- eval A on metaworldplus-pick-place: 4/5
- eval A on metaworldplus-door-lock: 4/5
- train B (init A, steps 6): trained
- eval B on metaworldplus-push-wall: 2/5
- eval B on metaworldplus-pick-place: 3/5
- eval B on metaworldplus-door-lock: 4/5
- eval A on metaworldplus-push-wall: 3/10
- eval A on metaworldplus-pick-place: 6/10
- eval A on metaworldplus-door-lock: 4/10
- eval B on metaworldplus-push-wall: 7/10
- eval B on metaworldplus-pick-place: 7/10
- eval B on metaworldplus-door-lock: 7/10
- load B
- finish: submitted B (token 0df9a0, job 26)
- eval B on metaworldplus-push-wall: 2/10
- eval B on metaworldplus-pick-place: 7/10
- eval B on metaworldplus-door-lock: 8/10
- finish: confirmed B (token 0df9a0)
