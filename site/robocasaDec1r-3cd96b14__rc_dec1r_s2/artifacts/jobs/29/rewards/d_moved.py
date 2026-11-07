import numpy as np
TGT = []

def _v(x):
    try:
        a = np.asarray(x, dtype=float).ravel()
        return a if a.size == 3 else None
    except Exception:
        return None

def _gd(o):
    try:
        d = float(o.get("gripper_dist")); return d if d >= 0 else 9.9
    except Exception:
        return 9.9

def reward_fn(state):
    try:
        objs = state.get("objects") or {}
        
        for name, o in objs.items():
            o = o or {}
            p = _v(o.get("pos")); q = _v(o.get("init_pos"))
            if p is None or q is None: continue
            d = float(np.linalg.norm(p - q))
            if d > 0.03:
                return 1
        return 0

        return 0
    except Exception:
        return 0
