import numpy as np
FIX = ['cabinet']

def reward_fn(state):
    try:
        fx = state.get("fixtures") or {}
        best = 0.0
        for name, f in fx.items():
            if not any(s in str(name).lower() for s in FIX):
                continue
            f = f or {}
            st = f.get("state") or {}
            for k, v in st.items():
                try:
                    val = float(v)
                    if val > best:
                        best = val
                except Exception:
                    pass
        return int(best > 0.4)
    except Exception:
        return 0
