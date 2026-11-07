def reward_fn(state):
 try:
  objs=state.get("objects") or {}
  fixtures=state.get("fixtures") or {}
  pot=None
  for n,o in objs.items():
   if "pot" in str(n).lower():
    pot=o; break
  if not pot: return 0
  p=pot.get("pos")
  if p is None: return 0
  px,py=float(p[0]),float(p[1])
  pts=[]
  for fn,f in fixtures.items():
   nm=str(fn).lower()
   if ("stove" in nm) or ("burner" in nm) or ("range" in nm) or ("hob" in nm) or ("cooktop" in nm):
    regs=f.get("regions") or {}
    rl=list(regs.values()) if isinstance(regs,dict) else list(regs)
    for r in rl:
     if not isinstance(r,dict): continue
     for k in ("p0","px","py","pz"):
      v=r.get(k)
      if v:
       try: pts.append([float(v[0]),float(v[1])])
       except: pass
  if not pts: return 0
  best=min(((px-x)**2+(py-y)**2)**0.5 for x,y in pts)
  return int(best<0.30)
 except Exception:
  return 0
