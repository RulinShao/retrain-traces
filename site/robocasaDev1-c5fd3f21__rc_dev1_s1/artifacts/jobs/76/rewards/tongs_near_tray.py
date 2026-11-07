import numpy as np
def reward_fn(state):
    objs=state.get("objects",{}) or {}
    def has(ws): return [o for n,o in objs.items() if isinstance(o,dict) and any(w in n.lower() for w in ws)]
    tongs=has(["tong"]) or has(["tongs"])
    tray=has(["tray"]) or has(["platter"]) or has(["plate"])
    if not tongs or not tray: return 0
    moved=False
    for t in tongs:
        try:
            if float(np.linalg.norm(np.array(t.get("pos",[0,0,0]),float)-np.array(t.get("init_pos",[0,0,0]),float)))>0.10: moved=True
        except Exception: pass
    if not moved: return 0
    for t in tongs:
        for tr in tray:
            try:
                td=t.get("gripper_dist"); rd=tr.get("gripper_dist")
                if td is not None and td<0.15: continue
                if rd is not None and rd<0.15: continue
                tp=np.array(t.get("pos",[0,0,0]),float); rp=np.array(tr.get("pos",[0,0,0]),float)
                if float(np.linalg.norm(tp[:2]-rp[:2]))<0.5:
                    return 1.0
            except Exception: pass
    return 0
