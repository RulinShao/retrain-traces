def reward_fn(state):
 fixtures=state.get("fixtures") or {}
 for fn,f in fixtures.items():
  if "microwave" not in str(fn).lower(): continue
  st=f.get("state") or {}
  for k,v in st.items():
   kl=str(k).lower()
   if any(w in kl for w in ("on","button","start","power","switch","lever","cook")):
    try: val=float(v)
    except: continue
    if val>0.5: return 1
 return 0
