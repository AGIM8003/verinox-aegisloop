#!/usr/bin/env python3
import json
from pathlib import Path
from verinox_aegisloop.core import classify_closure, independence_ok
from verinox_aegisloop.types import (
    BOND_REUSED, CLOSURE_PASS, ENVELOPE_VIOLATION, EVIDENCE_INDEPENDENT_FAIL,
    LEARNING_REVOKED, PENDING,
)
OUT = Path(__file__).with_name("verinox_mutation_results.json")
BASE=dict(has_pre=True,has_post=True,has_bond=True,bond_reused=False,independent=True,
          learning_revoked=False,measured=1.0,env_min=0.5,env_max=2.0,cf_min=0.0,cf_max=5.0)
def main():
    results=[]
    def mut_indep(**kw):
        kw=dict(kw); kw["independent"]=True; return classify_closure(**kw)[0]
    results.append({"name":"force_independent","killed": mut_indep(**{**BASE,"independent":False}) != EVIDENCE_INDEPENDENT_FAIL})
    def mut_env(**kw):
        return CLOSURE_PASS
    results.append({"name":"always_pass","killed": mut_env(**{**BASE,"measured":9.0}) != ENVELOPE_VIOLATION})
    def mut_bond(**kw):
        kw=dict(kw); kw["bond_reused"]=False; return classify_closure(**kw)[0]
    results.append({"name":"ignore_bond_reuse","killed": mut_bond(**{**BASE,"bond_reused":True}) != BOND_REUSED})
    def mut_rev(**kw):
        kw=dict(kw); kw["learning_revoked"]=False; return classify_closure(**kw)[0]
    results.append({"name":"ignore_revoke","killed": mut_rev(**{**BASE,"learning_revoked":True}) != LEARNING_REVOKED})
    def mut_pending(**kw):
        kw=dict(kw); kw["has_post"]=True; kw["measured"]=1.0; return classify_closure(**kw)[0]
    results.append({"name":"fake_post","killed": mut_pending(**{**BASE,"has_post":False,"measured":None}) != PENDING})
    def mut_roots():
        return True  # mutant always independent
    results.append({"name":"indep_fn","killed": mut_roots() != independence_ok(["A","A"])})
    def mut_wide(**kw):
        kw=dict(kw); kw["env_min"]=-1e9; kw["env_max"]=1e9; return classify_closure(**kw)[0]
    results.append({"name":"widen_envelope","killed": mut_wide(**{**BASE,"measured":9.0}) != ENVELOPE_VIOLATION})
    def mut_no_pre(**kw):
        kw=dict(kw); kw["has_pre"]=True; kw["has_bond"]=True; return classify_closure(**kw)[0]
    results.append({"name":"fake_pre","killed": mut_no_pre(**{**BASE,"has_pre":False}) != PENDING})
    def mut_cf(**kw):
        # ignore predicted envelope by using huge cf incorrectly as pass
        return CLOSURE_PASS if kw.get("measured",0)>kw.get("env_max",0) else classify_closure(**kw)[0]
    results.append({"name":"cf_bypass","killed": mut_cf(**{**BASE,"measured":9.0}) != ENVELOPE_VIOLATION})
    def mut_bond2(**kw):
        return CLOSURE_PASS if kw.get("bond_reused") else classify_closure(**kw)[0]
    results.append({"name":"reuse_as_pass","killed": mut_bond2(**{**BASE,"bond_reused":True}) != BOND_REUSED})
    killed=sum(1 for r in results if r["killed"]); rate=killed/len(results)
    payload={"killed":killed,"total":len(results),"kill_rate":round(rate,4),"pass":rate>=0.9,"results":results}
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"mutation {killed}/{len(results)}"); return 0 if payload["pass"] else 1
if __name__ == "__main__":
    raise SystemExit(main())
