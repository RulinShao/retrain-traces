import numpy as np
def _get(r, k, d=None):
    try:
        if hasattr(r, "get"):
            return r.get(k, d)
    except Exception:
        pass
    try:
        return getattr(r, k, d)
    except Exception:
        return d

def _disp(o):
    p = o.get("pos"); ip = o.get("init_pos")
    if not (p and ip):
        return 0.0
    return abs(p[0]-ip[0]) + abs(p[1]-ip[1]) + abs(p[2]-ip[2])

def _stack(o_top, o_bot, min_move):
    if not o_top or not o_bot:
        return 0.0
    if _disp(o_top) < min_move:      # top cube was not really manipulated
        return 0.0
    p = o_top.get("pos"); t = o_bot.get("pos")
    if not (p and t):
        return 0.0
    dxy = float(np.hypot(p[0]-t[0], p[1]-t[1]))
    st = o_top.get("size", [0.04, 0.04, 0.04]); sb = o_bot.get("size", [0.05, 0.05, 0.05])
    top_bottom = p[2] - st[2]/2.0; bot_top = t[2] + sb[2]/2.0
    on_top = (-0.008 < top_bottom - bot_top) and (top_bottom - bot_top < 0.04)
    s = 0.12 + 0.55 * max(0.0, 1.0 - dxy/0.12)
    if on_top and dxy < 0.06:
        s += 0.28
    return s

def reward(r):
    rc = _get(r, "sandbox_rc")
    if rc is not None and rc != 0:
        return 0.0
    fs = _get(r, "final_state")
    if not fs:
        return 0.0
    o = _get(fs, "objects", {}) or {}
    red = o.get("red_cube"); grn = o.get("green_cube")
    if red is None or grn is None:
        return 0.0
    a = _stack(grn, red, 0.03)   # green on red (revstack goal); green must be moved
    b = _stack(red, grn, 0.03)   # red on green (restack goal); red must be moved
    best = max(a, b)
    if best < 0.01:
        return 0.0
    tc = _get(r, "task_completed")
    if tc:
        return 1.0
    return float(min(1.0, max(0.0, best)))
