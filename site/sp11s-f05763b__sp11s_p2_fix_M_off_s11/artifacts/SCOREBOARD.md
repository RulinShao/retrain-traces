# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | r1_wipe | r1_restack | r1_stack | r1_stack+r1_wipe |
|---|---|---|---|---|---|
| lift | 67/100 = 67% | 12/20 = 60% (base 67% = 13.4/20) | untested | 17/20 = 85% (base 67% = 13.4/20) | 14/20 = 70% (base 67% = 13.4/20) |
| stack | 51/100 = 51% | untested | untested | untested | 13/20 = 65% (base 51% = 10.2/20) |
| nut | 0/100 = 0% | untested | untested | untested | untested |
| wipe | 16/100 = 16% | untested | untested | untested | 12/20 = 60% (base 16% = 3.2/20) |
| restack | 0/100 = 0% | untested | untested | untested | untested |
| twolift | 1/100 = 1% | untested | untested | untested | untested |
| handover | 2/100 = 2% | untested | untested | untested | untested |
| revstack | 0/100 = 0% | untested | untested | untested | untested |
| stackv2 | 1/100 = 1% | untested | untested | untested | 0/20 = 0% (base 1% = 0.2/20) |

GPU-hours: 15.740 spent, 0.260 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: r1_stack+r1_wipe
Submitted: base + r1_stack (sha 328eb37e82e7) + r1_wipe (sha 1720a34aca5f) (turn 24, token 78f22c; confirmed in turn 25)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| r1_wipe | base | 10 | specs/r1_wipe.json | trained |
| r1_restack | base | 10 | specs/r1_restack.json | trained |
| r1_stack | base | 10 | specs/r1_stack.json | trained |

## History (latest 30)

- train r1_wipe (init base, steps 10): trained
- train r1_restack (init base, steps 10): trained
- train r1_stack (init base, steps 10): trained
- eval r1_stack+r1_wipe on lift: 14/20
- eval r1_stack+r1_wipe on stack: 13/20
- eval r1_stack+r1_wipe on wipe: 12/20
- eval r1_stack on lift: 17/20
- eval r1_wipe on lift: 12/20
- eval r1_stack+r1_wipe on stackv2: 0/20
- load r1_stack+r1_wipe
- finish: submitted r1_stack+r1_wipe (token 78f22c, job 19)
- finish: confirmed r1_stack+r1_wipe (token 78f22c)
