import math

def reward(r):
    """Wipe practice score: 0.5 * the simulator's own staged reward (un-gameable:
    computed by the sim from the true scene) + 0.4 * a partial-credit ladder over
    the program's OWN printed 'WV:' pipeline lines (segment -> unproject grid ->
    2-D press grid). 1.0 only when the simulator's own success check passed,
    which strictly dominates everything else. Parse failures score 0.0.
    """
    try:
        return _score(r)
    except Exception:
        return 0.0


def _score(r):
    try:
        tc = r["task_completed"]
    except Exception:
        tc = False
    if tc:
        return 1.0
    try:
        staged = float(r.get("reward") or 0.0)
    except Exception:
        staged = 0.0
    if not math.isfinite(staged):
        staged = 0.0
    staged = min(max(staged, 0.0), 1.0)
    return float(min(0.5 * staged + 0.4 * _ladder(r), 0.95))


def _ladder(r):
    log = r.get("log_tail")
    if log is None:
        return 0.0
    if isinstance(log, bytes):
        log = log.decode("utf-8", "replace")
    wv = []
    for line in str(log).splitlines():
        s = line.strip()
        if s.startswith("WV:"):
            wv.append(s[3:].strip())
    if not wv:
        return 0.0
    score = 0.05
    seg_ok = False
    grid_ok = False
    good = 0
    pts = set()
    js = set()
    for s in wv:
        if s.startswith("mask"):
            b = _nums(_tok(s, "box"))
            if b is not None and len(b) == 4 and b[2] - b[0] >= 5 and b[3] - b[1] >= 5:
                seg_ok = True
        elif s.startswith("grid"):
            c = _nums(_tok(s, "center"))
            sz = _nums(_tok(s, "size"))
            if c is not None and sz is not None and len(c) == 2 and len(sz) == 2 \
                    and all(math.isfinite(v) for v in c + sz) and sz[0] >= 0.03 and sz[1] >= 0.03:
                grid_ok = True
        elif s.startswith("wipe"):
            x = _nums(_tok(s, "x"))
            y = _nums(_tok(s, "y"))
            z = _nums(_tok(s, "z"))
            q = _nums(_tok(s, "q"))
            j = _nums(_tok(s, "j"))
            if x is not None and y is not None and z is not None and q is not None and j is not None \
                    and len(x) == 1 and len(y) == 1 and len(z) == 1 and len(q) == 4 and len(j) == 7 \
                    and math.isfinite(x[0]) and math.isfinite(y[0]) and math.isfinite(z[0]) \
                    and -0.02 <= z[0] <= 0.04 and q[0] >= 0.9 \
                    and all(math.isfinite(v) and abs(v) <= 3.0 for v in j):
                good += 1
                pts.add((round(x[0], 3), round(y[0], 3)))
                js.add(tuple(round(v, 2) for v in j))
    if seg_ok:
        score = max(score, 0.20)
    if grid_ok:
        score = max(score, 0.30)
    uniq = len(pts)
    if good > 0:
        score = max(score, 0.30 + 0.35 * min(uniq, 4) / 4.0)
    done = any(s.startswith("done") and _nums(_tok(s, "moves")) is not None for s in wv)
    if done and good >= 8 and uniq >= 4 and len(js) >= 2:
        score = max(score, 0.80)
    if done and good >= 8 and uniq >= 8 and len(js) >= 4:
        score = max(score, 0.90)
    return float(min(score, 0.90))


def _tok(s, key):
    for part in s.split():
        if part.startswith(key + "="):
            return part[len(key) + 1:]
    return None


def _nums(v):
    if v is None:
        return None
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        v = v[1:-1]
    out = []
    for t in v.split(","):
        t = t.strip()
        if not t:
            continue
        try:
            out.append(float(t))
        except Exception:
            return None
    return out if out else None
