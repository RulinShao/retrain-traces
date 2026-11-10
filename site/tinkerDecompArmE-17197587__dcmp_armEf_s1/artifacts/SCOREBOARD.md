# SCOREBOARD

playbook: nogit-f1700b86
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | revstack1 | restack1 | nut1 | sft1 | sft2 | sft3 | sft4 | sft5 | sft6b |
|---|---|---|---|---|---|---|---|---|---|---|
| nut | 0/100 = 0% | untested | untested | 0/60 = 0% (base 0% = 0.0/60) | 0/30 = 0% (base 0% = 0.0/30) | 0/50 = 0% (base 0% = 0.0/50) | 0/50 = 0% (base 0% = 0.0/50) | 0/50 = 0% (base 0% = 0.0/50) | 0/20 = 0% (base 0% = 0.0/20) | 0/20 = 0% (base 0% = 0.0/20) |
| restack | 0/100 = 0% | untested | 0/60 = 0% (base 0% = 0.0/60) | untested | 0/30 = 0% (base 0% = 0.0/30) | 50/100 = 50% (base 0% = 0.0/100) | 31/50 = 62% (base 0% = 0.0/50) | 0/20 = 0% (base 0% = 0.0/20) | 0/50 = 0% (base 0% = 0.0/50) | 36/50 = 72% (base 0% = 0.0/50) |
| revstack | 1/100 = 1% | 0/60 = 0% (base 1% = 0.6/60) | untested | untested | 0/30 = 0% (base 1% = 0.3/30) | 51/100 = 51% (base 1% = 1.0/100) | 25/50 = 50% (base 1% = 0.5/50) | 0/20 = 0% (base 1% = 0.2/20) | 0/50 = 0% (base 1% = 0.5/50) | 21/50 = 42% (base 1% = 0.5/50) |

GPU-hours: 35.326 spent, 12.674 remaining of 48.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: sft6b
Submitted: base + sft6b (sha 5e3d1fde02ad) (turn 299, token 03d763; unconfirmed; scored at the session end (CAPPED))

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| revstack1 | base | 30 | spec_revstack1.json | trained |
| restack1 | base | 30 | spec_restack1.json | trained |
| nut1 | base | 30 | spec_nut1.json | trained |
| sft1 | base | None | spec_sft1.json | trained |
| sft2 | base | None | spec_sft2.json | trained |
| sft3 | base | None | sft3spec.json | trained |
| sft4 | base | None | sft4spec.json | trained |
| sft5 | base | None | sft5spec.json | trained |
| sft6b | base | None | sft6bspec.json | trained |

- train job 143 (sft4): prompt in 40 data row(s) set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim
- train job 150 (sft5): prompt in 80 data row(s) set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- job 15: rollout restack1 on restack: 12 seeds -> rollouts/15.jsonl; self-reward mean 0.381 over 12 seeds (rewards/restack_reach.py); stages reached: unstack the green off the red 12/12, grasp the red 0/12, lift the red 0/12, align the red over the green 0/12, place the red on the green 0/12; distinct values over 12 rows: task_completed 1, sim_reward 12, stage unstack the green off the red 1, stage grasp the red 1, stage lift the red 1, stage align the red over the green 1, stage place the red on the green 1

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- revstack: 16 failures in adapters/revstack1/failures.jsonl; stages none:13 lift the green_cube:2 grasp the green_cube:1
- restack: 16 failures in adapters/restack1/failures.jsonl; stages none:15 unstack the green off the red:1
- nut: 16 failures in adapters/nut1/failures.jsonl; stages none:15 grasp the nut:1

## History (latest 30)

- eval sft3 on revstack: 17/50
- eval sft3 on nut: 0/50
- eval sft3 on revstack: 25/50
- rollout sft3 on nut: 8 seeds -> rollouts/129.jsonl; stages reached: reach the handle 2/8, grasp the nut 0/8, align the nut over the peg 0/8, insert the nut 0/8; distinct values over 8 rows: task_completed 1, sim_reward 7, stage reach the handle 2, stage grasp the nut 1, stage align the nut over the peg 1, stage insert the nut 1
- preset nd3 on nut: 4 seeds -> presets/nd3.json
- preset nd4 on nut: 4 seeds -> presets/nd4.json
- preset nd5 on nut: 4 seeds -> presets/nd5.json
- preset nd6 on nut: 4 seeds -> presets/nd6.json
- cancel job 139
- train sft4 failed: train: data line 1: prompt must be a list of messages {"role", "content"} (tasks/<task>/eval_prompt.txt's chat)
- preset nd7 cancelled: preset nd7 cancelled; no preset kept (a preset needs every seed's state); charged 0.000 GPU-h
- train sft4 (init base, steps None): trained
- eval sft4 on nut: 0/50
- eval sft4 on restack: 0/20
- eval sft4 on revstack: 0/20
- train sft5 (init base, steps None): trained
- eval sft5 on restack: 0/50
- eval sft5 on revstack: 0/50
- eval sft5 on nut: 0/20
- cancel job 156
- train sft6 cancelled: train cancelled; its job ended (JobFailed)
- train sft6b (init base, steps None): trained
- eval sft6b on restack: 36/50
- eval sft6b on revstack: 21/50
- eval sft6b on nut: 0/20
- cancel job 164
- load sft6b
- eval base cancelled: eval cancelled; charged 0.014 GPU-h
- train rstack6 failed: train: epochs, min_reward: field(s) of objective 'sft'; a grpo spec has none
- train rstack6 failed: train: data line 1: prompt must be a list of messages {"role", "content"} (tasks/<task>/eval_prompt.txt's chat)
