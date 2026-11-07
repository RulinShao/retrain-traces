def reward_fn(state):
    fx = state["fixtures"].get("microwave") or {}
    st = fx.get("state") or {}
    for k, v in st.items():
        if "door" in k.lower():
            return int(v > 0.5)
    return int(bool(st) and max(st.values()) > 0.5)
