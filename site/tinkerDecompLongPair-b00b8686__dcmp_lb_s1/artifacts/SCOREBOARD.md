# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | rev1 | nu1 | rev2 | sftrev1 | sftrev2 | rev3 | restack3 | restack4 | nut4 | revstack4 | restack_sft | revstack6 | revstack5 | revstack7 | revstack8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nut | 0/100 = 0% | untested | 0/100 = 0% (base 0% = 0.0/100) | untested | untested | untested | 0/20 = 0% (base 0% = 0.0/20) | untested | untested | 0/20 = 0% (base 0% = 0.0/20) | untested | untested | untested | untested | untested | untested |
| restack | 0/100 = 0% | untested | 0/100 = 0% (base 0% = 0.0/100) | untested | untested | untested | 0/50 = 0% (base 0% = 0.0/50) | untested | untested | untested | untested | 0/20 = 0% (base 0% = 0.0/20) | untested | untested | untested | untested |
| revstack | 1/100 = 1% | 0/20 = 0% (base 1% = 0.2/20) | untested | 1/100 = 1% (base 1% = 1.0/100) | 1/100 = 1% (base 1% = 1.0/100) | 0/100 = 0% (base 1% = 1.0/100) | 5/100 = 5% (base 1% = 1.0/100) | untested | untested | untested | 1/100 = 1% (base 1% = 1.0/100) | untested | 2/50 = 4% (base 1% = 0.5/50) | untested | 2/50 = 4% (base 1% = 0.5/50) | 2/100 = 2% (base 1% = 1.0/100) |

GPU-hours: 38.855 spent, 9.145 remaining of 48.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: rev3
Submitted: base + rev3 (sha 6b9b6a0a6c8f) (turn 136, token f84276; confirmed in turn 140)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| rev1 | base | 10 | spec_rev1.json | trained |
| nu1 | base | 20 | spec_nu1.json | trained |
| rev2 | rev1 | 25 | spec_rev2.json | trained |
| sftrev1 | base | None | spec_sftrev1.json | trained |
| sftrev2 | base | None | spec_sftrev2.json | trained |
| rev3 | adapters/rev2 | 35 | spec_rev3.json | trained |
| restack3 | base | 35 | spec_restack3.json | trained |
| restack4 | base | 11 | spec_restack4.json | trained |
| nut4 | base | 30 | spec_nut4.json | trained |
| revstack4 | rev3 | 30 | spec_revstack4.json | trained |
| restack_sft | base | None | spec_sft_restack.json | trained |
| revstack6 | rev3 | None | spec_revstack6.json | trained |
| revstack5 | rev3 | 7 | spec_revstack5.json | trained |
| revstack7 | rev3 | None | spec_revstack7.json | trained |
| revstack8 | rev3 | 15 | spec_revstack8.json | trained |

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- revstack: 16 failures in adapters/rev1/failures.jsonl; stages none:14 grasp the green_cube:2
- nut: 16 failures in adapters/nu1/failures.jsonl; stages none:15 grasp the nut:1
- restack: 16 failures in adapters/nu1/failures.jsonl; stages none:15 unstack the green off the red:1
- revstack: 16 failures in adapters/rev2/failures.jsonl; stages none:6 reach the green_cube:6 grasp the green_cube:4
- revstack: 16 failures in adapters/rev3/failures.jsonl; stages none:12 grasp the green_cube:4
- restack: 16 failures in adapters/restack3/failures.jsonl; stages none:13 unstack the green off the red:2 align the red over the green:1
- restack: 16 failures in adapters/restack4/failures.jsonl; stages unstack the green off the red:10 none:6
- nut: 16 failures in adapters/nut4/failures.jsonl; stages none:16
- revstack: 16 failures in adapters/revstack4/failures.jsonl; stages lift the green_cube:7 grasp the green_cube:6 reach the green_cube:2 none:1
- revstack: 16 failures in adapters/revstack5/failures.jsonl; stages grasp the green_cube:6 none:5 reach the green_cube:4 lift the green_cube:1
- revstack: 16 failures in adapters/revstack8/failures.jsonl; stages grasp the green_cube:8 lift the green_cube:3 none:3 reach the green_cube:2

## History (latest 30)

- eval rev1+rev2 cancelled: eval cancelled; charged 0.000 GPU-h
- cancel job 45
- train restack4 (init base, steps 11): trained
- train nut4 (init base, steps 30): trained
- train restack_sft failed: train: init adapter not found: …/adapters/base
- train revstack4 (init rev3, steps 30): trained
- train restack_sft (init base, steps None): trained
- eval revstack4+restack_sft+nut4 failed: eval: stack rank 96 > 64 (the serving's --max-lora-rank): at most 2 adapters of rank 32
- eval revstack4+restack_sft+nut4 failed: eval: stack rank 96 > 64 (the serving's --max-lora-rank): at most 2 adapters of rank 32
- eval revstack4 on revstack: 1/100
- eval rev3 on revstack: 1/20
- eval restack_sft on restack: 0/20
- eval nut4 on nut: 0/20
- train revstack6 (init rev3, steps None): trained
- cancel job 61
- train revstack5 (init rev3, steps 7): trained
- eval revstack6 on revstack: 2/50
- eval rev3 on revstack: 3/50
- train revstack7 (init rev3, steps None): trained
- eval revstack7 on revstack: 2/50
- load rev3
- train revstack8 (init rev3, steps 15): trained
- eval revstack8 on revstack: 2/100
- eval rev3 on revstack: 5/100
- rollout restack_sft on restack: 5 seeds -> rollouts/83.jsonl; stages reached: unstack the green off the red 4/5, grasp the red 0/5, lift the red 0/5, align the red over the green 0/5, place the red on the green 0/5; distinct values over 5 rows: task_completed 1, sim_reward 5, stage unstack the green off the red 2, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1
- load rev3
- finish: submitted rev3 (token f84276, job 86)
- eval rev3 on restack: 0/50
- eval rev3 on nut: 0/20
- finish: confirmed rev3 (token f84276)
