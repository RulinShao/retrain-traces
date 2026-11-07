def reward_fn(state):
 objs=state.get("objects") or {}
 breads=[o for n,o in objs.items() if "bread" in str(n).lower()]
 if not breads: return 0
 for o in breads:
  contacts=o.get("contacts") or []
  if isinstance(contacts,dict): contacts=list(contacts.keys())
  if not any("bowl" in str(c).lower() for c in contacts):
   return 0
 return 1
