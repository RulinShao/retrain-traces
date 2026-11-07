def reward(r):
    if r.get('sandbox_rc') not in (0, None):
        return 0.0
    if (r.get('final_state') or {}).get('t', 0) <= 0:
        return 0.0
    if r.get('task_completed'):
        return 1.0
    stages = list((r.get('stages') or {}).values())
    k = 0
    for reached in stages:
        if not reached:
            break
        k += 1
    dense = max(0.0, min(1.0, float(r.get('sim_reward', r.get('reward', 0.0)))))
    return (k + 0.25 * dense) / (len(stages) + 1.0)
