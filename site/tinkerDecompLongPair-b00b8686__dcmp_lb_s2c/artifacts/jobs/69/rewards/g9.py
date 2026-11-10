import math

def reward(r):
    # revstack, anchored: 0 at start/crash, 1.0 when released on top;
    # rewards HOLDING the green aligned over the red (0.8), punishes a premature drop.
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
        rs = list(red.get("size") or [0.05, 0.05, 0.05])
        gx, gy, gz = g["pos"]
        rx, ry, rz = red["pos"]
        dxy = math.hypot(gx - rx, gy - ry)
        zgap = gz - (rz + rs[2] / 2.0)
        gr = (fs.get("grippers") or {}).get("arm0") or {}
        held = "green_cube" in (gr.get("grasping") or [])
        lifted = gz > rz + 0.09
        above = max(0.0, 1.0 - dxy / 0.12)
        ontop = (dxy < 0.05) and (abs(zgap - gs[2] / 2.0) < 0.05)
        if ontop and not held:
            return 1.0
        if held and lifted:
            geo = 0.3 + 0.5 * above
        elif not held:
            # released: only close-to-on-top pays; a drop scores little
            zok = max(0.0, 1.0 - abs(zgap - gs[2] / 2.0) / 0.06)
            geo = 0.1 * above * (0.5 + 0.5 * zok)
    return min(1.0, 0.5 * stage_frac + 0.5 * geo)
