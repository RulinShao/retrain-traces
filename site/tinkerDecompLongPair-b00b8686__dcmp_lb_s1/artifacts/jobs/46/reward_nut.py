import numpy as np
def _get(r,k,d=None):
    try:
        if hasattr(r,"get"): return r.get(k,d)
    except Exception: pass
    try: return getattr(r,k,d)
    except Exception: return d
def reward(r):
    rc=_get(r,"sandbox_rc")
    if rc is not None and rc!=0: return 0.0
    fs=_get(r,"final_state")
    if not fs: return 0.0
    o=_get(fs,"objects",{}) or {}
    nut=o.get("square_nut"); peg=o.get("square_peg")
    if not nut or not peg: return 0.0
    np_=nut.get("pos"); pp=peg.get("pos")
    if not (np_ and pp): return 0.0
    nip=nut.get("init_pos") or np_
    moved=abs(np_[0]-nip[0])+abs(np_[1]-nip[1])+abs(np_[2]-nip[2])
    if moved<0.01: return 0.0
    dxy=float(np.hypot(np_[0]-pp[0],np_[1]-pp[1]))
    s=0.12+0.5*max(0.0,1.0-dxy/0.20)
    # nut aligned over peg and descended toward/into it (insertion)
    if dxy<0.07 and np_[2] < pp[2]+0.02:
        s+=0.22
    tc=_get(r,"task_completed")
    if tc: return 1.0
    return float(min(1.0,max(0.0,s)))
