# Ordered stage-reach reward for restack (real start).
# Subtask order (sim checklist): unstack the green off the red, grasp the red, lift the red, align the red over the green, place the red on the green
# crash -> 0.  Continuous frontier term: approach distance to the object + close-near-object.
import math

ORDER = ['unstack the green off the red', 'grasp the red', 'lift the red', 'align the red over the green', 'place the red on the green']
D0 = 0.3          # gripper-to-object distance normalization
CLOSE_D = 0.06  # "close enough to have grasped"
GRIP = "arm0"
OBJ = "red_cube"

def _get(d, k, default=None):
    if d is None: return default
    if isinstance(d, dict): return d.get(k, default)
    return getattr(d, k, default)

def _dist(a, b):
    try:
        return math.sqrt(sum((float(x)-float(y))**2 for x, y in zip(a, b)))
    except Exception:
        return None

def _grip_obj(f):
    g = _get(f, "grippers", {})
    o = _get(f, "objects", {})
    gg = g.get(GRIP) if isinstance(g, dict) else getattr(g, GRIP, None)
    og = o.get(OBJ) if isinstance(o, dict) else getattr(o, OBJ, None)
    gp = _get(gg, "pos", None); op = _get(og, "pos", None)
    closed = _get(gg, "closed_cmd", None)
    return gp, op, closed

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
    dmin = None; closed_near = 0.0
    if pts:
        for f in pts:
            gp, op, closed = _grip_obj(f)
            d = _dist(gp, op)
            if d is not None:
                if dmin is None or d < dmin: dmin = d
                if closed and d < CLOSE_D: closed_near = 1.0
    approach = 0.0
    if dmin is not None:
        approach = max(0.0, min(1.0, 1.0 - dmin / D0))
    cont = 0.7 * approach + 0.3 * closed_near
    return 0.5 * base + 0.5 * cont
