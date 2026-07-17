#!/usr/bin/env python3
import json
from pathlib import Path
from verinox_aegisloop import VerinoxEngine, CLOSURE_PASS
OUT = Path(__file__).with_name("verinox_integration_results.json")
def main():
    e=VerinoxEngine()
    e.add_pre("E1", claim_scope="x", source_root="A", value=1.0)
    e.add_pre("E2", claim_scope="x", source_root="B", value=1.0)
    e.set_envelope(predicted_min=0, predicted_max=2, counterfactual_min=0, counterfactual_max=5)
    e.issue_bond("B"); e.actuate("B"); e.add_post("P", measured=1.0)
    d=e.close("C", claim_scope="x"); c=e.issue_recovery_capsule("C", claim_scope="x")
    ok=d["verdict"]==CLOSURE_PASS and c["capsule_digest"]==d["capsule_digest"]
    OUT.write_text(json.dumps({"pass":ok,"verdict":d["verdict"]}, indent=2), encoding="utf-8")
    print("integration", ok); return 0 if ok else 1
if __name__ == "__main__":
    raise SystemExit(main())
