import numpy as np
SUBS = ['pot', 'pan']

def _v(x):
    try:
        a = np.asarray(x, dtype=float).ravel()
        return a if a.size == 3 else None
    except Exception:
        return None

def _box_of(reg):
    pts = []
    def walk(o):
        if isinstance(o, dict):
            for k, val in o.items():
                if k in ("p0","px","py","pz"):
                    v = _v(val)
                    if v is not None: pts.append(v)
                else: walk(val)
        elif isinstance(o, (list, tuple)):
            for e in o: walk(e)
    walk(reg)
    if len(pts) >= 2:
        return (np.minimum.reduce(pts), np.maximum.reduce(pts))
    return None

def _fx(state, *subs):
    out = []
    for name, f in (state.get("fixtures") or {}).items():
        if any(s in str(name).lower() for s in subs):
            out.append((name, f or {}))
    return out

def _center(name, state, *subs):
    for fn, f in _fx(state, *subs):
        for reg in (f.get("regions") or []):
            b = _box_of(reg)
            if b:
                return (_v((b[0] + b[1]) / 2.0))
    return None

def _target(state):
    for name, o in (state.get("objects") or {}).items():
        o = o or {}
        if any(s in name.lower() for s in SUBS):
            return o
    return None

def reward_fn(state):
    try:
        o = _target(state)
        if o is None:
            return 0
        p = _v(o.get("pos"))
        if p is None:
            return 0
        
        q = _v(o.get("init_pos"))
        if q is not None and float(np.linalg.norm(p - q)) > 0.03:
            return 1
        return 0

        return 0
    except Exception:
        return 0
