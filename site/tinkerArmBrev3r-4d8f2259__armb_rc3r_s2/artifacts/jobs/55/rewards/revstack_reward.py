def _g(r, k, d=None):
    return r.get(k, d) if isinstance(r, dict) else getattr(r, k, d)

def reward(r):
    st = _g(r, "stages", {}) or {}
    if not isinstance(st, dict):
        st = {}
    reach = 1.0 if st.get("reach the green_cube") else 0.0
    grasp = 1.0 if st.get("grasp the green_cube") else 0.0
    lift  = 1.0 if st.get("lift the green_cube") else 0.0
    align = 1.0 if st.get("align the green_cube over the red_cube") else 0.0
    place = 1.0 if st.get("place the green_cube on the red_cube") else 0.0
    done  = 1.0 if _g(r, "task_completed", False) else 0.0
    # Emphasize grasp (the foothold) and the tail; dominant strict-success term. No-op from raw start = 0.
    return min(1.0, 0.35 * done + 0.25 * grasp + 0.20 * lift + 0.20 * align + 0.25 * place + 0.05 * reach)
