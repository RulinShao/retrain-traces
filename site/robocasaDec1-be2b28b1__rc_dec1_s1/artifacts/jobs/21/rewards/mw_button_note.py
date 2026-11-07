def reward_fn(state):
    fx = state["fixtures"].get("microwave") or {}
    st = fx.get("state") or {}
    return int(bool(st) and max(st.values()) > 0.5)
