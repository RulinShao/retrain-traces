import numpy as np
SUBS = ['chicken','drumstick','meat']

def reward_fn(state):
    try:
        objs = state.get("objects") or {}
        closed = False
        try:
            closed = float((state.get("gripper") or {}).get("opening")) < 0.04
        except Exception:
            closed = False
        rc = [str(c).lower() for c in (state.get("robot_contacts") or [])]
        for name, o in objs.items():
            o = o or {}
            if not any(s in name.lower() for s in SUBS):
                continue
            try:
                d = float(o.get("gripper_dist"))
            except Exception:
                d = 9.9
            held = any(s in c for c in rc for s in SUBS)
            if d < 0.10 and closed and held:
                return 1
            if d < 0.06 and closed:
                return 1
        return 0
    except Exception:
        return 0
