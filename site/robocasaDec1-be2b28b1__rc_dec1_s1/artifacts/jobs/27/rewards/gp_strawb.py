def reward_fn(state):
    o = state["objects"]
    s = [n for n in o if "strawb" in n.lower()]
    if not s: return 0
    cts = o[s[0]].get("contacts") or []
    return int(any(("pancake" in c.lower() or "pan" in c.lower()) for c in cts))
