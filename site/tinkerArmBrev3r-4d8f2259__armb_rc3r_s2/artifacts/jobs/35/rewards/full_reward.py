def _g(r, k, d=None):
    return r.get(k, d) if isinstance(r, dict) else getattr(r, k, d)

def reward(r):
    st = _g(r, "stages", {}) or {}
    if not isinstance(st, dict):
        st = {}
    u = 1.0 if st.get("unstack the green off the red") else 0.0
    g = 1.0 if st.get("grasp the red") else 0.0
    l = 1.0 if st.get("lift the red") else 0.0
    a = 1.0 if st.get("align the red over the green") else 0.0
    p = 1.0 if st.get("place the red on the green") else 0.0
    d = 1.0 if _g(r, "task_completed", False) else 0.0
    # Stage credit (spread at the base's reachable level) + dominant strict-success term.
    return 0.5 * d + 0.12 * (u + g + l + a + p)
