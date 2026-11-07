def reward_fn(state):
    o = state["objects"]
    m = [n for n in o if "mug" in n.lower()]
    if not m: return 0
    cts = o[m[0]].get("contacts") or []
    return int(any("sink" in c.lower() for c in cts))
