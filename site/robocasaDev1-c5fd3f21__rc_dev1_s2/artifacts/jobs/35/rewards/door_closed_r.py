import math
def _statevals(f):
    return (f.get("state") or {}), (f.get("init_state") or {})
def reward_fn(state):
    for n, f in (state.get("fixtures") or {}).items():
        nl = n.lower(); t = str(f.get("type") or "").lower()
        if ("cabinet" in nl or "cabinet" in t or "fridge" in nl or "fridge" in t or "oven" in nl):
            st, ist = _statevals(f)
            if isinstance(st, dict):
                for k, v in st.items():
                    if "door" in str(k).lower() and isinstance(v, (int, float)) and float(v) <= 0.15:
                        return 1
    return 0
