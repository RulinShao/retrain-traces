def reward_fn(state):
 objs=state.get("objects") or {}
 b=None
 for n,o in objs.items():
  if "bowl" in str(n).lower(): b=(n,o);break
 if not b: return 0
 n,o=b
 contacts=o.get("contacts") or []
 if isinstance(contacts,dict): contacts=list(contacts.keys())
 for c in contacts:
  cl=str(c).lower()
  if any(w in cl for w in ("dining","counter","table")): return 1
 p=o.get("pos")
 if p is None: return 0
 return 0
