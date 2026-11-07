def reward_fn(state):
 try:
  objs=state.get("objects") or {}
  pot=None
  for n,o in objs.items():
   if "pot" in str(n).lower():
    pot=o; break
  if not pot: return 0
  def vec(keys):
   for k in keys:
    v=pot.get(k)
    if v is not None:
     try: return [float(v[0]),float(v[1]),float(v[2])]
     except: pass
   return None
  p=vec(["pos","position","position_world","pos_world"])
  ip=vec(["init_pos","init_position","initial_pos"])
  if p and ip:
   d=((p[0]-ip[0])**2+(p[1]-ip[1])**2+(p[2]-ip[2])**2)**0.5
   return int(d>0.40)
  return 0
 except Exception:
  return 0
