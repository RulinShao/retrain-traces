# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 900001
policy: Qwen3-8B+init:79fbddb55dd8

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | r1s |
|---|---|---|
| lift | 89/100 = 89% | untested |
| stack | 57/100 = 57% | untested |
| nut | 0/100 = 0% | untested |
| wipe | 22/100 = 22% | untested |
| restack | 0/100 = 0% | untested |
| twolift | 0/100 = 0% | untested |
| handover | 0/100 = 0% | untested |
| revstack | 2/100 = 2% | untested |
| stackv2 | 1/100 = 1% | untested |

GPU-hours: 1.193 spent, 14.431 remaining of 16.0 (1 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.47, 10 steps 0.70, 50 steps 1.70) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| r1s | base | 1 | specs/r1s.json | trained |

## History (latest 30)

- train n1s failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- train lift_a failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- train stack_a failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- train stack_1 failed: the call ended in an infrastructure fault; the session stopped there and was resumed after the operator fixed the cause
- train wipe_1 failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- train restack_1 failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
