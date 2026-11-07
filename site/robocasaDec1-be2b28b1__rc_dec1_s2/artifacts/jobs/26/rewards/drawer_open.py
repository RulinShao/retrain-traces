def reward_fn(state):
 fixtures=state.get("fixtures") or {}
 best=0.0
 for fn,f in fixtures.items():
  if "drawer" not in str(fn).lower(): continue
  st=f.get("state") or {}
  for k,v in st.items():
   try: val=float(v)
   except: continue
   if 0.0<=val<=1.0: best=max(best,val)
 return int(best>0.5)
