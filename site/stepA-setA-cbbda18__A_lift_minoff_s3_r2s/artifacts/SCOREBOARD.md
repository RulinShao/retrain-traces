# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | l10 |
|---|---|---|
| lift | 67/100 = 67% | 78/100 = 78% (base 67% = 67.0/100) |

GPU-hours: 4.506 spent, 3.494 remaining of 8.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: l10
Submitted: base + l10 (sha dcf3b6b5844b) (turn 26, token 1777dd; confirmed in turn 27)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| l10 | base | 10 | spec_l10.json | trained |

## History (latest 30)

- train l10 (init base, steps 10): trained
- eval l10 on lift: 78/100
- load l10
- train sft1 failed: train: objective 'sft' trains the small policy profiles on this site (Qwen3-14B, Qwen3-8B, Qwen3-Coder-30B-A3B-Instruct); this session's policy is Qwen3.8-27B
- finish: submitted l10 (token 1777dd, job 11)
- finish: confirmed l10 (token 1777dd)
