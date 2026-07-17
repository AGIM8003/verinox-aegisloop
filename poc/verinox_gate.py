#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path
from verinox_aegisloop import (
    BOND_REUSED, CLOSURE_PASS, ENVELOPE_VIOLATION, EVIDENCE_INDEPENDENT_FAIL,
    LEARNING_REVOKED, PENDING, VerinoxEngine,
)
OUT = Path(__file__).with_name("verinox_gate_results.json")
def t(name, fn):
    try: return {"name": name, "pass": bool(fn()), "error": None}
    except Exception as e: return {"name": name, "pass": False, "error": str(e)}
def primed(e, lo=0.5, hi=2.0):
    e.add_pre("E1", claim_scope="x", source_root="A", value=1.0)
    e.add_pre("E2", claim_scope="x", source_root="B", value=1.0)
    e.set_envelope(predicted_min=lo, predicted_max=hi, counterfactual_min=0.0, counterfactual_max=5.0)
    e.issue_bond("B1")
def main():
    def pass_():
        e=VerinoxEngine(); primed(e); e.actuate("B1"); e.add_post("P", measured=1.0)
        return e.close("C", claim_scope="x")["verdict"]==CLOSURE_PASS
    def envelope():
        e=VerinoxEngine(); primed(e, lo=0.5, hi=1.0); e.actuate("B1"); e.add_post("P", measured=3.0)
        return e.close("C", claim_scope="x")["verdict"]==ENVELOPE_VIOLATION
    def indep():
        e=VerinoxEngine()
        e.add_pre("E1", claim_scope="x", source_root="A", value=1.0)
        e.add_pre("E2", claim_scope="x", source_root="A", value=1.1)  # same root
        e.set_envelope(predicted_min=0.5, predicted_max=2.0, counterfactual_min=0.0, counterfactual_max=5.0)
        e.issue_bond("B1"); e.actuate("B1"); e.add_post("P", measured=1.0)
        return e.close("C", claim_scope="x")["verdict"]==EVIDENCE_INDEPENDENT_FAIL
    def bond():
        e=VerinoxEngine(); primed(e); e.actuate("B1"); e.actuate("B1"); e.add_post("P", measured=1.0)
        return e.close("C", claim_scope="x")["verdict"]==BOND_REUSED
    def pending():
        e=VerinoxEngine(); primed(e); return e.close("C", claim_scope="x")["verdict"]==PENDING
    def revoked():
        e=VerinoxEngine(); primed(e); e.actuate("B1"); e.add_post("P", measured=1.0); e.revoke_learning()
        return e.close("C", claim_scope="x")["verdict"]==LEARNING_REVOKED
    def digest():
        e=VerinoxEngine(); primed(e); e.actuate("B1"); e.add_post("P", measured=1.0)
        d=e.close("C", claim_scope="x"); return len(d["capsule_digest"])==64 and d["verdict"]==CLOSURE_PASS
    def capsule():
        e=VerinoxEngine(); primed(e); e.actuate("B1"); e.add_post("P", measured=1.0)
        c=e.issue_recovery_capsule("C", claim_scope="x"); return c["verdict"]==CLOSURE_PASS
    results=[t(n,f) for n,f in [
        ("closure_pass",pass_),("envelope_violation",envelope),("independence_fail",indep),
        ("bond_reused",bond),("pending",pending),("learning_revoked",revoked),
        ("capsule_digest",digest),("recovery_capsule",capsule)]]
    payload={"gate":"VERINOX Reality Gate","passed":sum(r["pass"] for r in results),
             "total":len(results),"all_pass":all(r["pass"] for r in results),
             "timestamp":datetime.now(timezone.utc).isoformat(),"results":results}
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"Gate {payload['passed']}/{payload['total']}"); return 0 if payload["all_pass"] else 1
if __name__ == "__main__":
    raise SystemExit(main())
