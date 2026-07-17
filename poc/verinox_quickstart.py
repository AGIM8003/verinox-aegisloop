#!/usr/bin/env python3
from verinox_aegisloop import VerinoxEngine
e = VerinoxEngine()
e.add_pre("E1", claim_scope="recovery", source_root="sensorA", value=1.0)
e.add_pre("E2", claim_scope="recovery", source_root="sensorB", value=1.1)
e.set_envelope(predicted_min=0.5, predicted_max=2.0, counterfactual_min=0.0, counterfactual_max=3.0)
e.issue_bond("B1"); e.actuate("B1"); e.add_post("P1", measured=1.2)
d = e.close("CAP1", claim_scope="recovery")
print("Verdict:", d["verdict"])
print("Capsule:", d["capsule_digest"][:24], "...")
