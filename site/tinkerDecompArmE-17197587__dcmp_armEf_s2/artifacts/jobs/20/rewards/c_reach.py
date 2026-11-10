"""Multi-task [restack, nut] stage-reach reward v2. Dispatch on stage keys.
crash / no-op = 0. Ordered stage reach + continuous term at the current frontier.
"""


def _restack(fs, st, tc):
    def pos(n):
        try: return fs["objects"][n]["pos"]
        except Exception: return None
    def i0(n):
        try: return fs["objects"][n]["init_pos"]
        except Exception: return None
    red, red0 = pos("red_cube"), i0("red_cube")
    grn = pos("green_cube")
    if red is None or grn is None:
        return 0.0
    g = (fs.get("grippers") or {}).get("arm0") or {}
    gp, op = g.get("pos"), g.get("opening")
    def d3(a,b): return ((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)**0.5
    def dxy(a,b): return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    un = bool(st.get("unstack the green off the red"))
    under_green = (red[2] <= grn[2] + 0.03) and (dxy(red, grn) < 0.06)
    gr = bool(st.get("grasp the red"))
    if not gr and gp is not None:
        if (op is not None and op < 0.045) and d3(gp, red) < 0.10: gr = True
    if gr and (not un or under_green): gr = False
    lift = bool(st.get("lift the red"))
    if gr and red0 is not None:
        lift = lift or (red[2] > red0[2] + 0.05)
    elif not gr: lift = False
    align = bool(st.get("align the red over the green"))
    if gr and lift and not align:
        if dxy(red, grn) < 0.04 and red[2] > grn[2] + 0.01: align = True
    elif not (gr and lift): align = False
    place = tc or bool(st.get("place the red on the green"))
    if not place:
        on = (dxy(red, grn) < 0.035) and (0.02 <= red[2] - grn[2] <= 0.06)
        released = (op is None) or (op > 0.045)
        if on and released and gr and lift and align: place = True
    s = 0.02
    s += 0.10*(1.0 if un else 0.0)
    s += 0.35*(1.0 if gr else 0.0)
    if gr:
        s += 0.15*(1.0 if lift else 0.0)
    if gr and lift:
        s += 0.15*(1.0 if align else 0.0)
    if gr and lift and align:
        s += 0.23*(1.0 if place else 0.0)
    # frontier: approach the exposed red once unstacked (grasp not yet)
    if un and not gr and gp is not None:
        s += 0.15*max(0.0, 1.0 - d3(gp, red)/0.20)
    return s


def _nut(fs, st, tc):
    def obj(n):
        try: return fs["objects"][n]
        except Exception: return None
    nut = obj("square_nut"); peg = obj("square_peg")
    if nut is None or peg is None:
        return 0.0
    h = nut.get("handle_pos") or nut.get("pos")
    np_ = nut.get("pos"); pp = peg.get("pos")
    nut0 = nut.get("init_pos") or np_
    g = (fs.get("grippers") or {}).get("arm0") or {}
    gp, op = g.get("pos"), g.get("opening")
    def d3(a,b): return ((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)**0.5
    def dxy(a,b): return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    reach = bool(st.get("reach the handle"))
    reach_cont = max(0.0, min(1.0, 1.0 - d3(gp, h)/0.75)) if gp is not None else 0.0
    if gp is not None and not reach and d3(gp, h) < 0.12: reach = True
    grasp = bool(st.get("grasp the nut"))
    if not grasp and gp is not None:
        if (op is not None and op < 0.045) and d3(gp, h) < 0.14 and np_ is not None: grasp = True
    if not grasp and nut0 is not None:
        if (np_[2] > nut0[2] + 0.04) and gp is not None and d3(gp, np_) < 0.15: grasp = True
    if not reach: grasp = False
    align = bool(st.get("align the nut over the peg"))
    align_cont = 0.0
    if grasp:
        if not align:
            if dxy(np_, pp) < 0.05 and np_[2] > pp[2] - 0.05: align = True
        # continuous: move grasped nut up and over the peg
        align_cont = max(0.0, min(1.0, 1.0 - dxy(np_, pp)/0.30)) * (1.0 if np_[2] > pp[2] - 0.10 else 0.0)
    if not grasp: align = False
    insert = tc or bool(st.get("insert the nut"))
    s = 0.02
    s += 0.10*(1.0 if reach else 0.0)
    s += 0.08*reach_cont
    if reach: s += 0.20*(1.0 if grasp else 0.0)
    if grasp:
        s += 0.10*(1.0 if align else 0.0)
        s += 0.12*align_cont
    if grasp and align: s += 0.38*(1.0 if insert else 0.0)
    return s


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
    if any(k in st for k in ("unstack the green off the red", "grasp the red", "place the red on the green")):
        out = _restack(fs, st, tc)
    elif any(k in st for k in ("reach the handle", "grasp the nut", "insert the nut", "align the nut over the peg")):
        out = _nut(fs, st, tc)
    else:
        out = 0.0
    tz = fs.get("table_z")
    if tz is not None:
        for v in fs["objects"].values():
            try:
                if v["pos"][2] < tz - 0.02:
                    out = min(out, 0.05)
            except Exception:
                pass
    return out
