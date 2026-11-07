# Ordered stage-reach reward for nut (real start).
# Subtask order (sim checklist): reach the handle, grasp the nut, align the nut over the peg, insert the nut
# crash -> 0.  Continuous term: (a) approach to target (nut or peg) in absolute terms,
# (b) fraction of the initial gripper-to-target distance closed (separates a no-op from a moving program).
import math

ORDER = ["reach the handle", "grasp the nut", "align the nut over the peg", "insert the nut"]
D0 = 0.30          # absolute approach normalization
GRIP = "arm0"
TARGETS = ["square_nut", "square_peg"]   # handle is part of square_nut; insertion targets the peg

def _get(d, k, default=None):
    if d is None: return default
    if isinstance(d, dict): return d.get(k, default)
    return getattr(d, k, default)

def _dist(a, b):
    try:
        return math.sqrt(sum((float(x)-float(y))**2 for x, y in zip(a, b)))
    except Exception:
        return None

def _frame(f):
    g = _get(f, "grippers", {})
    o = _get(f, "objects", {})
    gg = g.get(GRIP) if isinstance(g, dict) else getattr(g, GRIP, None)
    gp = _get(gg, "pos", None)
    closed = _get(gg, "closed_cmd", None)
    tpos = {}
    for t in TARGETS:
        og = o.get(t) if isinstance(o, dict) else getattr(o, t, None)
        tpos[t] = _get(og, "pos", None)
    return gp, tpos, closed

def reward(r):
    rc = _get(r, "sandbox_rc", 0)
    if rc not in (0, None):
        return 0.0
    stages = _get(r, "stages", {}) or {}
    depth = 0
    for i, name in enumerate(ORDER):
        if stages.get(name):
            depth = i + 1
        else:
            break
    base = depth / len(ORDER)

    trace = _get(r, "trace", None)
    pts = None
    if isinstance(trace, dict): pts = trace.get("points", None)
    elif isinstance(trace, list): pts = trace
    if not pts:
        return 0.5 * base   # no trace: only stage credit

    dmin_abs = None          # min distance to any target over the episode
    dstart = None            # distance to any target at the first frame
    for j, f in enumerate(pts):
        gp, tpos, closed = _frame(f)
        ds = [d for d in (_dist(gp, tpos[t]) for t in TARGETS) if d is not None]
        if not ds:
            continue
        m = min(ds)
        if j == 0:
            dstart = m
        if dmin_abs is None or m < dmin_abs:
            dmin_abs = m

    approach = 0.0
    if dmin_abs is not None:
        approach = max(0.0, min(1.0, 1.0 - dmin_abs / D0))
    closed_frac = 0.0
    if dstart and dmin_abs is not None:
        closed_frac = max(0.0, min(1.0, (dstart - dmin_abs) / dstart))
    cont = 0.4 * approach + 0.6 * closed_frac
    return 0.5 * base + 0.5 * cont + 0.03   # +0.03: produced executable code (crash=0 < valid); progress terms dominate once code is valid
