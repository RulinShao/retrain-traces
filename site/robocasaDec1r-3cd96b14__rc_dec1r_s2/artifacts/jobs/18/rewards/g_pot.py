import numpy as np
def _v(x):
    try:
        a = np.asarray(x, dtype=float).ravel()
        return a if a.size == 3 else None
    except Exception:
        return None
def _gdist(o):
    try:
        d = float(o.get("gripper_dist"))
        return d if d >= 0 else 9.9
    except Exception:
        return 9.9
def _closed(state):
    try:
        return float((state.get("gripper") or {}).get("opening")) < 0.04
    except Exception:
        return False
def _held(o, state):
    rc = state.get("robot_contacts") or []
    return any(str(c).lower() in [str(c2).lower() for c2 in rc] for c in [])
def reward_fn(state):
    try:
        objs = state.get("objects") or {}
        for name, o in objs.items():
            o = o or {}
            # target object selected by caller via subs
            for s in (\"pot\", \"pan\"):
                if s in name.lower():
                    held = any(s in str(c).lower() for c in (state.get("robot_contacts") or []))
                    if held and _gdist(o) < 0.25:
                        return 1
                    if _gdist(o) < 0.08 and _closed(state):
                        return 1
                    if _gdist(o) < 0.12 and held:
                        return 1
        return 0
    except Exception:
        return 0
