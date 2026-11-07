def reward_fn(state):
    o = state["objects"]
    l = [n for n in o if "lemon" in n.lower() or "wedge" in n.lower()]
    if not l: return 0
    cts = o[l[0]].get("contacts") or []
    return int(any("glass" in c.lower() for c in cts))
