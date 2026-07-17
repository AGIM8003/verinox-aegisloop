#!/usr/bin/env python3
import json
from pathlib import Path
from verinox_aegisloop import VerinoxEngine
from verinox_aegisloop.core import classify_closure, independence_ok
OUT = Path(__file__).with_name("verinox_replication_evidence.json")
def main():
    rows=[]
    # independence oracle
    assert independence_ok(["A","B"]) and not independence_ok(["A","A"])
    specs=[
        dict(has_pre=True,has_post=True,has_bond=True,bond_reused=False,independent=True,
             learning_revoked=False,measured=1.0,env_min=0.5,env_max=2.0,cf_min=0.0,cf_max=5.0),
        dict(has_pre=True,has_post=True,has_bond=True,bond_reused=False,independent=True,
             learning_revoked=False,measured=9.0,env_min=0.5,env_max=2.0,cf_min=0.0,cf_max=5.0),
        dict(has_pre=True,has_post=True,has_bond=True,bond_reused=False,independent=False,
             learning_revoked=False,measured=1.0,env_min=0.5,env_max=2.0,cf_min=0.0,cf_max=5.0),
    ]
    for i,s in enumerate(specs):
        oracle=classify_closure(**s)[0]
        e=VerinoxEngine()
        roots=["A","B"] if s["independent"] else ["A","A"]
        e.add_pre("E1", claim_scope="x", source_root=roots[0], value=1.0)
        e.add_pre("E2", claim_scope="x", source_root=roots[1], value=1.0)
        e.set_envelope(predicted_min=s["env_min"], predicted_max=s["env_max"],
                       counterfactual_min=s["cf_min"], counterfactual_max=s["cf_max"])
        e.issue_bond("B"); e.actuate("B"); e.add_post("P", measured=s["measured"])
        eng=e.close("C", claim_scope="x")["verdict"]
        rows.append({"i":i,"engine":eng,"oracle":oracle,"match":eng==oracle})
    ok=all(r["match"] for r in rows)
    OUT.write_text(json.dumps({"rows":rows,"replication_pass":ok}, indent=2), encoding="utf-8")
    print("replication", ok); return 0 if ok else 1
if __name__ == "__main__":
    raise SystemExit(main())
