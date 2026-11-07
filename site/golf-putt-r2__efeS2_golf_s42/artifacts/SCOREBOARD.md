# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: tinker:Qwen/Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | a1 | a3 |
|---|---|---|---|
| embodied-olympics-fun-golf-putt | untested | untested | untested |

GPU-hours: 1.507 spent, 0.493 remaining of 2.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.18, 10 steps 1.32, 50 steps 6.41) GPU-h; eval.py per task (5 seeds 0.02, 20 seeds 0.04, 100 seeds 0.12) GPU-h
Loaded on your serving endpoint: base
Submitted: base (turn 14, token ae9e67; confirmed in turn 15)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| a1 | base | 1 | probe1.yaml | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| a3 | base | 10 | runA.yaml | trained 10 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |

## History (latest 30)

- train a1 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train a3 (init base, steps 10): trained 10 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- finish: submitted base (token ae9e67, job 5)
- finish: confirmed base (token ae9e67)
