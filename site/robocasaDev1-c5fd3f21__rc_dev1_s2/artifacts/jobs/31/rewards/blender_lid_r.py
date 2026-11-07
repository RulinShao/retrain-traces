
import math
def _c(triplet):
    try:
        return (sum(triplet[0])/4.0, sum(triplet[1])/4.0, sum(triplet[2])/4.0)
    except Exception:
        return None
def _dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])
def _fixture(state, words):
    for n, f in (state.get("fixtures") or {}).items():
        t = str(f.get("type") or "").lower(); nl = n.lower()
        if any(w in nl or w in t for w in words):
            return n, f
    return None, None
def _obj(state, words, notwords=()):
    for n, o in (state.get("objects") or {}).items():
        nl = n.lower()
        if any(w in nl for w in words) and not any(w in nl for w in notwords):
            return n, o
    return None, None
def _statevals(f):
    st = f.get("state") or {}
    ist = f.get("init_state") or {}
    return st, ist
def _any_on(f, words):
    st, ist = _statevals(f)
    if not isinstance(st, dict): return False
    for k, v in st.items():
        kl = str(k).lower()
        if isinstance(v, (int, float)) and float(v) >= 0.5 and any(w in kl for w in words):
            return True
    return False
def _any_off(f, words):
    st, ist = _statevals(f)
    if not isinstance(st, dict): return False
    for k, v in st.items():
        kl = str(k).lower()
        if isinstance(v, (int, float)) and float(v) <= 0.15 and any(w in kl for w in words):
            return True
    return False
def _region_centers(f):
    out = []
    for rk, rv in (f.get("regions") or {}).items():
        c = _c((rv.get("px"), rv.get("py"), rv.get("pz")))
        if c: out.append(c)
    return out
def _objpos(o):
    try: return [float(x) for x in o["pos"][:3]]
    except Exception: return None

def reward_fn(state):

    n, f = _fixture(state, ("blender",))
    if f is None: return 0
    st, ist = _statevals(f)
    if isinstance(st, dict):
        for k, v in st.items():
            if "lid" in str(k).lower() and isinstance(v, (int, float)):
                if float(v) <= 0.15:
                    return 1
    return 0
