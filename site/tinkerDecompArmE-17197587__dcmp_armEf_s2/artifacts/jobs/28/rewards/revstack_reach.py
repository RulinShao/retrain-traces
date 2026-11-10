"""revstack stage-reach reward v3 (ordered; crash/no-op=0; continuous terms across
the whole chain so pressure stays on the current frontier).
frontier after ~15 steps was lift; keep pushing lift -> align -> place.
"""

def reward(r):
    try:
        if float(r.get("sandbox_rc")) != 0.0:
            return 0.0
    except (TypeError, ValueError):
        return 0.0
    fs = r.get("final_state")
    if not isinstance(fs, dict) or not fs.get("objects"):
        return 0.0
    st = r.get("stages") or {}
    tc = bool(r.get("task_completed"))

    def pos(n):
        try: return fs["objects"][n]["pos"]
        except Exception: return None
    def i0(n):
        try: return fs["objects"][n]["init_pos"]
        except Exception: return None
    grn, grn0 = pos("green_cube"), i0("green_cube")
    red, red0 = pos("red_cube"), i0("red_cube")
    if grn is None or red is None:
        return 0.0
    g = (fs.get("grippers") or {}).get("arm0") or {}
    gp, op = g.get("pos"), g.get("opening")

    def d3(a, b): return ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2) ** 0.5
    def dxy(a, b): return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

    reach = bool(st.get("reach the green_cube"))
    if not reach and gp is not None and d3(gp, grn) < 0.12:
        reach = True

    grasp = bool(st.get("grasp the green_cube"))
    if not grasp and gp is not None:
        if (op is not None and op < 0.045) and d3(gp, grn) < 0.12:
            grasp = True

    lift = bool(st.get("lift the green_cube"))
    lift_cont = 0.0
    if grasp and grn0 is not None:
        rise = grn[2] - grn0[2]
        lift_cont = max(0.0, min(1.0, rise / 0.08))
        if not lift and rise > 0.05 and dxy(grn, gp) < 0.10:
            lift = True
    if not grasp:
        lift = False; lift_cont = 0.0

    align = bool(st.get("align the green_cube over the red_cube"))
    align_cont = 0.0
    if grasp and lift:
        if not align:
            if dxy(grn, red) < 0.04 and grn[2] > red[2] + 0.02:
                align = True
        # while holding+lifted, move green toward directly above the red
        align_cont = max(0.0, min(1.0, 1.0 - dxy(grn, red)/0.35))
    elif not (grasp and lift):
        align = False; align_cont = 0.0

    place = tc or bool(st.get("place the green_cube on the red_cube"))
    place_cont = 0.0
    if grasp and lift and align and not place:
        # green on red (5cm): center delta ~0.045; lower from above onto it
        target = red[2] + 0.045
        over = 0.0 if (grn[2] > target) else 1.0
        near = max(0.0, min(1.0, 1.0 - abs(grn[2] - target)/0.05))
        place_cont = 0.5*over + 0.5*near
    elif not (grasp and lift and align):
        place_cont = 0.0
    if not place:
        on = (dxy(grn, red) < 0.035) and (0.025 <= grn[2] - red[2] <= 0.085)
        released = (op is None) or (op > 0.045)
        if on and released and grasp and lift and align:
            place = True

    score = 0.02
    score += 0.05 * (1.0 if reach else 0.0)
    score += 0.10 * (1.0 if grasp else 0.0)
    if grasp:
        score += 0.15 * (1.0 if lift else 0.0)
        score += 0.08 * lift_cont
    if grasp and lift:
        score += 0.07 * (1.0 if align else 0.0)
        score += 0.08 * align_cont
    if grasp and lift and align:
        score += 0.35 * (1.0 if place else 0.0)
        score += 0.08 * place_cont

    tz = fs.get("table_z")
    if tz is not None:
        for v in fs["objects"].values():
            try:
                if v["pos"][2] < tz - 0.02:
                    return min(score, 0.05)
            except Exception:
                pass
    return score
