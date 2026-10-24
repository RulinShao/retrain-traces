# SCOREBOARD

playbook: ea39163-15ab3e1e
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | lift_a1 | stack_a1 | lift_a1+stack_a1 |
|---|---|---|---|---|
| lift | 67/100 = 67% | 88/100 = 88% (base 67% = 67.0/100) | untested | 88/100 = 88% (base 67% = 67.0/100) |
| stack | 51/100 = 51% | 33/100 = 33% (base 51% = 51.0/100) | untested | 65/100 = 65% (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |
| wipe | 16/100 = 16% | 2/20 = 10% (base 16% = 3.2/20) | untested | 30/100 = 30% (base 16% = 16.0/100) |
| restack | 0/100 = 0% | untested | untested | untested |
| twolift | 1/100 = 1% | untested | untested | untested |
| handover | 2/100 = 2% | untested | untested | untested |
| revstack | 0/100 = 0% | untested | untested | untested |
| stackv2 | 1/100 = 1% | untested | untested | untested |

GPU-hours: 14.392 spent, 1.608 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: lift_a1+stack_a1
Submitted: base + lift_a1 (sha 059ff287ae7a) + stack_a1 (sha a063cff39fdf) (turn 51, token 4dd2a4; confirmed in turn 53)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| lift_a1 | base | 20 | specs/lift_a1.json | trained |
| stack_a1 | base | 20 | specs/stack_a1.json | trained |

## History (latest 30)

- train lift_a1 (init base, steps 20): trained
- eval lift_a1 on lift: 88/100
- eval lift_a1 on stack: 33/100
- eval lift_a1 on wipe: 2/20
- load lift_a1
- train stack_a1 (init base, steps 20): trained
- eval lift_a1+stack_a1 on stack: 65/100
- eval lift_a1+stack_a1 on lift: 88/100
- eval lift_a1+stack_a1 on wipe: 7/20
- load lift_a1+stack_a1
- eval lift_a1+stack_a1 on wipe: 30/100
- load lift_a1+stack_a1
- eval lift_a1+stack_a1 on nut: 0/20
- finish: submitted lift_a1+stack_a1 (token 4dd2a4, job 24)
- finish: confirmed lift_a1+stack_a1 (token 4dd2a4)
