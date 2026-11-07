# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800071
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (RoboCasa365 pool: every eval samples on Tinker, base or Tinker-trained adapter; dev / practice seeds only, hidden seeds refused); final=DEV (dev seeds 800021-800070, n=50, sampled on Tinker; never a Table 2 number: hidden finals need the local 27B)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | probe_boilpot | h2_blendingredients | h1_boilpot | sg_bp_burner | sg_bl_lid | sg_bp_place | pr_micr_start | pr_pickup_ssm | comp_mwt |
|---|---|---|---|---|---|---|---|---|---|---|
| TongBuffetSetup | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| PlaceVeggiesInDrawer | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| OrganizeMetallicUtensils | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BoilPot | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| SimmeringSauce | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| HeatMultipleWater | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BlendVegetableSauce | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BlendMarinade | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BlendIngredients | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| SteamInMicrowave | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| MicrowaveDefrostMeat | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| MicrowaveThawing | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | 0/20 = 0% (base 0% = 0.0/20) | untested |
| WashFruitColander | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| GetToastedBread | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | 0/20 = 0% (base 0% = 0.0/20) | untested |
| ClearReceptaclesForCleaning | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| HeatKebabSandwich | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| ToasterOvenBroilFish | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| ArrangeBreadBowl | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| MakeIceLemonade | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| GarnishPancake | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| CerealAndBowl | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | 0/20 = 0% (base 0% = 0.0/20) | untested |
| PackIdenticalLunches | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| StirVegetables | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| GatherTableware | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested |

GPU-hours: 15.348 spent, 0.652 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.21, 10 steps 1.34, 50 steps 6.37) GPU-h; eval.py per task (5 seeds 0.09, 20 seeds 0.12, 100 seeds 0.27) GPU-h
Loaded on your serving endpoint: base
Submitted: base + pr_pickup_ssm (sha b1030ae921dc) + pr_micr_start (sha 9370d712fde9) + sg_bp_burner (sha bf121c2f4d3f) (turn 130, token 6d8785; confirmed in turn 133)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| probe_boilpot | base | 1 | spec_probe_bp.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| h2_blendingredients | base | 1 | spec_h2_blendingredients.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| h1_boilpot | base | 1 | spec_h1_boilpot.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| sg_bp_burner | base | 8 | spec_sg_bp_burner.json | trained |
| sg_bl_lid | base | 8 | spec_sg_bl_lid.json | trained 8 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| sg_bp_place | base | 8 | spec_sg_bp_place.json | trained 8 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| pr_micr_start | base | 8 | spec_pr_micr_start.json | trained |
| pr_pickup_ssm | base | 8 | spec_pr_pickup_ssm.json | trained |
| comp_mwt | pr_pickup_ssm | 12 | spec_comp_mwt.json | trained |

- train job 11 (h1_boilpot): note set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 12 (h2_blendingredients): note set: part of the training prompt only; every eval, including the final score, uses tasks/BlendIngredients/eval_prompt.txt verbatim
- train job 29 (sg_bp_place): goal set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 30 (sg_bp_burner): goal set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 31 (sg_bl_lid): goal set: part of the training prompt only; every eval, including the final score, uses tasks/BlendIngredients/eval_prompt.txt verbatim
- train job 34 (pr_micr_start): goal set: part of the training prompt only; every eval, including the final score, uses tasks/SteamInMicrowave/eval_prompt.txt verbatim
- train job 35 (pr_cab_close): goal set: part of the training prompt only; every eval, including the final score, uses tasks/CerealAndBowl/eval_prompt.txt verbatim
- train job 36 (pr_pickup_ssm): goal set: part of the training prompt only; every eval, including the final score, uses tasks/SteamInMicrowave/eval_prompt.txt verbatim
- train job 42 (comp_mwt): goal set: part of the training prompt only; every eval, including the final score, uses tasks/MicrowaveThawing/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- job 26: rollout base on BoilPot: 5 seeds -> rollouts/26.jsonl; self-reward mean None over 0 seeds (rewards/dump.py)
- job 32: eval base on BoilPot: 0/20 -> rollouts/32.jsonl; self-reward mean None over 0 seeds (rewards/knob_changed_r.py)

## History (latest 30)

- train h2_blendingredients (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train h1_boilpot (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- preset pp_actuate failed: preset: preset building (preset.py) is not available for the RoboCasa365 pool on hyak (CaP-X simulator units only)
- preset pp_frobnicate_zzq failed: preset: preset building (preset.py) is not available for the RoboCasa365 pool on hyak (CaP-X simulator units only)
- preset pp_navigate_to failed: preset: preset building (preset.py) is not available for the RoboCasa365 pool on hyak (CaP-X simulator units only)
- train s1_boilpot failed: train: time: HH:MM:SS
- train s2_blend failed: train: time: HH:MM:SS
- cancel job 19
- cancel job 21
- train s1_boilpot cancelled: train cancelled; its job ended (JobFailed)
- train s2_blend cancelled: train cancelled; its job ended (JobFailed)
- rollout base on BoilPot: 5 seeds -> rollouts/26.jsonl; self-reward mean None over 0 seeds (rewards/dump.py)
- train sg_bp_burner (init base, steps 8): trained
- train sg_bl_lid (init base, steps 8): trained 8 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train sg_bp_place (init base, steps 8): trained 8 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- eval base on BoilPot: 0/20 --reward -> rollouts/32.jsonl
- cancel job 35
- train pr_cab_close cancelled: train cancelled; its job ended (JobFailed)
- train pr_micr_start (init base, steps 8): trained
- cancel job 33
- eval sg_bp_burner cancelled: eval cancelled; charged 0.000 GPU-h
- train pr_pickup_ssm (init base, steps 8): trained
- eval pr_pickup_ssm+pr_micr_start failed: eval: a RoboCasa eval samples one Tinker state: evaluate one adapter (or none for the base), not a stack
- eval pr_pickup_ssm+pr_micr_start failed: eval: a RoboCasa eval samples one Tinker state: evaluate one adapter (or none for the base), not a stack
- eval pr_pickup_ssm on MicrowaveThawing: 0/20
- eval pr_pickup_ssm on CerealAndBowl: 0/20
- eval pr_pickup_ssm on GetToastedBread: 0/20
- finish: submitted pr_pickup_ssm+pr_micr_start+sg_bp_burner (token 6d8785, job 46)
- finish: confirmed pr_pickup_ssm+pr_micr_start+sg_bp_burner (token 6d8785)
- train comp_mwt (init pr_pickup_ssm, steps 12): trained
