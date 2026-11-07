# SCOREBOARD

playbook: 6df138df-8645d430
agent: local
mode: dev
dev seeds: from 800071
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (RoboCasa365 pool: every eval samples on Tinker, base or Tinker-trained adapter; dev / practice seeds only, hidden seeds refused); final=DEV (dev seeds 800021-800070, n=50, sampled on Tinker; never a Table 2 number: hidden finals need the local 27B)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | p_boil | p_mw | p_tong | p_ice | p_straw | g_pot | g_chick | g_tong | d_approach | d_near | d_moved | d_loosepot | d_potmoved | d_chickloose | boil_note_fresh | boil_note_moved | o_drawer | o_cab | o_fridge | m_ice_precise |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TongBuffetSetup | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| PlaceVeggiesInDrawer | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| OrganizeMetallicUtensils | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BoilPot | 0/20 = 0% | 0/20 = 0% (base 0% = 0.0/20) | untested | untested | untested | untested | untested | untested | untested | untested | untested | 0/20 = 0% (base 0% = 0.0/20) | untested | 0/20 = 0% (base 0% = 0.0/20) | untested | untested | untested | untested | untested | untested | untested |
| SimmeringSauce | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| HeatMultipleWater | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BlendVegetableSauce | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BlendMarinade | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BlendIngredients | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| SteamInMicrowave | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| MicrowaveDefrostMeat | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| MicrowaveThawing | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| WashFruitColander | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| GetToastedBread | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| ClearReceptaclesForCleaning | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| HeatKebabSandwich | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| ToasterOvenBroilFish | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| ArrangeBreadBowl | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| MakeIceLemonade | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| GarnishPancake | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| CerealAndBowl | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| PackIdenticalLunches | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| StirVegetables | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| GatherTableware | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |

GPU-hours: 14.096 spent, 1.904 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.21, 10 steps 1.34, 50 steps 6.37) GPU-h; eval.py per task (5 seeds 0.09, 20 seeds 0.12, 100 seeds 0.27) GPU-h
Loaded on your serving endpoint: base
Submitted: base + p_boil (sha 28508c89ebdd) (turn 28, token 79bcf8; confirmed in turn 30)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| p_boil | base | 1 | specs/p_boil.json | trained |
| p_mw | base | 1 | specs/p_mw.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| p_tong | base | 1 | specs/p_tong.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| p_ice | base | 1 | specs/p_ice.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| p_straw | base | 1 | specs/p_straw.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| g_pot | base | 1 | specs/g_pot.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| g_chick | base | 1 | specs/g_chick.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| g_tong | base | 1 | specs/g_tong.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| d_approach | base | 1 | specs/d_approach.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| d_near | base | 1 | specs/d_near.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| d_moved | base | 1 | specs/d_moved.json | trained |
| d_loosepot | base | 1 | specs/d_loosepot.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| d_potmoved | base | 1 | specs/d_potmoved.json | trained |
| d_chickloose | base | 1 | specs/d_chickloose.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| boil_note_fresh | base | 3 | specs/boil_note_fresh.json | trained 3 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| boil_note_moved | d_potmoved | 3 | specs/boil_note_moved.json | trained |
| o_drawer | base | 1 | specs/o_drawer.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| o_cab | base | 1 | specs/o_cab.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| o_fridge | base | 1 | specs/o_fridge.json | trained |
| m_ice_precise | base | 1 | specs/m_ice_precise.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |

- train job 35 (boil_note_fresh): note set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 36 (boil_note_moved): note set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## History (latest 30)

- train p_mw (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train p_tong (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train p_ice (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train p_straw (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train g_pot failed: train: reward file refused by the reward guard: syntax error line 28 (numpy and math are the only imports; no files, printing, dunder names or classes)
- train g_chick failed: train: reward file refused by the reward guard: syntax error line 28 (numpy and math are the only imports; no files, printing, dunder names or classes)
- train g_tong failed: train: reward file refused by the reward guard: syntax error line 28 (numpy and math are the only imports; no files, printing, dunder names or classes)
- train g_pot (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train g_chick (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train g_tong (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- cancel job 12
- train p_utensil cancelled: train cancelled; its job ended (JobFailed)
- train d_approach (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train d_near (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train d_moved (init base, steps 1): trained
- train d_loosepot (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train d_potmoved (init base, steps 1): trained
- train d_chickloose (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train boil_note_fresh (init base, steps 3): trained 3 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train boil_note_moved (init d_potmoved, steps 3): trained
- train o_drawer (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train o_cab (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train o_fridge (init base, steps 1): trained
- train m_ice_precise (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- eval p_boil on BoilPot: 0/20
- eval d_potmoved on BoilPot: 0/20
- eval d_moved on BoilPot: 0/20
- finish: submitted base (token a95113, job 49)
- finish: submitted p_boil (token 79bcf8, job 50)
- finish: confirmed p_boil (token 79bcf8)
