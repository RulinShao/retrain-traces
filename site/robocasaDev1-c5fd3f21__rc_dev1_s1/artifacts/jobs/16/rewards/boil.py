import numpy as np

def _region_contains(r, pos, tol=0.06):
    try:
        p0 = np.asarray(r["p0"], dtype=float)
        px = np.asarray(r["px"], dtype=float)
        py = np.asarray(r["py"], dtype=float)
        pz = np.asarray(r["pz"], dtype=float)
        d = np.asarray(pos, dtype=float) - p0
        nx = px @ px; ny = py @ py; nz = pz @ pz
        if min(nx, ny, nz) < 1e-9:
            return False
        u = (d @ px) / nx; v = (d @ py) / ny; w = (d @ pz) / nz
        return (-tol <= u <= 1+tol) and (-tol <= v <= 1+tol) and (-tol <= w <= 1+tol)
    except Exception:
        return False

def reward_fn(state):
    try:
        objs = state.get("objects") or {}
        fixtures = state.get("fixtures") or {}
        pot = None
        for name, o in objs.items():
            if "pot" in name.lower():
                pot = (name, o)
        stove = None
        for name, f in fixtures.items():
            if "stove" in name.lower() or "stove" in str(f.get("type", "")).lower():
                stove = (name, f)
        s = 0.0
        if pot is not None and stove is not None:
            pname, po = pot
            sname, sf = stove
            contacts = " ".join(po.get("contacts") or []).lower()
            on_stove = ("stove" in contacts) or (sname.lower() in contacts)
            if not on_stove:
                for rname, r in (sf.get("regions") or {}).items():
                    if _region_contains(r, po.get("pos")):
                        on_stove = True
            if on_stove:
                s += 0.5
            st = sf.get("state") or {}
            if any(("burner" in k.lower()) and (float(v or 0) > 0.5) for k, v in st.items()):
                s += 0.5
        return float(s)
    except Exception:
        return 0.0
