#!/usr/bin/env python3
import json, time, tracemalloc
from pathlib import Path
from verinox_aegisloop import VerinoxEngine, CLOSURE_PASS
OUT = Path(__file__).with_name("verinox_stress_results.json")
def main():
    tracemalloc.start(); e=VerinoxEngine(); n=2000; t0=time.perf_counter()
    for i in range(n):
        e.add_pre(f"A{i}", claim_scope="x", source_root=f"R{i%50}", value=1.0)
        e.add_pre(f"B{i}", claim_scope="x", source_root=f"S{i%50}", value=1.0)
    e.set_envelope(predicted_min=0, predicted_max=10, counterfactual_min=0, counterfactual_max=20)
    e.issue_bond("B"); e.actuate("B"); e.add_post("P", measured=1.0)
    d=e.close("C", claim_scope="x"); sec=time.perf_counter()-t0; _,peak=tracemalloc.get_traced_memory(); tracemalloc.stop()
    payload={"pre_pairs":n,"verdict":d["verdict"],"seconds":round(sec,4),"peak_kib":round(peak/1024,1),
             "pass": d["verdict"]==CLOSURE_PASS and sec<30}
    OUT.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(payload); return 0 if payload["pass"] else 1
if __name__ == "__main__":
    raise SystemExit(main())
