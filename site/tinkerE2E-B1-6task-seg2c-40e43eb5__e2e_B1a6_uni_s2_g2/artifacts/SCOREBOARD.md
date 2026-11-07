# SCOREBOARD

playbook: none
agent: scripted:e2e-rl+6task-uniform-seg2
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | e2e_c1 | e2e_c2 |
|---|---|---|---|
| lift | untested | untested | untested |
| stack | untested | untested | untested |
| wipe | untested | untested | untested |
| nut | untested | untested | untested |
| restack | untested | untested | untested |
| revstack | untested | untested | untested |

GPU-hours: 13.822 spent, 2.178 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.44, 10 steps 2.42, 50 steps 11.23) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: e2e_c2
Submitted: base + e2e_c2 (sha 4de9f939ebf4) (turn 5, token c51fda; confirmed in turn 6)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| e2e_c1 | …/adapters/e2e_c2 | None | specs/e2e_c1.json | trained |
| e2e_c2 | e2e_c1 | 13 | specs/e2e_c2.json | trained |

## History (latest 30)

- train e2e_c1 (init …/adapters/e2e_c2, steps None): trained
- train e2e_c2 (init e2e_c1, steps 13): trained
- load e2e_c2
- finish: submitted e2e_c2 (token c51fda, job 6)
- finish: confirmed e2e_c2 (token c51fda)
