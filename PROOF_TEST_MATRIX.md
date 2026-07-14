# Sixty-Test Invention Proof Matrix

These are required tests, not claimed results. Every run must record release digest, hardware/software configuration, topology, fault injection, raw evidence, expected result, actual result, reviewer, and signed bundle root.

## A. Causal independence tests

| ID | Test | Required outcome |
|---|---|---|
| CIP-01 | Three sensors share one ADC | Collapsed into one causal domain |
| CIP-02 | Analog and digital sources share one power rail | Shared failure is declared |
| CIP-03 | Two services use one upstream observation | Circular evidence detected |
| CIP-04 | Unknown calibration lineage | Independence verdict downgraded |
| CIP-05 | Attestation and success report share one compromised root | Claim blocked |
| CIP-06 | Independent power, clock, firmware, and path | Required cut passes |
| CIP-07 | Evidence removed below required cut | Action denied |
| CIP-08 | Dependency graph altered after signing | Verification fails |
| CIP-09 | Operator is both action approver and sole witness | Independence policy blocks |
| CIP-10 | Same claim evaluated under two action risks | Correct claim-specific thresholds apply |

## B. Counterfactual prediction tests

| ID | Test | Required outcome |
|---|---|---|
| DCO-01 | Action branch missing | Commit denied |
| DCO-02 | Fallback branch missing | Commit denied |
| DCO-03 | Both branches violate safety | Safety stop |
| DCO-04 | Action benefit below threshold | Hold or fallback selected |
| DCO-05 | Branches overlap within uncertainty | Retrospective closure unavailable |
| DCO-06 | Model is outside calibrated fault class | Action reduced or denied |
| DCO-07 | Topology changes after prediction | DCOE and bond invalidated |
| DCO-08 | External event creates desired state | False causal attribution prevented |
| DCO-09 | Actual outcome matches action branch only | Attribution threshold passes |
| DCO-10 | Prediction artifact or parameter digest altered | Verification fails |

## C. Actuation-bond tests

| ID | Test | Required outcome |
|---|---|---|
| RAB-01 | Valid exact bond | Accepted once |
| RAB-02 | Replay consumed bond | Rejected |
| RAB-03 | Command parameter changed | Rejected |
| RAB-04 | Wrong actuator identity | Rejected |
| RAB-05 | Recovery epoch changed | Rejected |
| RAB-06 | Bond expired | Rejected |
| RAB-07 | Rollback unavailable | Commit denied |
| RAB-08 | Local safety interlock open | Rejected locally |
| RAB-09 | Coordinator claims success without actuator receipt | Outcome remains unverified |
| RAB-10 | Split-brain coordinators issue conflicting bonds | Epoch fencing permits at most one |

## D. Multi-horizon closure tests

| ID | Test | Required outcome |
|---|---|---|
| MHC-01 | Command completes without measurements | EXECUTED_UNVERIFIED |
| MHC-02 | Immediate readings pass | At most PROVISIONAL_CLOSED |
| MHC-03 | Stabilization window passes | STABLE_CLOSED if all other gates pass |
| MHC-04 | Delayed thermal excursion occurs | Reopen or revoke |
| MHC-05 | Digital success contradicts current sensor | Rollback or revoke |
| MHC-06 | Mandatory observation missing | INCONCLUSIVE |
| MHC-07 | Measurement source loses required independence | Closure downgraded |
| MHC-08 | All horizons and attribution pass | RETROSPECTIVE_CLOSED |
| MHC-09 | New calibration fault discovered later | Prior receipt reopened by superseding receipt |
| MHC-10 | Earlier receipt deletion attempted | Append-only verification detects tampering |

## E. Learning lineage tests

| ID | Test | Required outcome |
|---|---|---|
| RLL-01 | Provisional event offered as positive training | Rejected |
| RLL-02 | Retrospective-closed event admitted | Complete lineage record required |
| RLL-03 | Dataset digest differs from lineage | Promotion blocked |
| RLL-04 | Source OCR reopened | Descendants identified |
| RLL-05 | Affected model has clean checkpoint | Rollback executed and recorded |
| RLL-06 | Approved unlearning selected | Procedure and residual uncertainty recorded |
| RLL-07 | Descendant policy omitted from trace | Lineage completeness fails |
| RLL-08 | Revoked event remains positively weighted | Release blocked |
| RLL-09 | Retrained model weakens safety regression | Promotion blocked |
| RLL-10 | Correction completes | Signed influence-correction receipt emitted |

## F. Adversarial, safety, and integration tests

| ID | Test | Required outcome |
|---|---|---|
| INT-01 | Forged evidence signature | Rejected |
| INT-02 | Stale CSE | Action denied |
| INT-03 | Corrupt FPGA bitstream | Reconfiguration blocked |
| INT-04 | Switch stuck closed after digital success | Independent readback detects failure |
| INT-05 | Rollback actuator fails | Upstream containment or safety stop |
| INT-06 | Receipt store temporarily unavailable | Safety state preserved; no false closure |
| INT-07 | Coordinator restarts mid-transaction | Deterministic recovery without duplicate actuation |
| INT-08 | Emergency action required | Safety path acts and remains ineligible for positive learning |
| INT-09 | Deterministic replay | Same inputs and versions reproduce decision and digests |
| INT-10 | Full baseline comparison | Integrated kernel demonstrates measurable effect or claim is weakened |

## Release gate

No implementation may claim `evidence-backed prototype` until all mandatory applicable tests pass, failures are published honestly, and signed results are independently reproducible.

