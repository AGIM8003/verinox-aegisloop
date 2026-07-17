#!/usr/bin/env python3
import json, time
from pathlib import Path
from verinox_aegisloop import VerinoxEngine, CLOSURE_PASS
OUT = Path(__file__).with_name("verinox_benchmark_results.json")
def main():
    e=VerinoxEngine(); t0=time.perf_counter()
    for i in range(200):
        e.add_pre(f"E{i}a", claim_scope="x", source_root=f"R{i%10}", value=1.0)
        e.add_pre(f"E{i}b", claim_scope="x", source_root=f"S{i%10}", value=1.0)
    e.set_envelope(predicted_min=0, predicted_max=10, counterfactual_min=0, counterfactual_max=20)
    e.issue_bond("B"); e.actuate("B"); e.add_post("P", measured=1.0)
    d=e.close("C", claim_scope="x"); sec=time.perf_counter()-t0
    cases=[{"name":"400_pre_close","pass":d["verdict"]==CLOSURE_PASS,"seconds":round(sec,6)}]
    OUT.write_text(json.dumps({"cases":cases,"all_pass":cases[0]["pass"]}, indent=2), encoding="utf-8")
    print(cases); return 0 if cases[0]["pass"] else 1
if __name__ == "__main__":
    raise SystemExit(main())
