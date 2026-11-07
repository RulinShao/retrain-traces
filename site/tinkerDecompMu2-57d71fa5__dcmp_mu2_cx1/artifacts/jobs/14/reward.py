def reward(r):
    if r.get('sandbox_rc') not in (0, None):
        return 0.0
    if r.get('task_completed'):
        return 1.0
    if (r.get('final_state') or {}).get('t', 0) <= 0:
        return 0.0
    stages = list((r.get('stages') or {}).values())
    reached = 0
    for value in stages:
        if not value:
            break
        reached += 1
    return 0.8 * reached / max(1, len(stages))
