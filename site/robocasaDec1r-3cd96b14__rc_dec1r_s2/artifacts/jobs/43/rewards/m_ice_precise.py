import numpy as np

def _fx(state, *subs):
    out = []
    for name, f in (state.get("fixtures") or {}).items():
        if any(s in str(name).lower() for s in subs):
            out.append((name, f or {}))
    return out

def _touch(o, *subs):
    for c in (o.get("contacts") or []):
        if any(s in str(c).lower() for s in subs):
            return True
    return False

def _objs(state, *subs):
    out = []
    for name, o in (state.get("objects") or {}).items():
        if any(s in name.lower() for s in subs):
            out.append(o or {})
    return out

def reward_fn(state):
    try:
        # lemon touches glass AND at least one ice touches glass
        lemons = _objs(state, "lemon")
        ices = _objs(state, "ice")
        lemon_ok = any(_touch(o, "glass", "cup") for o in lemons)
        ice_ok = any(_touch(o, "glass", "cup") for o in ices)
        return int(lemon_ok and ice_ok)
    except Exception:
        return 0
