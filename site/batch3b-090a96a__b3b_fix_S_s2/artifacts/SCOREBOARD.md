# SCOREBOARD

playbook: 13a939b-eeac9359
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | v1 | current |
|---|---|---|---|
| lift | 67/100 = 67% | untested | 74/100 = 74% (v1) (base 67% = 67.0/100) |
| stack | 51/100 = 51% | untested | 60/100 = 60% (v1) (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | 1/100 = 1% (v1) (base 0% = 0.0/100) |
| wipe | 16/100 = 16% | untested | 29/100 = 29% (v1) (base 16% = 16.0/100) |
| restack | 0/100 = 0% | untested | 0/100 = 0% (v1) (base 0% = 0.0/100) |
| twolift | 1/100 = 1% | untested | 0/100 = 0% (v1) (base 1% = 1.0/100) |
| handover | 2/100 = 2% | untested | 1/100 = 1% (v1) (base 2% = 2.0/100) |
| revstack | 0/100 = 0% | untested | 3/100 = 3% (v1) (base 0% = 0.0/100) |
| stackv2 | 1/100 = 1% | untested | 4/100 = 4% (v1) (base 1% = 1.0/100) |

GPU-hours: 15.014 spent, 0.986 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: current
Submitted: base + current (v1, sha e1d3ecf25ee6) (turn 16, token d35fc7; confirmed in turn 18)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| v1 | base | 30 | specs/stack30.json | trained |
| current | base | 30 | specs/stack30.json | trained |

Lineage of current: base -> v1 (train job 1, steps 30, specs/stack30.json, trained)
Active version: v1 (load.py load v<k> to make another active)

## History (latest 30)

- train current v1 (init base, steps 30): trained; loaded current v1
- eval current failed: the call ended in an infrastructure fault; the session stopped there and was resumed after the operator fixed the cause
- eval current failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- eval current failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- eval current failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- eval current failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- eval current failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- eval current failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- eval current failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- eval current failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- eval current on lift: 74/100
- eval current on stack: 60/100
- eval current on nut: 1/100
- eval current on wipe: 29/100
- eval current on restack: 0/100
- eval current on twolift: 0/100
- eval current on handover: 1/100
- eval current on revstack: 3/100
- eval current on stackv2: 4/100
- finish: submitted current (token 54b6c6, DONE)
- finish: submitted current (token a4180f, DONE)
- finish: submitted current (token d35fc7, DONE)
- finish: confirmed current (token d35fc7)
