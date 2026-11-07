def _v(o,ks):
 for k in ks:
  v=o.get(k) if isinstance(o,dict) else None
  if v is not None:
   try:
    return[float(v[0]),float(v[1]),float(v[2])]
   except Exception:pass
 return None
def reward_fn(state):
 try:
  objs=state.get("objects")
  if objs is None:return 0
  items=list(objs.items()) if isinstance(objs,dict) else [((o.get("name",str(i)) if isinstance(o,dict) else str(i)),o) for i,o in enumerate(objs)]
  best=0.0
  for n,o in items:
   if not isinstance(o,dict):continue
   p=_v(o,["pos","position","position_world","pos_base","pos_world"])
   ip=_v(o,["init_pos","init_position","initial_pos","initial_position","init_position_world"])
   if p and ip:
    d=((p[0]-ip[0])**2+(p[1]-ip[1])**2+(p[2]-ip[2])**2)**0.5
    best=max(best,d)
  return int(best>0.02)
 except Exception:
  return 0
