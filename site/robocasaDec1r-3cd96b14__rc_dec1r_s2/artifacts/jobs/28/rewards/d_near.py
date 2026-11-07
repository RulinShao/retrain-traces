import numpy as np
TGT = ['pot', 'pan']

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
        
        best = 9.9
        for name, o in objs.items():
            if any(s in name.lower() for s in ['pot', 'pan']):
                best = min(best, _gd(o or {}))
        return int(best < 0.15)

        return 0
    except Exception:
        return 0
