import math

def reward(r):
    # Dense, monotone reward for revstack: 0 at start/crash, 1.0 on success,
    # continuous over lift -> align over red -> release close to on-top.
    if r.get("sandbox_rc") not in (0, None):
        return 0.0
    if r.get("task_completed"):
        return 1.0
    st = r.get("stages") or {}
    vals = list(st.values())
    stage_frac = (sum(1 for v in vals if v) / len(vals)) if vals else 0.0
    fs = r.get("final_state") or {}
    ob = fs.get("objects") or {}
    g = ob.get("green_cube")
    red = ob.get("red_cube")
    geo = 0.0
    if g and red:
        gs = list(g.get("size") or [0.04, 0.04, 0.04])
        rs = list(red.get("size") or [0.04, 0.04, 0.04])
        gx, gy, gz = g["pos"]
        rx, ry, rz = red["pos"]
        dxy = math.hypot(gx - rx, gy - ry)
        zgap = gz - (rz + rs[2] / 2.0)
        lifted = gz > rz + 0.09
        above = max(0.0, 1.0 - dxy / 0.15)
        zok = max(0.0, 1.0 - abs(zgap - gs[2] / 2.0) / 0.10)
        gr = (fs.get("grippers") or {}).get("arm0") or {}
        held = ("green_cube" in (gr.get("grasping") or [])) or (gr.get("opening", 0.1) < 0.03)
        if lifted:
            geo = above * (0.6 if held else 1.0)
            if not held:
                geo *= (0.5 + 0.5 * zok)
    return min(1.0, 0.55 * stage_frac + 0.45 * geo)
