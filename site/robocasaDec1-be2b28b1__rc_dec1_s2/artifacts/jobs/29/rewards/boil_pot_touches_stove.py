def reward_fn(state):
 objs=state.get("objects") or {}
 fixtures=state.get("fixtures") or {}
 pot=None
 for n,o in objs.items():
  if "pot" in str(n).lower(): pot=o; break
 if not pot: return 0
 contacts=pot.get("contacts") or []
 if isinstance(contacts,dict): contacts=list(contacts.keys())
 for c in contacts:
  cl=str(c).lower()
  if any(w in cl for w in ("stove","burner","range","cooktop","hob")): return 1
 p=pot.get("pos")
 if p is None: return 0
 px,py=float(p[0]),float(p[1])
 for fn,f in fixtures.items():
  nml=str(fn).lower()
  if not any(w in nml for w in ("stove","burner","range","cooktop","hob")): continue
  regs=f.get("regions") or {}
  rl=list(regs.values()) if isinstance(regs,dict) else list(regs)
  for r in rl:
   if not isinstance(r,dict): continue
   for k in ("p0","px","py","pz"):
    v=r.get(k)
    if v:
     try: x,y=float(v[0]),float(v[1])
     except: continue
     if ((px-x)**2+(py-y)**2)**0.5<0.15: return 1
 return 0
