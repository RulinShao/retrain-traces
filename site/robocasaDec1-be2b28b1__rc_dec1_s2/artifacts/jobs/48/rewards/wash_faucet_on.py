def reward_fn(state):
 fixtures=state.get("fixtures") or {{}}
 for fn,f in fixtures.items():
  nml=str(fn).lower()
  if not any(w in nml for w in ("sink","faucet","tap","basin")): continue
  st=f.get("state") or {{}}
  if not isinstance(st,dict): continue
  for k,v in st.items():
   kl=str(k).lower()
   if any(w in kl for w in ("on","faucet","tap","water","flow","open","running")):
    try: val=float(v)
    except: continue
    if val>0.5: return 1
 return 0
