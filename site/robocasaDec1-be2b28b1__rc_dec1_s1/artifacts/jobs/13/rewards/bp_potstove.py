def reward_fn(state):
    for name, o in state["objects"].items():
        cts = o.get("contacts") or []
        if any("stove" in c.lower() for c in cts):
            return 1
    return 0
