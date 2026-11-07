def reward_fn(state):
    st = state["fixtures"].get("stove") or {}
    regions = st.get("regions") or []
    pts = []
    for r in regions:
        for k in ("p0", "px", "py", "pz"):
            v = r.get(k)
            if v and len(v) >= 3:
                pts.append(v[:3])
    o = state["objects"]
    pots = [n for n in o if "pot" in n.lower() or "saucepan" in n.lower() or "pan" in n.lower()]
    return int(bool(pts) and bool(pots))
