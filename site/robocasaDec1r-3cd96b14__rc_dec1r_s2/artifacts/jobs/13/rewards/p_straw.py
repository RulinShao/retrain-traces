import numpy as np
def _v(x):
    try:
        a = np.asarray(x, dtype=float).ravel()
        if a.size == 3:
            return a
    except Exception:
        pass
    return None
def _box_of(reg):
    pts = []
    def walk(o):
        if isinstance(o, dict):
            for k, val in o.items():
                if k in ("p0", "px", "py", "pz"):
                    v = _v(val)
                    if v is not None:
                        pts.append(v)
                else:
                    walk(val)
        elif isinstance(o, (list, tuple)):
            for e in o:
                walk(e)
    walk(reg)
    if len(pts) >= 2:
        return (np.minimum.reduce(pts), np.maximum.reduce(pts))
    return None
def _inside(pos, reg):
    b = _box_of(reg)
    if b is None:
        return False
    lo, hi = b
    p = _v(pos)
    if p is None:
        return False
    return bool(np.all(p >= lo - 0.02) and np.all(p <= hi + 0.02))
def _fx(state, *subs):
    out = []
    fx = state.get("fixtures") or {}
    for name, f in fx.items():
        if any(s in str(name).lower() for s in subs):
            out.append((name, f or {}))
    return out
def _touch(contacts, *subs):
    for c in (contacts or []):
        cs = str(c).lower()
        if any(s in cs for s in subs):
            return True
    return False
def _hdist(a, b):
    pa, pb = _v(a), _v(b)
    if pa is None or pb is None:
        return 9.9
    d = pa - pb
    return float(np.sqrt(d[0]*d[0] + d[1]*d[1]))
def _obj_by(state, *subs, excl=()):
    out = []
    objs = state.get("objects") or {}
    for name, o in objs.items():
        n = str(name).lower()
        if any(s in n for s in subs) and not any(e in n for e in excl):
            out.append((name, o or {}))
    return out

def reward_fn(state):
    try:
        cakes = [o for _, o in _obj_by(state, "pancake")]
        for name, o in _obj_by(state, "strawberry", "fruit"):
            for c in cakes:
                if _hdist(o.get("pos"), c.get("pos")) < 0.7:
                    return 1
            if _touch(o.get("contacts"), "pancake", "plate"):
                return 1
        return 0
    except Exception:
        return 0
