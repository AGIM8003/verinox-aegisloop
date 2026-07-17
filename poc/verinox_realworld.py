#!/usr/bin/env python3
"""CPS cooling recovery: independent sensors, one-use bond, envelope closure."""
import json
from pathlib import Path
from verinox_aegisloop import (
    VerinoxEngine, CLOSURE_PASS, ENVELOPE_VIOLATION, BOND_REUSED, EVIDENCE_INDEPENDENT_FAIL,
)
OUT = Path(__file__).with_name("verinox_realworld_evidence.json")
def main():
    # Happy path: two sensors, valve actuation, temp within envelope
    e=VerinoxEngine()
    e.add_pre("T_in", claim_scope="coolant", source_root="RTD-1", value=85.0)
    e.add_pre("T_out", claim_scope="coolant", source_root="RTD-2", value=84.5)
    e.set_envelope(predicted_min=60.0, predicted_max=80.0, counterfactual_min=40.0, counterfactual_max=100.0)
    e.issue_bond("VALVE-ONCE"); e.actuate("VALVE-ONCE"); e.add_post("T_post", measured=72.0, horizon="t+5m")
    ok=e.close("RC1", claim_scope="coolant")
    # Same-root false independence
    e2=VerinoxEngine()
    e2.add_pre("T1", claim_scope="coolant", source_root="RTD-1", value=85.0)
    e2.add_pre("T2", claim_scope="coolant", source_root="RTD-1", value=84.0)
    e2.set_envelope(predicted_min=60, predicted_max=80, counterfactual_min=40, counterfactual_max=100)
    e2.issue_bond("B"); e2.actuate("B"); e2.add_post("P", measured=72.0)
    indep=e2.close("RC2", claim_scope="coolant")
    # Envelope miss
    e3=VerinoxEngine()
    e3.add_pre("T1", claim_scope="coolant", source_root="A", value=85.0)
    e3.add_pre("T2", claim_scope="coolant", source_root="B", value=84.0)
    e3.set_envelope(predicted_min=60, predicted_max=70, counterfactual_min=40, counterfactual_max=100)
    e3.issue_bond("B"); e3.actuate("B"); e3.add_post("P", measured=91.0)
    env=e3.close("RC3", claim_scope="coolant")
    # Bond reuse
    e4=VerinoxEngine()
    e4.add_pre("T1", claim_scope="coolant", source_root="A", value=1.0)
    e4.add_pre("T2", claim_scope="coolant", source_root="B", value=1.0)
    e4.set_envelope(predicted_min=0, predicted_max=10, counterfactual_min=0, counterfactual_max=20)
    e4.issue_bond("B"); e4.actuate("B"); e4.actuate("B"); e4.add_post("P", measured=1.0)
    bond=e4.close("RC4", claim_scope="coolant")
    payload={
        "ok":ok["verdict"],"indep":indep["verdict"],"env":env["verdict"],"bond":bond["verdict"],
        "numbers":{"pre_sensors":2,"predicted_max_c":80,"measured_c":72},
        "pass": (ok["verdict"]==CLOSURE_PASS and indep["verdict"]==EVIDENCE_INDEPENDENT_FAIL
                 and env["verdict"]==ENVELOPE_VIOLATION and bond["verdict"]==BOND_REUSED),
    }
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload); return 0 if payload["pass"] else 1
if __name__ == "__main__":
    raise SystemExit(main())
