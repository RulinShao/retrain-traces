# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | stack1 | wipe1 | stack1+wipe1 |
|---|---|---|---|---|
| lift | 67/100 = 67% | untested | untested | untested |
| stack | 51/100 = 51% | 56/100 = 56% (base 51% = 51.0/100) | untested | 49/100 = 49% (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | untested | untested |
| wipe | 16/100 = 16% | untested | untested | 32/100 = 32% (base 16% = 16.0/100) |
| restack | 0/100 = 0% | untested | untested | untested |
| twolift | 1/100 = 1% | untested | untested | untested |
| handover | 2/100 = 2% | untested | untested | untested |
| revstack | 0/100 = 0% | untested | untested | untested |
| stackv2 | 1/100 = 1% | untested | untested | untested |

GPU-hours: 15.278 spent, 0.722 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: stack1+wipe1
Submitted: base + stack1 (sha a8d6314f3b43) + wipe1 (sha 01ec4ee0468a) (turn 23, token 687faf; confirmed in turn 33)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| stack1 | base | 20 | spec_stack.json | trained |
| wipe1 | base | 8 | spec_wipe.json | trained |

## History (latest 30)

- train wipe1 failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- train restack1 failed: the call's outcome was lost: the session stopped on an infrastructure failure while it ran and was resumed; this site cannot recover a call across a restart
- eval stack1 failed: the call ended in an infrastructure fault; the session stopped there and was resumed after the operator fixed the cause
- eval stack1 on stack: 56/100
- load stack1
- train wipe1 (init base, steps 8): trained
- eval stack1+wipe1 on wipe: 32/100
- eval stack1+wipe1 on stack: 49/100
- load stack1+wipe1
- finish: submitted stack1+wipe1 (token 687faf, DONE)
- finish: confirmed stack1+wipe1 (token 687faf)
