"""restack stage-reach reward (ordered; crash/no-op=0; continuous approach to frontier).
frontier = grasp the red (0/16). prerequisite = unstack green off red (12/16).
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
    red, red0 = pos("red_cube"), i0("red_cube")
    grn, grn0 = pos("green_cube"), i0("green_cube")
    if red is None or grn is None:
        return 0.0
    g = (fs.get("grippers") or {}).get("arm0") or {}
    gp, op = g.get("pos"), g.get("opening")

    def d3(a, b): return ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2) ** 0.5
    def dxy(a, b): return ((a[0]-b[0])**2 + (a[1]-b[1])**2) ** 0.5

    un = bool(st.get("unstack the green off the red"))
    under_green = (red[2] <= grn[2] + 0.03) and (dxy(red, grn) < 0.06)
    gr = bool(st.get("grasp the red"))
    if not gr and gp is not None:
        closed = (op is not None) and (op < 0.045)
        if closed and d3(gp, red) < 0.10:
            gr = True
    if gr and (not un or under_green):
        gr = False  # red must be exposed before it counts as the grasp

    lift = bool(st.get("lift the red"))
    if gr and red0 is not None:
        lift = lift or (red[2] > red0[2] + 0.05)
    elif not gr:
        lift = False

    align = bool(st.get("align the red over the green"))
    if gr and lift and not align:
        if dxy(red, grn) < 0.04 and red[2] > grn[2] + 0.01:
            align = True
    elif not (gr and lift):
        align = False

    place = tc or bool(st.get("place the red on the green"))
    if not place:
        on = (dxy(red, grn) < 0.035) and (0.02 <= red[2] - grn[2] <= 0.06)
        released = (op is None) or (op > 0.045)
        if on and released and gr and lift and align:
            place = True

    score = 0.0
    score += 0.15 * (1.0 if un else 0.0)
    score += 0.35 * (1.0 if gr else 0.0)
    if gr:
        score += 0.10 * (1.0 if lift else 0.0)
    if gr and lift:
        score += 0.10 * (1.0 if align else 0.0)
    if gr and lift and align:
        score += 0.30 * (1.0 if place else 0.0)
    # continuous approach to the frontier (grasp red) once red is exposed
    if un and not gr and gp is not None:
        score += 0.12 * max(0.0, 1.0 - d3(gp, red) / 0.25)

    tz = fs.get("table_z")
    if tz is not None:
        for v in fs["objects"].values():
            try:
                if v["pos"][2] < tz - 0.02:
                    return min(score, 0.05)
            except Exception:
                pass
    return score
