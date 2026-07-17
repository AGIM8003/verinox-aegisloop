#!/usr/bin/env python3
import json
from pathlib import Path
from verinox_aegisloop import VerinoxEngine, CLOSURE_PASS, ENVELOPE_VIOLATION
OUT = Path(__file__).with_name("verinox_evidence.json")
def main():
    e=VerinoxEngine()
    e.add_pre("E1", claim_scope="temp", source_root="A", value=1.0)
    e.add_pre("E2", claim_scope="temp", source_root="B", value=1.1)
    e.set_envelope(predicted_min=0.5, predicted_max=2.0, counterfactual_min=0.0, counterfactual_max=3.0)
    e.issue_bond("B1"); e.actuate("B1"); e.add_post("P1", measured=1.2)
    ok=e.close("C1", claim_scope="temp")
    e2=VerinoxEngine()
    e2.add_pre("E1", claim_scope="temp", source_root="A", value=1.0)
    e2.add_pre("E2", claim_scope="temp", source_root="B", value=1.1)
    e2.set_envelope(predicted_min=0.5, predicted_max=1.0, counterfactual_min=0.0, counterfactual_max=3.0)
    e2.issue_bond("B1"); e2.actuate("B1"); e2.add_post("P1", measured=1.8)
    bad=e2.close("C2", claim_scope="temp")
    payload={"ok":ok["verdict"],"bad":bad["verdict"],
             "pass": ok["verdict"]==CLOSURE_PASS and bad["verdict"]==ENVELOPE_VIOLATION}
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload); return 0 if payload["pass"] else 1
if __name__ == "__main__":
    raise SystemExit(main())
