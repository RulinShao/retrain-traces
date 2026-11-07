# SCOREBOARD

playbook: 6df138df-8645d430
agent: local
mode: dev
dev seeds: from 800071
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (RoboCasa365 pool: every eval samples on Tinker, base or Tinker-trained adapter; dev / practice seeds only, hidden seeds refused); final=DEV (dev seeds 800021-800070, n=50, sampled on Tinker; never a Table 2 number: hidden finals need the local 27B)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | mwt_base_full1 | diag_mwt_0 | diag_mwt_1 | diag_mwt_2 | diag_bp_a | diag_bp_b | diag_tb_a | diag_tb_tongs | diag_bp_potmoved | diag_mw_note | diag_tb_tn | diag_tb_tc | diag_gp_s | diag_mil_l | diag_cr_m | bd0.15 | bd1.00 | bd0.50 | bd0.30 | bp_sanity | tb_tray0.3 | tb_tray0.8 | tb_tray1.5 | note_tcomp_0 | note_tcomp_1 | note_tcomp_2 | gp_band03 | gp_moved |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TongBuffetSetup | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| PlaceVeggiesInDrawer | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| OrganizeMetallicUtensils | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BoilPot | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| SimmeringSauce | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| HeatMultipleWater | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BlendVegetableSauce | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BlendMarinade | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BlendIngredients | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| SteamInMicrowave | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| MicrowaveDefrostMeat | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| MicrowaveThawing | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| WashFruitColander | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| GetToastedBread | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| ClearReceptaclesForCleaning | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| HeatKebabSandwich | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| ToasterOvenBroilFish | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| ArrangeBreadBowl | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| MakeIceLemonade | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| GarnishPancake | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| CerealAndBowl | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| PackIdenticalLunches | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| StirVegetables | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| GatherTableware | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |

GPU-hours: 11.328 spent, 4.672 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.21, 10 steps 1.34, 50 steps 6.37) GPU-h; eval.py per task (5 seeds 0.09, 20 seeds 0.12, 100 seeds 0.27) GPU-h
Loaded on your serving endpoint: base
Submitted: base (turn 49, token 2188e4; confirmed in turn 51)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| mwt_base_full1 | base | 2 | spec_mwt.json | trained 2 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| diag_mwt_0 | base | 1 | specs/diag_mwt_0.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| diag_mwt_1 | base | 1 | specs/diag_mwt_1.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| diag_mwt_2 | base | 1 | specs/diag_mwt_2.json | trained |
| diag_bp_a | base | 1 | specs/diag_bp_a.json | trained |
| diag_bp_b | base | 1 | specs/diag_bp_b.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| diag_tb_a | base | 1 | specs/diag_tb_a.json | trained |
| diag_tb_tongs | base | 1 | specs/diag_tb_tongs.json | trained |
| diag_bp_potmoved | base | 1 | specs/diag_bp_potmoved.json | trained |
| diag_mw_note | base | 1 | specs/diag_mw_note.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| diag_tb_tn | base | 1 | specs/diag_tb_tn.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| diag_tb_tc | base | 1 | specs/diag_tb_tc.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| diag_gp_s | base | 1 | specs/diag_gp_s.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| diag_mil_l | base | 1 | specs/diag_mil_l.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| diag_cr_m | base | 1 | specs/diag_cr_m.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| bd0.15 | base | 1 | specs/bd0.15.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| bd1.00 | base | 1 | specs/bd1.00.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| bd0.50 | base | 1 | specs/bd0.50.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| bd0.30 | base | 1 | specs/bd0.30.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| bp_sanity | base | 1 | specs/bp_sanity.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| tb_tray0.3 | base | 1 | specs/tb_tray0.3.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| tb_tray0.8 | base | 1 | specs/tb_tray0.8.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| tb_tray1.5 | base | 1 | specs/tb_tray1.5.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| note_tcomp_0 | base | 1 | specs/note_tcomp_0.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| note_tcomp_1 | base | 1 | specs/note_tcomp_1.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| note_tcomp_2 | base | 1 | specs/note_tcomp_2.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| gp_band03 | base | 1 | specs/gp_band03.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| gp_moved | base | 1 | specs/gp_moved.json | trained |

- train job 21 (diag_mw_note): note set: part of the training prompt only; every eval, including the final score, uses tasks/MicrowaveThawing/eval_prompt.txt verbatim
- train job 49 (note_tcomp_0): note set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 50 (note_tcomp_1): note set: part of the training prompt only; every eval, including the final score, uses tasks/TongBuffetSetup/eval_prompt.txt verbatim
- train job 51 (note_tcomp_2): note set: part of the training prompt only; every eval, including the final score, uses tasks/PlaceVeggiesInDrawer/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## History (latest 30)

- train diag_mwt_0 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train diag_mwt_1 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train diag_mwt_2 (init base, steps 1): trained
- train diag_bp_a (init base, steps 1): trained
- train diag_bp_b (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train diag_tb_a (init base, steps 1): trained
- rollout base on BoilPot: 4 seeds -> rollouts/17.jsonl
- train diag_tb_tongs (init base, steps 1): trained
- train diag_bp_potmoved (init base, steps 1): trained
- train diag_mw_note (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train diag_tb_tn (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train diag_tb_tc (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train diag_gp_s (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train diag_mil_l (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train diag_cr_m (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train bd0.15 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train bd1.00 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train bd0.50 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train bd0.30 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train bp_sanity (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train tb_tray0.3 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train tb_tray0.8 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train tb_tray1.5 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train note_tcomp_0 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train note_tcomp_1 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train note_tcomp_2 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train gp_band03 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train gp_moved (init base, steps 1): trained
- finish: submitted base (token 2188e4, job 56)
- finish: confirmed base (token 2188e4)
