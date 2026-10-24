# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 900001
policy: Qwen3-8B+init:79fbddb55dd8

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | lift1 | stack1 | wipe1 | restack1 | nut1 | rev1 | restack2 | nut2 | rev2 | stack2 | wipe2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| lift | 89/100 | 19/20 | - | - | - | - | - | - | - | - | - | - |
| stack | 57/100 | - | 11/20 | - | - | - | - | - | - | - | - | - |
| nut | 0/100 | - | - | - | - | 0/20 | - | - | - | - | - | - |
| wipe | 22/100 | - | - | 12/20 | - | - | - | - | - | - | - | - |
| restack | 0/100 | - | - | - | 0/20 | - | - | - | - | - | - | - |
| twolift | 0/100 | - | - | - | - | - | - | - | - | - | - | - |
| handover | 0/100 | - | - | - | - | - | - | - | - | - | - | - |
| revstack | 2/100 | - | - | - | - | - | 2/20 | - | - | - | - | - |
| stackv2 | 1/100 | - | - | - | - | - | - | - | - | - | - | - |

GPU-hours: 12.456 spent, 3.544 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.47, 10 steps 0.70, 50 steps 1.70) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: base

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| lift1 | base | 15 | specs/lift1.json | trained |
| stack1 | base | 15 | specs/stack1.json | trained |
| wipe1 | base | 15 | specs/wipe1.json | trained |
| restack1 | base | 25 | specs/restack1.json | trained |
| nut1 | base | 25 | specs/nut1.json | trained |
| rev1 | base | 25 | specs/rev1.json | trained |
| restack2 | restack1 | 20 | specs/restack2.json | trained |
| nut2 | nut1 | 20 | specs/nut2.json | trained |
| rev2 | rev1 | 20 | specs/rev2.json | trained |
| stack2 | stack1 | 15 | specs/stack2.json | trained |
| wipe2 | wipe1 | 15 | specs/wipe2.json | trained |

## History (latest 30)

- train lift1 (init base, steps 15): trained
- train stack1 (init base, steps 15): trained
- train wipe1 (init base, steps 15): trained
- train restack1 (init base, steps 25): trained
- train nut1 (init base, steps 25): trained
- train rev1 (init base, steps 25): trained
- eval lift1 on lift: 19/20
- eval stack1 on stack: 11/20
- eval wipe1 on wipe: 12/20
- eval restack1 on restack: 0/20
- eval nut1 on nut: 0/20
- eval rev1 on revstack: 2/20
- train restack2 (init restack1, steps 20): trained
- train nut2 (init nut1, steps 20): trained
- train rev2 (init rev1, steps 20): trained
- train stack2 (init stack1, steps 15): trained
- train wipe2 (init wipe1, steps 15): trained
