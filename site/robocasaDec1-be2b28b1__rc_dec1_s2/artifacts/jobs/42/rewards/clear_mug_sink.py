def reward_fn(state):
 objs=state.get("objects") or {}
 b=None
 for n,o in objs.items():
  if any(w in str(n).lower() for w in ['mug', 'cup']): b=(n,o);break
 if not b: return 0
 o=b[1]
 contacts=o.get("contacts") or []
 if isinstance(contacts,dict): contacts=list(contacts.keys())
 return int(any(w in str(c).lower() for c in contacts for w in ['sink']))
