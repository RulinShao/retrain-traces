def reward_fn(state):
 objs=state.get("objects") or {{}}
 for n,o in objs.items():
  nl=str(n).lower()
  if any(w in nl for w in ("orange","mango","kiwi","fruit","lemon","wedge")):
   contacts=o.get("contacts") or []
   if isinstance(contacts,dict): contacts=list(contacts.keys())
   if any("colander" in str(c).lower() for c in contacts): return 1
 return 0
