def reward_fn(state):
    if isinstance(state, dict):
        objs = state.get("objects")
        if isinstance(objs, dict) and len(objs) > 0:
            return 1.0
        fx = state.get("fixtures")
        if isinstance(fx, dict) and len(fx) > 0:
            return 0.5
        rl = state.get("reward")
        if isinstance(rl,(int,float)) and rl>0:
            return 0.25
        if state.get("task_completed"):
            return 0.1
    return 0.0
