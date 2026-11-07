def reward_fn(state):
    o = state["objects"]
    tongs = [n for n in o if "tong" in n.lower()]
    if not tongs:
        return 0
    n = tongs[0]
    cts = o[n].get("contacts") or []
    return int(any(("counter" in c.lower() or "dining" in c.lower()) for c in cts))
