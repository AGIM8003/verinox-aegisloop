# VERINOX AEGISLOOP

## Sovereign Evidence-Closed Recovery Fabric

### Complete End-to-End Invention Blueprint

**Technical kernel:** Evidence-Closed Recovery Loop (ECRL)  
**Document file:** VERINOX_AEGISLOOP.md  
**Version:** 2.0 Publication Candidate  
**Blueprint date:** July 14, 2026  
**Language:** English (US)  
**Document identifier:** VERINOX-AEGISLOOP-ECRL-v2.0-2026-07-14  
**Author and concept originator:** Agim Haxhijaha  
**ORCID:** 0009-0002-3234-7765  
**DOI:** 10.5281/zenodo.21364737  
**Edition:** v3.0.0 Public Research Edition (evidence uplift)  
**Status:** Complete publication-candidate technical disclosure and build specification; not prototype-validated, patented, certified, or production-proven  
**Disclosure gate:** Decide whether to seek patent advice or filing before making this publication candidate public  

---

## 0. Critical status statement

This document targets 100% **blueprint and publication-package completeness**: it defines the technical problem, distinguishing mechanism, architecture, data structures, algorithms, physical and software embodiments, implementation path, experiments, failure handling, drawings, claim strategy, attribution, licensing, and publication controls.

It does **not** establish 100% novelty, patentability, freedom to operate, commercial success, safety certification, regulatory conformity, or a working invention. No responsible blueprint can guarantee those outcomes. They require a documented professional prior-art search, prototype evidence, independent testing, and legal review.

The proposed invention is intentionally narrower than the ten source projects. The invention is not “all modules connected together.” Its center is a single causal mechanism:

> A recovery action is authorized, executed, closed, and admitted into future learning only when one cryptographically and functionally bound recovery capsule connects independent pre-action evidence, proof obligations, a predicted outcome envelope, two-phase actuation, measured post-action evidence, and a signed closure verdict.

Version 2.0 narrows that binding further through claim-scoped causal independence, dual counterfactual outcome envelopes, a one-use actuation bond, multi-horizon closure, and revocable learning lineage. That ordered combination is the principal novelty hypothesis.

---

## 1. Invention identity

### 1.1 Project name

**VERINOX AEGISLOOP**

**Full technical designation:** Sovereign Evidence-Closed Recovery Fabric

**Name meaning:** “Aegis” represents protection; “Loop” represents the evidence-closed cycle that binds detection, proof, recovery, measured closure, and learning control.

### 1.2 Core mechanism name

**Evidence-Closed Recovery Loop (ECRL)**

### 1.3 Proposed patent-style title

**Systems and Methods for Evidence-Closed Recovery of Cyber-Physical and Reconfigurable Computing Systems**

### 1.4 Inventor record

Public authorship record:

| Field | Required entry |
|---|---|
| Named author and concept originator | Agim Haxhijaha |
| Contribution summary | Project direction; evidence-closed recovery concept; selection and integration of the final technical mechanism |
| Legal inventor determination | Not determined by this document; professional review required if a patent filing is pursued |
| Applicant or owner | Not asserted in this public technical edition |
| First-filing jurisdiction | No filing represented by this document |
| Blueprint disclosure date | July 14, 2026 |
| Patent status | No patent or patent-pending status claimed |
| Assignment obligations | Must be reviewed privately before any filing or commercial transfer |

### 1.5 Intended defensive use

The fabric is designed for fault containment, resilience, safe reconfiguration, recovery verification, and auditable control. It must not be configured for autonomous targeting, offensive disruption, destructive action against third-party systems, or covert persistence.

---

## 2. Executive invention summary

Modern autonomous and cyber-physical systems can detect faults and initiate recovery, but their evidence, prediction, authorization, execution, verification, and learning processes are usually separate. A system may therefore recover based on circular evidence, declare success without proving that the physical and digital result matches the intended result, or learn from an unsafe or inconclusive action.

ECRL addresses that problem by creating a **Recovery Candidate Capsule**, or RCC, for every proposed recovery. The capsule binds:

1. A canonical pre-action state.
2. Evidence from independently characterized sources.
3. A quantified discordance analysis.
4. The proposed action and its blast radius.
5. Machine-checkable proof obligations.
6. Counterexample and refutation results.
7. A predicted outcome envelope.
8. A two-phase actuation authorization.
9. Measured post-action evidence.
10. A signed Outcome Closure Receipt.
11. A decision stating whether the event may influence future recovery behavior.

The system does not treat “action completed” as “recovery verified.” It closes a recovery only when actual results fall within the bound outcome envelope and mandatory invariants remain satisfied. Inconclusive, degraded, rolled-back, quarantined, or safety-stopped cases are prevented from silently training or modifying the recovery policy.

---

## 3. Technical field

The invention relates to:

- resilient computing;
- cyber-physical control;
- fault-tolerant and reconfigurable systems;
- autonomous recovery;
- hardware attestation;
- runtime assurance;
- deterministic orchestration;
- evidence provenance;
- safety interlocks;
- adaptive control and bounded machine learning;
- tamper-evident audit records; and
- offline or sovereign operation.

The narrow technical focus is the closed-loop coupling of evidence independence, predicted recovery outcomes, two-phase physical or digital actuation, outcome verification, and learning eligibility.

---

## 4. Technical problem

### 4.1 Primary problem

A recovery controller may take an action using evidence that appears diverse but is causally dependent, compromised, stale, or derived from the same sensor, model, clock, software component, or network path. It may then accept an action as successful merely because the command completed, without proving that the physical and digital system entered the intended safe state.

### 4.2 Secondary problems

- A recovery proposal is not cryptographically bound to the exact pre-action state.
- Prediction and actuation use different versions of topology, policy, firmware, or model parameters.
- A proof engine checks abstract rules but not the actual measured outcome.
- A physical switch or FPGA reports success digitally while analog measurements contradict it.
- A rollback path is defined after failure rather than before actuation.
- Learning systems absorb degraded or unsafe recovery events.
- An audit receipt describes the action but cannot reproduce the decision.
- Multiple controllers issue conflicting recoveries.
- An operator cannot distinguish verified recovery from incomplete recovery.
- Offline environments cannot depend on a cloud verifier or public transparency log.

### 4.3 Required technical effect

The invention must produce measurable improvement in at least one of the following:

- lower propagation of a seeded physical or digital fault;
- lower time to verified containment;
- lower false-success classification;
- higher detection of correlated or circular evidence;
- deterministic reproduction of recovery decisions;
- lower rate of unsafe policy updates from bad recovery events;
- improved verification of physical state after a digital control action; or
- reduced ambiguity in post-incident reconstruction.

---

## 5. Baseline technologies and unresolved gap

The system may use known components such as secure boot, remote attestation, digital twins, redundancy, fault isolation, partial reconfiguration, policy engines, formal verification, signed logs, Merkle trees, two-phase commit, runtime monitoring, and reinforcement-learning safety gates.

The invention should not be presented as inventing those components separately.

The proposed distinguishing combination is:

| Baseline capability | Common limitation | ECRL distinction |
|---|---|---|
| Fault detection | Sources may be correlated | Explicit evidence-independence graph and discordance gate |
| Recovery planning | Plan may not be bound to exact state | RCC digest binds state, topology, policy, evidence, action, and prediction |
| Formal verification | Proof may stop before physical execution | Proof obligations are carried through outcome closure |
| Digital twin | Simulation may be advisory only | Prediction envelope becomes an actuation and closure condition |
| Two-phase commit | Usually protects distributed data consistency | ECRL applies prepare/commit/close to cyber-physical recovery |
| Signed logs | Logs prove record integrity, not recovery correctness | OCR records predicted-versus-measured deviation and closure class |
| Safe learning | Data filtering may be external to control | Learning eligibility is an authenticated output of recovery closure |
| Physical isolation | Command acknowledgment may be mistaken for isolation | Independent analog and digital evidence must confirm outcome |

The patent search must test whether this exact functional binding, not merely its individual parts, was publicly disclosed before the filing date.

---

## 6. Novelty hypothesis

### 6.1 Principal novelty hypothesis

The potentially inventive concept is a **causally bound evidence-closed recovery transaction** in which:

1. a proposed recovery is represented by a state-bound capsule;
2. the capsule identifies evidence provenance and independence;
3. a gate evaluates evidence discordance, proof obligations, and attempted refutations;
4. the capsule specifies a predicted multi-domain outcome envelope;
5. an actuator uses a prepare stage before an irreversible or state-changing commit;
6. post-action measurements are compared with the same capsule’s outcome envelope;
7. a closure receipt assigns one of a defined set of recovery outcomes; and
8. the closure outcome controls whether the event may update future recovery behavior;
9. evidence independence is evaluated for each safety claim using shared-failure-domain cut sets, not only source count;
10. the predicted outcome includes both intervention and safe-no-action or fallback counterfactual envelopes;
11. the actuator accepts only a one-use capability cryptographically bound to state, action, deadline, rollback, prediction, and recovery epoch; and
12. delayed contradictory evidence can reopen closure and revoke dependent learning influence.

### 6.2 Strongest narrow embodiment

The strongest initial embodiment is a reconfigurable edge-compute fabric in which a controller isolates or reconfigures a suspect hardware zone only after:

- independent analog rail or link measurements;
- signed digital attestation;
- a topology-aware containment prediction;
- proof that safety and continuity invariants will remain satisfied;
- refutation testing against stuck-switch, spoofed-attestation, stale-topology, and common-clock faults; and
- a prepared rollback or alternate-route graph.

The controller then measures analog and digital results and produces an OCR before treating the new configuration as trusted or reusable.

### 6.3 What is not claimed as the invention

- generic AI governance;
- generic blockchain or Merkle logging;
- a general digital twin;
- a general policy engine;
- ordinary remote attestation;
- ordinary partial FPGA reconfiguration;
- ordinary redundancy or failover;
- ordinary two-phase commit;
- a generic multi-agent referee; or
- a collection of the ten source systems without the ECRL binding.

### 6.4 Version 2.0 novelty-strengthening kernel

The strongest candidate is the indivisible ordered combination below.

| Mechanism | Function | Distinguishing relationship |
|---|---|---|
| Claim-Scoped Causal Independence Proof, CIP | Proves that the evidence supporting each mandatory claim survives policy-defined shared-failure assumptions | Independence is evaluated per claim and action, not as one global sensor count |
| Dual Counterfactual Outcome Envelope, DCOE | Predicts bounded outcomes for the proposed intervention and a safe no-action or fallback alternative | Commit requires a useful and distinguishable expected effect, not merely a safe-looking simulation |
| One-Time Recovery Actuation Bond, RAB | Hardware-verifiable capability bound to RCC, state, action, actuator, epoch, deadline, rollback, and DCOE | The actuator cannot accept a stale or repurposed recovery authorization |
| Multi-Horizon Closure Ladder, MHCL | Moves a recovery through provisional, stabilized, and retrospective closure windows | Command completion or one immediate reading cannot create final success |
| Revocable Learning Lineage, RLL | Records every model, rule, or policy artifact influenced by a closure receipt | Reopened or revoked recovery evidence triggers quarantine, rollback, or unlearning of dependent influence |

The proposed invention is weakened if these mechanisms are separated into optional modules. The preferred claim position requires them to operate as one transaction whose evidence and authority remain bound across time.

---

## 7. Source-project contribution map

The ten source concepts contribute supporting modules. They do not remain ten equal centers of invention.

| Source concept | Reused contribution | Role in the unified project |
|---|---|---|
| CERBERUS — Sovereign Metamaterial Fabric | Analog sanity checks, signed liveness, physical isolation, rerouting, receipt chain | Physical fabric and containment embodiment |
| KHEMERA — Sovereign Physical Foundry | Signed partial reconfiguration, artifact verification, deterministic hardware changes | Reconfiguration actuator |
| AION Continuum Guardian | Predictive orchestration, continuity evaluation, recovery sequencing | Prediction and orchestration |
| Trust Core Reasoning Referee | Conflict arbitration, allow/rewrite/escalate/block logic | Independent recovery referee |
| Sovereign Forge / Aura | Prove-before-build, typed blueprint, deterministic execution package | RCC compiler |
| Sovereign Cognitive Autonomy Engine | Minimal proof kernel, proof-carrying artifacts, deterministic replay | Proof-obligation engine |
| Vanguard Genesis Engine | Candidate generation, counterfactual simulation, counterexample minimization | Refutation engine |
| Prometheus First-Principle Machine | Deterministic experiment runtime and simulation receipts | Outcome-envelope simulator |
| VERINOX AI EcoGuard | Sensor provenance, anomaly workflow, reversible remediation | Environmental and infrastructure embodiment |
| EcoGuard–Agora Fusion Platform | Multi-stakeholder policy, quorum, public or institutional governance | Human and governance gate |

---

## 8. Definitions

| Term | Definition |
|---|---|
| Canonical State Envelope, CSE | A deterministic, signed description of the pre-action state and its evidence |
| Evidence item | A measurement, attestation, observation, model result, operator statement, or neighbor report |
| Evidence Independence Graph, EIG | A graph describing shared dependencies between evidence items |
| Discordance Matrix, DM | Pairwise and group-level measures of disagreement between evidence items |
| Recovery Candidate Capsule, RCC | The complete state-bound proposal for one recovery action |
| Proof obligation | A machine-checkable condition required before preparation or commit |
| Refutation test | An attempt to invalidate the recovery candidate using counterexamples or fault hypotheses |
| Predicted Outcome Envelope, POE | Allowed post-action ranges, transitions, timings, and invariants |
| Prepare token | A short-lived authorization showing that preconditions were satisfied without yet committing the action |
| Actuation commit | The authorized physical or digital state-changing operation |
| Outcome Closure Receipt, OCR | The signed record connecting actual results to the original RCC and assigning closure status |
| Learning eligibility | A signed decision defining whether and how the recovery event may influence future policy or models |
| Evidence-closed | A recovery whose decision, actuation, outcome, and learning status are all bound to one RCC |
| Blast radius | The maximum set of nodes, links, rails, services, users, or regions that an action can affect |
| Safety invariant | A condition that must never be violated |
| Continuity invariant | A minimum service, control, or computation condition required during recovery |

---

## 9. System requirements

### 9.1 Mandatory functional requirements

| ID | Requirement |
|---|---|
| FR-01 | Every recovery proposal must create a unique RCC before actuation |
| FR-02 | Every RCC must reference exactly one CSE digest |
| FR-03 | The CSE must include physical, digital, topology, policy, and time context when available |
| FR-04 | Evidence items must declare provenance and known shared dependencies |
| FR-05 | The system must compute an EIG and DM before authorization |
| FR-06 | Policy must specify the minimum number and types of independent evidence domains |
| FR-07 | Every RCC must include a POE and rollback graph |
| FR-08 | Required proof obligations must pass before preparation |
| FR-09 | Mandatory refutation tests must fail to refute the candidate before preparation |
| FR-10 | Prepare and commit must use separate state transitions |
| FR-11 | A prepare token must expire and be bound to the RCC digest |
| FR-12 | Commit must be rejected if the CSE, topology, policy, or actuator identity changed materially |
| FR-13 | Post-action measurements must be compared with the RCC’s POE |
| FR-14 | Exactly one terminal OCR status must be emitted |
| FR-15 | Learning eligibility must derive from OCR status and policy |
| FR-16 | An inconclusive event must not silently enter the trusted learning set |
| FR-17 | All critical artifacts must be independently verifiable offline |
| FR-18 | Destructive or irreversible actions must require dual authorization and physical interlock where practical |
| FR-19 | The system must support a deterministic replay profile |
| FR-20 | Payload, secrets, and unnecessary personal data must be excluded from receipts |

### 9.2 Nonfunctional requirements

- Fail closed when evidence, policy, time, identity, or topology is ambiguous.
- Remain operable without cloud connectivity in the sovereign profile.
- Use cryptographic agility and version all algorithms.
- Support degraded safe operation when the proof or prediction service is unavailable.
- Separate the safety-critical path from optional AI assistance.
- Provide bounded execution time for each decision stage.
- Maintain monotonic sequence numbers or a trusted local ordering mechanism.
- Preserve operator override, but record and classify override outcomes.
- Keep the trusted computing base as small as practical.

---

## 10. High-level architecture

~~~mermaid
flowchart TD
    A["Independent evidence sources"] --> B["CSE + independence graph"]
    B --> C["RCC compiler"]
    C --> D["Proof, refutation, and policy gate"]
    D --> E["Prepare and actuation controller"]
    E --> F["Outcome measurement and OCR"]
    F --> G["Learning and trust gate"]
    F --> H["Rollback or quarantine"]
~~~

### 10.1 Architectural planes

| Plane | Responsibility | Safety status |
|---|---|---|
| Evidence plane | Acquire, normalize, timestamp, sign, and relate evidence | Critical input |
| State plane | Produce CSE and topology snapshot | Critical |
| Candidate plane | Generate RCCs and rollback alternatives | Controlled |
| Assurance plane | Proof, policy, independence, and refutation gates | Critical |
| Prediction plane | Produce POE and uncertainty bounds | Critical for commit |
| Actuation plane | Prepare, commit, isolate, reroute, reconfigure, or restore | Safety-critical |
| Closure plane | Measure results and issue OCR | Critical |
| Learning plane | Admit, down-weight, quarantine, or reject recovery evidence | Controlled |
| Operator plane | Review, override, inspect, and export evidence | Human control |

### 10.2 Trust boundaries

1. Sensor-to-evidence boundary.
2. Evidence-to-CSE boundary.
3. Candidate generator-to-referee boundary.
4. Assurance-to-actuator boundary.
5. Digital controller-to-physical switch boundary.
6. Closure-to-learning boundary.
7. Operator-to-safety-controller boundary.
8. Local fabric-to-external export boundary.

No component may approve its own evidence as independent merely because it uses a different software process.

---

## 11. Physical reference embodiment

### 11.1 Lab-scale topology

Build an eight-node fabric with:

- four compute nodes;
- two sensor and timing nodes;
- one assurance controller;
- one independent audit workstation;
- redundant network links;
- at least two independently switched power domains;
- one FPGA or SoC with a partially reconfigurable region;
- secure elements or TPM-class roots for node identity;
- voltage, current, temperature, and link-quality measurements;
- solid-state load switches or e-fuses;
- a relay or switch feedback contact independent of the command path;
- a hardware safety stop;
- an isolated management network; and
- a programmable fault-injection harness.

### 11.2 Minimum hardware blocks

| Block | Purpose | Independence consideration |
|---|---|---|
| Main compute MCU/SoC | Workload and node control | Must not be sole health source |
| Safety MCU | Local interlock and bounded actuator control | Separate firmware and watchdog |
| Secure element or TPM | Device identity and signing | Separate key boundary |
| Voltage/current monitor | Rail plausibility | Prefer independent ADC path |
| Temperature sensor | Thermal safety | Avoid sole reliance on SoC telemetry |
| Link monitor | Signal and connectivity quality | Include PHY-level metrics |
| Power isolation switch | Containment | Readback must be independent of command |
| Network crosspoint or managed switch | Rerouting | State must be externally verifiable |
| FPGA reconfigurable region | KHEMERA embodiment | Signed bitstream and readback digest |
| Time source | Ordering and freshness | Detect common-clock dependency |
| Tamper input | Enclosure or connector event | Debounce and authenticate locally |
| WORM-capable storage | Receipt retention | Exportable and offline-verifiable |

### 11.3 Safety controller rules

- It accepts only signed, unexpired prepare tokens.
- It verifies the RCC digest and actuator-specific action digest.
- It confirms local preconditions using its own measurements.
- It rejects commands above the local blast-radius limit.
- It enforces maximum actuation duration and cooldown.
- It can enter SAFE_HOLD without the main controller.
- It records command, readback, and independent measurement hashes.

---

## 12. Software reference architecture

### 12.1 Core services

| Service | Responsibility | Inputs | Outputs |
|---|---|---|---|
| evidence-adapter | Normalize raw evidence | sensor, attestation, operator, model data | EvidenceItem |
| independence-analyzer | Build EIG and source clusters | EvidenceItem set | IndependenceReport |
| state-envelope | Canonicalize trusted current state | evidence, topology, policy | CSE |
| candidate-generator | Generate bounded recovery options | CSE, goals, action catalog | RCC drafts |
| simulator | Predict outcome and uncertainty | RCC draft, state model | POE |
| proof-kernel | Check invariants and proof objects | RCC, CSE, POE | ProofVerdict |
| refutation-engine | Search for counterexamples | RCC, fault library | RefutationReport |
| reasoning-referee | Combine gate results deterministically | all assurance artifacts | GateDecision |
| transaction-coordinator | Prepare and commit action | approved RCC | ActuationRecord |
| outcome-closer | Compare result with POE | measurements, RCC | OCR |
| learning-gate | Control adaptation | OCR, policy | LearningDecision |
| receipt-ledger | Hash-chain and export artifacts | all critical events | sealed bundle |
| operator-console | Human review and override | summaries and evidence | signed decisions |

### 12.2 Trusted computing base

The smallest production profile should place only these components in the trusted base:

- canonical serializer;
- signature and hash verifier;
- policy evaluator;
- proof checker;
- prepare-token verifier;
- safety-controller firmware;
- outcome comparison engine;
- closure classifier; and
- receipt-chain verifier.

AI candidate generation, natural-language explanation, and optimization are outside the trusted base. Their outputs are proposals only.

---

## 13. Canonical State Envelope

### 13.1 Purpose

The CSE freezes the exact state against which the recovery is reasoned. If a material field changes before commit, the RCC must be re-evaluated or regenerated.

### 13.2 Required fields

~~~json
{
  "schema": "verinox.cse/1.0",
  "cse_id": "uuid",
  "created_at_monotonic": 184467,
  "freshness_deadline": 184967,
  "fabric_id": "fabric-01",
  "zone_id": "zone-a",
  "topology_digest": "sha256:...",
  "policy_digest": "sha256:...",
  "firmware_set_digest": "sha256:...",
  "gateware_set_digest": "sha256:...",
  "model_set_digest": "sha256:...",
  "evidence_root": "sha256:...",
  "independence_report_digest": "sha256:...",
  "physical_state": {},
  "digital_state": {},
  "service_state": {},
  "safety_state": {},
  "active_invariants": [],
  "uncertainties": [],
  "signatures": []
}
~~~

### 13.3 Material-change rules

The following invalidate a prepared action unless policy explicitly permits a bounded change:

- topology membership or route change;
- safety-state change;
- actuator identity change;
- policy or invariant version change;
- relevant sensor crossing a precondition threshold;
- attestation freshness expiration;
- firmware or gateware digest change;
- loss of a required independent evidence domain; or
- expiry of the CSE freshness deadline.

---

## 14. Evidence independence and discordance

### 14.1 Evidence Independence Graph

Each evidence item is a node. An edge indicates a shared dependency, including:

- same physical sensor;
- same ADC;
- same power rail;
- same clock;
- same firmware process;
- same model;
- same training data;
- same network path;
- same attestation root;
- same operator;
- same derived data source; or
- same upstream event.

An evidence set is not independent merely because its values are stored in separate databases.

### 14.2 Independence score

For evidence item \(e_i\), define a dependency vector \(q_i\). Pairwise dependency is:

\[
R_{ij} = \frac{\sum_k w_k \mathbf{1}[q_{ik}=q_{jk}\neq \varnothing]}{\sum_k w_k}
\]

where \(w_k\) weights the importance of each dependency class.

Pairwise independence is:

\[
I_{ij}=1-\min(1,R_{ij})
\]

The effective independent-domain count is computed from source clusters after collapsing items whose dependency exceeds a policy threshold.

The score is a control aid, not a statistical proof of independence.

### 14.3 Discordance Matrix

For normalized values \(x_i\) and \(x_j\):

\[
D_{ij}=\alpha d_v(x_i,x_j)+\beta d_t(e_i,e_j)+\gamma d_p(e_i,e_j)+\delta d_m(e_i,e_j)
\]

where:

- \(d_v\) measures value disagreement;
- \(d_t\) measures timing or freshness disagreement;
- \(d_p\) measures provenance conflict; and
- \(d_m\) measures model or modality conflict.

Weights are fixed by policy for deterministic operation.

### 14.4 Gate outcomes

| Condition | Gate result |
|---|---|
| Agreement across required independent domains | CONTINUE |
| High discordance with one low-trust source | DOWN-WEIGHT_AND_RECHECK |
| High discordance across high-trust sources | ESCALATE |
| Evidence is circular or insufficiently independent | BLOCK_INDEPENDENCE |
| Evidence freshness expired | BLOCK_STALE |
| Analog state contradicts digital success claim | BLOCK_OR_ROLLBACK |
| No safe interpretation exists | SAFETY_STOP |

### 14.5 Minimum policy for the first prototype

- At least one analog and one authenticated digital domain for physical isolation.
- At least two effective independent domains for reversible digital recovery.
- At least three effective domains plus human approval for irreversible action.
- No source may simultaneously provide the action command, the only success evidence, and the learning label.

### 14.6 Claim-scoped causal independence proof

For mandatory claim (c), let (G_c=(E_c,D_c)) be a dependency hypergraph where evidence nodes (E_c) support the claim and each hyperedge in (D_c) represents a shared failure domain such as power, clock, sensor, calibration, firmware, model, network, operator, or attestation root.

The policy defines a required surviving-domain cut (k_c). The CIP passes only when compromise or removal of any allowed set of shared domains smaller than (k_c) cannot leave the claim supported solely by one causal root.

The CIP records:

- claim identifier and invariant;
- evidence nodes used;
- direct and inferred dependencies;
- shared-failure assumptions;
- minimum surviving cut;
- unresolved or unknown dependencies;
- freshness window; and
- deterministic verifier result.

Unknown dependencies reduce the maximum independence result. They never default to independent.

---

## 15. Recovery Candidate Capsule

### 15.1 Capsule function

The RCC is the transaction object that prevents decision drift between detection, prediction, proof, actuation, closure, and learning.

### 15.2 Required schema

~~~json
{
  "schema": "verinox.rcc/1.0",
  "rcc_id": "uuid",
  "cse_digest": "sha256:...",
  "goal": {
    "type": "CONTAIN_AND_RESTORE",
    "target_service_floor": 0.70
  },
  "trigger": {
    "fault_class": "RAIL_ANOMALY",
    "evidence_ids": []
  },
  "action_plan": [
    {
      "step": 1,
      "actuator_id": "switch-z3",
      "command": "ISOLATE",
      "parameters": {},
      "reversible": true
    }
  ],
  "preconditions": [],
  "safety_invariants": [],
  "continuity_invariants": [],
  "proof_obligations": [],
  "required_refutations": [],
  "predicted_outcome_envelope": {},
  "blast_radius": {},
  "rollback_graph": {},
  "evidence_independence_requirement": {},
  "approval_requirement": {},
  "expiry": 185067,
  "compiler_digest": "sha256:...",
  "candidate_digest": "sha256:...",
  "signatures": []
}
~~~

### 15.3 Capsule immutability

After the candidate digest is signed, any change to action, order, parameters, evidence, prediction, invariants, topology, policy, expiry, or rollback creates a new RCC. Amendments are linked but never overwrite the old capsule.

### 15.4 Candidate ranking

Candidate ranking is deterministic and lexicographic:

1. reject candidates that violate a safety invariant;
2. reject candidates without a valid rollback path unless the action is a required emergency stop;
3. minimize maximum blast radius;
4. maximize predicted continuity;
5. maximize evidence independence;
6. minimize action irreversibility;
7. minimize energy and wear;
8. minimize predicted recovery time; and
9. use candidate digest as the final stable tie-breaker.

The ranking policy is versioned and included in the RCC.

---

## 16. Predicted Outcome Envelope

### 16.1 Purpose

The POE converts prediction from an advisory report into a measurable condition for commit and closure.

### 16.2 Envelope dimensions

| Domain | Example fields |
|---|---|
| Electrical | voltage, current, impedance, inrush, ripple |
| Thermal | node temperature, rate of change, hotspot limit |
| Timing | clock drift, response deadline, stabilization window |
| Network | link state, route set, loss, latency, partition boundary |
| Compute | node membership, CPU state, memory health, process state |
| Reconfiguration | bitstream digest, region state, interface quiescence |
| Service | minimum availability, throughput, queue depth |
| Security | attestation state, key state, isolation confirmation |
| Safety | interlock state, hazard limit, operator exclusion zone |
| Evidence | required post-action sources and their independence |

### 16.3 Envelope structure

For each observable \(y_k\), the POE defines:

- pre-action value or class;
- expected transition direction;
- allowed lower and upper bounds;
- maximum rate of change;
- earliest and latest observation time;
- stabilization duration;
- measurement source;
- source-independence class;
- uncertainty allowance; and
- mandatory or advisory status.

### 16.4 Deviation vector

\[
\Delta_k = \frac{y_k^{actual}-y_k^{expected}}{\max(\epsilon,s_k)}
\]

where \(s_k\) is the permitted scale or tolerance. The closure engine evaluates the vector using policy-defined mandatory limits and aggregate norms.

### 16.5 Prediction provenance

The POE includes:

- simulator version and digest;
- model parameters;
- calibration dataset digest;
- topology digest;
- deterministic seed;
- uncertainty method;
- known out-of-distribution flags;
- test coverage for the fault class; and
- prediction confidence class.

A low-confidence POE may authorize only a smaller, reversible, or human-approved action.

### 16.6 Dual Counterfactual Outcome Envelope

The v2.0 DCOE contains two separately signed prediction branches:

1. (Y(do(a))): the bounded expected result if the proposed recovery action (a) is committed; and
2. (Y(do(a_0))): the bounded expected result under a safe no-action, hold, or defined fallback (a_0).

For required observable (k), the predicted action effect is:

\[
\tau_k = Y_k(do(a)) - Y_k(do(a_0))
\]

Commit requires:

- the intervention branch to satisfy safety invariants;
- the fallback branch to be explicitly represented;
- the expected benefit or containment effect to exceed a policy threshold where applicable;
- uncertainty intervals and model limitations to be declared;
- the two branches to be sufficiently distinguishable for causal attribution; and
- a rollback branch to remain feasible.

If the actual outcome is equally consistent with action and fallback branches, the recovery cannot reach retrospective closure merely because the desired state happened to occur.

---

## 17. Proof and refutation gate

### 17.1 Proof classes

| Class | Example obligation |
|---|---|
| Static schema | RCC and artifacts conform to versioned schemas |
| Identity | Actuator and evidence sources have valid identities |
| Freshness | Evidence and prepare tokens are within deadlines |
| Topology | Isolation will not disconnect all control paths |
| Safety | Voltage, temperature, motion, or pressure limits remain bounded |
| Continuity | Required minimum service remains reachable |
| Authorization | Actor, action, zone, and risk class are permitted |
| Rollback | At least one safe rollback path exists |
| Resource | Energy, time, memory, and actuator-cycle budgets are acceptable |
| Determinism | Same canonical input produces the same gate result |

### 17.2 Refutation library

The first implementation must attempt at least:

- stuck-open and stuck-closed switch;
- spoofed digital acknowledgment;
- stale attestation;
- compromised neighbor report;
- common-clock failure;
- wrong topology version;
- sensor saturation;
- sensor drift;
- missing measurement;
- network partition;
- rollback actuator unavailable;
- simultaneous second fault;
- reconfiguration artifact mismatch;
- delayed thermal response;
- operator command replay; and
- race between two recovery coordinators.

### 17.3 Gate logic

An RCC may proceed only if:

\[
G = P \land R \land E \land A \land T
\]

where:

- \(P\): all mandatory proofs pass;
- \(R\): required refutations do not produce a disqualifying counterexample;
- \(E\): evidence independence meets policy;
- \(A\): required authorization exists; and
- \(T\): state and evidence are fresh.

The gate emits ALLOW_PREPARE, REVISE, ESCALATE, BLOCK, or SAFETY_STOP.

### 17.4 Proof boundary

Proof is always bounded by declared assumptions. A proof receipt must identify unmodeled hardware behavior, sensor error bounds, timing assumptions, and any parts checked only by testing.

---

## 18. Two-phase cyber-physical actuation

### 18.1 Phase 1: prepare

The transaction coordinator:

1. verifies the RCC signature and digest;
2. verifies the current CSE is still valid;
3. reserves actuators and routes;
4. confirms rollback availability;
5. quiesces affected workloads if required;
6. asks each safety controller for local preflight;
7. freezes conflicting recovery transactions;
8. records a PREPARE receipt; and
9. issues a short-lived prepare token bound to the RCC, actuator set, and time window.

Prepare must not perform the final state-changing action, except reversible quiescence explicitly listed in the RCC.

### 18.2 Phase 2: commit

Commit occurs only if all prepared participants confirm:

- same RCC digest;
- same or policy-equivalent state;
- valid prepare token;
- local safety preconditions;
- no higher-priority safety stop;
- authorized coordinator epoch; and
- actuator availability.

Each step returns command acknowledgment and independent state readback.

### 18.3 Phase 3: observe and close

After commit, the closure engine:

1. opens the POE measurement windows;
2. gathers the specified independent evidence;
3. verifies evidence provenance and freshness;
4. computes deviations;
5. checks safety and continuity invariants;
6. decides whether stabilization is complete;
7. selects one closure status;
8. invokes rollback or quarantine when required;
9. creates the OCR; and
10. sends the OCR to the learning gate.

### 18.4 Concurrency control

- A zone has one active recovery epoch.
- Safety-stop transactions preempt all other transactions.
- Two RCCs that touch the same actuator or dependent zone conflict.
- Nonconflicting RCCs may run concurrently only when their combined blast radius is proven acceptable.
- Coordinator failover requires epoch fencing to prevent split-brain commit.

### 18.5 One-Time Recovery Actuation Bond

The safety controller or hardware root issues one RAB only after prepare checks pass. The bond digest is:

\[
B=H(\text{RCC}\|\text{CSE}\|\text{DCOE}\|\text{actuator}\|\text{command}\|\text{epoch}\|\text{deadline}\|\text{rollback})
\]

The actuator MUST verify the bond locally and MUST reject it when:

- the bond has already been consumed;
- state, topology, firmware, policy, or actuator identity changed;
- the deadline or epoch expired;
- the command differs by any parameter;
- required local interlocks are not satisfied; or
- the rollback or safe-hold capability is unavailable.

Consumption produces an actuator-signed record. A coordinator acknowledgment alone is insufficient.

---

## 19. Outcome Closure Receipt

### 19.1 Terminal statuses

| Status | Meaning | Learning default |
|---|---|---|
| VERIFIED_CLOSED | Mandatory outcomes met and invariants held | Eligible |
| VERIFIED_DEGRADED | Safe but one or more noncritical targets missed | Quarantine pending review |
| ROLLED_BACK | Recovery failed or underperformed and rollback succeeded | Ineligible as positive example |
| QUARANTINED | System contained but trust is unresolved | Ineligible |
| INCONCLUSIVE | Evidence cannot establish outcome | Ineligible |
| SAFETY_STOP | Safety controller stopped or prevented action | Ineligible; mandatory review |

Exactly one status is terminal for an RCC. A later action uses a new linked RCC.

### 19.2 OCR schema

~~~json
{
  "schema": "verinox.ocr/1.0",
  "ocr_id": "uuid",
  "rcc_digest": "sha256:...",
  "cse_digest": "sha256:...",
  "prepare_receipt_digest": "sha256:...",
  "actuation_record_digest": "sha256:...",
  "observed_evidence_root": "sha256:...",
  "predicted_outcome_digest": "sha256:...",
  "deviation_vector": {},
  "invariant_results": [],
  "closure_status": "VERIFIED_CLOSED",
  "rollback_result": null,
  "final_state_digest": "sha256:...",
  "learning_decision_digest": "sha256:...",
  "assumptions": [],
  "unresolved_findings": [],
  "signatures": []
}
~~~

### 19.3 Closure decision

VERIFIED_CLOSED requires:

- all mandatory POE observations present;
- required source independence preserved;
- every safety invariant satisfied;
- every required continuity invariant satisfied;
- every mandatory deviation within tolerance;
- no unresolved actuator contradiction;
- final state attested; and
- no higher-priority fault active.

### 19.4 Multi-Horizon Closure Ladder and reopening

Version 2.0 distinguishes temporal closure states:

| State | Meaning | Learning authority |
|---|---|---|
| EXECUTED_UNVERIFIED | Actuation occurred; outcome not established | None |
| PROVISIONAL_CLOSED | Immediate mandatory measurements match the DCOE | Diagnostic use only |
| STABLE_CLOSED | Required stabilization window passed | Bounded candidate learning |
| RETROSPECTIVE_CLOSED | Delayed-failure window and causal-attribution checks passed | Policy-authorized learning |
| REOPENED | New evidence invalidated an earlier closure assumption | Freeze and trace all dependent influence |
| REVOKED | Recovery is proven unsafe, falsely closed, or materially unsupported | Roll back, unlearn, quarantine, and issue corrective receipt |

Every closed recovery remains addressable by evidence and dependency identifiers. A new sensor-calibration failure, compromised attestation root, delayed thermal excursion, topology discovery, or receipt contradiction can reopen the result. Reopening never erases the prior receipt; it appends a signed superseding receipt.

---

## 20. Proof-gated learning

### 20.1 Purpose

The learning gate prevents an autonomous system from treating action completion, operator acceptance, or a digital acknowledgment as reliable training evidence.

### 20.2 Admission policy

| OCR result | Policy action |
|---|---|
| VERIFIED_CLOSED | Admit to trusted recovery dataset with weight set by evidence quality |
| VERIFIED_DEGRADED | Hold for human review; permit limited negative or boundary learning |
| ROLLED_BACK | Record as failed candidate; do not reward the action |
| QUARANTINED | Store outside trusted model-update corpus |
| INCONCLUSIVE | Store for diagnostics only |
| SAFETY_STOP | Add to mandatory red-team and safety regression sets |

### 20.3 Learning Decision record

The record includes:

- OCR digest;
- eligibility class;
- allowed use;
- weight ceiling;
- affected model or policy;
- review requirement;
- privacy class;
- expiry or retention;
- approving authority; and
- resulting model or policy version, if any.

### 20.4 Update constraints

- No online self-modification of the safety kernel.
- Candidate policies train or optimize in a sandbox.
- Promotion requires replay of the complete safety and fault suite.
- The new policy must not weaken mandatory invariants.
- The previous policy remains available for rollback.
- Every promotion emits a signed release receipt.

### 20.5 Revocable Learning Lineage

Every admitted recovery example creates a Learning Influence Record containing:

- source OCR and closure horizon;
- exact training example, feature, reward, rule, or policy contribution identifier;
- consuming dataset, model, optimizer, policy, and release digests;
- influence weight or bounded contribution estimate;
- promotion approvals and tests;
- rollback checkpoint or unlearning method; and
- descendants that inherit the influence.

When an OCR becomes REOPENED or REVOKED, the lineage service MUST identify affected artifacts and apply policy-selected containment:

1. block further promotion;
2. quarantine affected datasets and models;
3. revert to a clean checkpoint;
4. run an approved unlearning or retraining procedure;
5. repeat safety and regression tests; and
6. publish a signed influence-correction receipt.

No claim is made that all model influence can be perfectly removed. The record states the selected remediation, evidence, residual uncertainty, and affected descendants.

---

## 21. End-to-end operational workflow

### 21.1 Normal recovery

1. Sensors and digital attesters emit evidence.
2. Evidence adapters normalize and sign records.
3. The independence analyzer builds the EIG.
4. The state service creates the CSE.
5. The candidate generator produces bounded RCC drafts.
6. The simulator generates a POE for each draft.
7. The proof kernel checks obligations.
8. The refutation engine tests fault hypotheses.
9. The referee ranks and authorizes one RCC.
10. The coordinator prepares actuators and rollback resources.
11. Safety controllers issue prepare acknowledgments.
12. The coordinator commits.
13. Outcome sources measure the result.
14. The closure engine compares actual values with the POE.
15. An OCR is signed and chained.
16. The learning gate issues a Learning Decision.
17. The operator receives the closure summary and evidence bundle.

### 21.2 State machine

~~~mermaid
stateDiagram-v2
    [*] --> Detected
    Detected --> Captured: Build CSE
    Captured --> Proposed: Compile RCC
    Proposed --> Assured: Proof and refutation pass
    Proposed --> Blocked: Gate fails
    Assured --> Prepared: Preflight and reserve
    Prepared --> Committed: Token valid
    Prepared --> Expired: State or time changes
    Committed --> Observing
    Observing --> Closed: Outcome verified
    Observing --> Rollback: Envelope violated
    Observing --> Quarantine: Evidence inconclusive
    Rollback --> Closed
    Quarantine --> Closed
    Blocked --> [*]
    Expired --> [*]
    Closed --> [*]
~~~

### 21.3 Emergency safety path

Immediate local safety action is permitted without full remote assurance when delay itself would create greater harm. The safety controller then:

1. executes a preauthorized bounded safety action;
2. records the local evidence and policy basis;
3. creates an emergency RCC retrospectively marked EMERGENCY_LOCAL;
4. prevents positive learning by default;
5. requests independent outcome verification; and
6. requires human review.

This exception must be narrow and cannot become a general bypass.

---

## 22. Deterministic referee pseudocode

~~~text
function evaluate_recovery(trigger):
    evidence = acquire_required_evidence(trigger)
    independence = build_independence_graph(evidence)
    if not meets_independence_policy(independence):
        return closureless_block("BLOCK_INDEPENDENCE")

    cse = canonical_state_envelope(evidence, topology, policy)
    candidates = generate_bounded_candidates(cse, trigger)

    assured = []
    for candidate in stable_sort(candidates):
        poe = simulate_outcome(candidate, cse)
        rcc = compile_capsule(candidate, cse, poe)
        proofs = check_proof_obligations(rcc)
        refutations = attempt_required_refutations(rcc)
        gate = deterministic_gate(rcc, proofs, refutations, independence)
        if gate == ALLOW_PREPARE:
            assured.append(rcc)

    if assured is empty:
        return signed_gate_result("BLOCK_NO_SAFE_CANDIDATE")

    selected = deterministic_rank(assured)
    prepared = prepare(selected)
    if not prepared.valid:
        return signed_gate_result("PREPARE_FAILED")

    actuation = commit(selected, prepared.token)
    observations = measure_outcome(selected.predicted_outcome_envelope)
    ocr = close_outcome(selected, actuation, observations)

    if ocr.requires_rollback:
        rollback_result = execute_rollback(selected.rollback_graph)
        ocr = finalize_with_rollback(ocr, rollback_result)

    learning = decide_learning_eligibility(ocr)
    seal(ocr, learning)
    return ocr
~~~

---

## 23. Reconfiguration embodiment

### 23.1 FPGA partial-reconfiguration workflow

1. A region is identified as faulty or inefficient.
2. The CSE records static-region hash, dynamic-region hash, interfaces, clocks, routes, and current workload.
3. An RCC references a signed partial bitstream and its provenance.
4. The POE predicts interface quiescence, reconfiguration duration, power transient, thermal change, and post-load function.
5. Proof obligations verify artifact signature, device compatibility, static-region continuity, rollback image, and maximum disruption.
6. Refutations simulate corrupt image, wrong device, interrupted load, stale topology, and excess inrush.
7. Prepare reserves the rollback image and quiesces interfaces.
8. Commit loads the partial bitstream.
9. Readback digest, independent power telemetry, interface tests, and service probes verify the outcome.
10. The OCR controls whether that bitstream and action are approved for future automatic use.

### 23.2 Physical isolation workflow

1. Analog evidence detects a rail or link anomaly.
2. Signed node liveness claims normal operation.
3. The DM identifies analog/digital discordance.
4. The system lowers trust in the digital claim and proposes bounded isolation.
5. The POE specifies expected current drop, route change, service floor, and stabilization time.
6. A prepare token reserves alternate routes.
7. The safety MCU opens the isolation switch.
8. Independent readback and current measurement verify disconnection.
9. If current does not fall as predicted, the system rolls back, escalates to upstream isolation, or enters SAFETY_STOP.

This analog-versus-digital closure is a preferred claim embodiment.

---

## 24. Additional embodiments

### 24.1 Industrial environmental remediation

The action may change a pump, valve, fan, treatment process, or sensor route. The RCC binds environmental observations, actuator preconditions, predicted physical effects, legal or operational approvals, and post-action measurements. High-impact remediation remains human-approved.

### 24.2 Robotic or autonomous machine

The action may isolate a motor controller, switch to a degraded perception path, reduce speed, or reconfigure compute. The POE includes motion, thermal, power, and localization limits. Local emergency safety remains independent.

### 24.3 Data-center or edge cluster

The action may isolate a node, reroute network paths, rotate keys, restore a firmware image, or move a workload. The POE includes power, route reachability, service latency, and attestation state.

### 24.4 AI-agent action recovery

The action may revoke a tool, restore a policy, roll back a generated configuration, or quarantine an agent. Physical evidence may be replaced by independently controlled operational evidence, but the claim is stronger when at least one independent physical or hardware-attested source is present.

### 24.5 Air-gapped sovereign deployment

All schemas, proofs, signatures, receipts, and verification tools operate locally. Evidence bundles can be exported through an approved one-way or removable-media process.

---

## 25. Interfaces and events

### 25.1 Local API

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /v1/evidence | Submit evidence item |
| POST | /v1/state/capture | Create CSE |
| POST | /v1/recovery/candidates | Generate RCC drafts |
| POST | /v1/recovery/{id}/assure | Run proof and refutation |
| POST | /v1/recovery/{id}/prepare | Request prepare token |
| POST | /v1/recovery/{id}/commit | Commit action |
| POST | /v1/recovery/{id}/observe | Submit outcome evidence |
| POST | /v1/recovery/{id}/close | Issue OCR |
| GET | /v1/receipts/{id} | Retrieve receipt |
| POST | /v1/bundles/verify | Verify offline bundle |
| POST | /v1/policies/promote | Promote reviewed policy |

The safety controller should use a smaller authenticated binary or fieldbus protocol, not the full management API.

### 25.2 Critical events

- EVIDENCE_ACCEPTED
- EVIDENCE_REJECTED
- CSE_CREATED
- INDEPENDENCE_BLOCKED
- RCC_CREATED
- PROOF_PASSED
- PROOF_FAILED
- COUNTEREXAMPLE_FOUND
- ALLOW_PREPARE
- PREPARE_EXPIRED
- COMMIT_STARTED
- ACTUATOR_CONFIRMED
- ACTUATOR_CONTRADICTION
- OUTCOME_WINDOW_OPENED
- OCR_ISSUED
- ROLLBACK_STARTED
- SAFETY_STOPPED
- LEARNING_ADMITTED
- LEARNING_QUARANTINED
- POLICY_PROMOTED

Every event contains schema version, event ID, monotonic sequence, subject digest, previous-event digest, actor, and signature.

---

## 26. Cryptographic and evidence design

### 26.1 Canonicalization

- Use a defined canonical JSON representation for signed JSON artifacts.
- Reject duplicate keys, invalid Unicode normalization, NaN, infinity, and ambiguous numeric forms.
- Use stable ordering for sets and candidate lists.
- Bind schema version and algorithm identifiers into every signature.

### 26.2 Receipt chain

\[
h_n = H(domain \parallel canonical(event_n) \parallel h_{n-1})
\]

Receipt bundles include:

- manifest;
- ordered event records;
- artifact digests;
- signature certificates or local trust anchors;
- Merkle root or equivalent batch root;
- policy and schema versions;
- verification instructions; and
- redacted human-readable summary.

### 26.3 Crypto agility

- Version hash, signature, key-establishment, and certificate profiles.
- Keep safety decisions functional if an external public log is unavailable.
- Allow hybrid or post-quantum migration after device, latency, memory, and interoperability validation.
- Do not place experimental cryptography in a hard real-time isolation path without evidence.

### 26.4 Key separation

Use separate keys for:

- device identity;
- evidence signing;
- actuator authorization;
- operator approval;
- policy release;
- software or gateware release;
- OCR signing; and
- bundle export.

Compromise of an explanation or dashboard key must not authorize actuation.

---

## 27. Security threat model

| Threat | Control | Verification |
|---|---|---|
| Spoofed sensor | Device identity, calibration record, cross-domain evidence | Inject forged sensor |
| Correlated evidence presented as independent | EIG dependency analysis | Shared-clock and shared-model tests |
| Replayed command | Nonce, epoch, expiry, sequence, RCC binding | Replay old prepare token |
| Split-brain coordinator | Epoch fencing and quorum | Partition test |
| Compromised node claims healthy | Analog contradiction gate | Attestation-spoof scenario |
| Malicious RCC generator | Independent proof/refutation/referee | Generate invariant-violating candidate |
| Prediction model poisoning | Signed model provenance and calibration tests | Poisoned-model comparison |
| Stale topology | Digest binding and prepare recheck | Topology mutation during prepare |
| Actuator lies about state | Independent electrical or mechanical readback | Stuck switch test |
| Receipt deletion or modification | Hash chain, WORM retention, offline verifier | Tamper and truncate bundle |
| Unsafe policy update | Signed release, regression gates, rollback | Weaken invariant attempt |
| Operator abuse | Least privilege, dual control, physical interlock | Unauthorized destructive command |
| Data exfiltration through receipts | Schema allowlist and payload exclusion | Secret-seeding test |
| Denial of assurance service | Local safe mode and bounded emergency path | Kill proof service |

### 27.1 Security invariants

- No unsigned RCC reaches prepare.
- No expired prepare token reaches commit.
- No action exceeds its declared blast radius.
- No single software service both authorizes and proves its own outcome.
- No learning update changes the safety kernel automatically.
- No receipt contains raw payload or secret material.

---

## 28. Safety and failure handling

### 28.1 Failure-response matrix

| Failure | Immediate state | Required response |
|---|---|---|
| Missing evidence | HOLD | Gather evidence or escalate |
| Independence below minimum | BLOCK | Obtain independent domain |
| Proof timeout | SAFE_HOLD | Use preapproved bounded fallback |
| Counterexample found | BLOCK | Revise RCC |
| Prepare participant unavailable | ABORT_PREPARE | Release reservations |
| State changes after prepare | EXPIRE | Rebuild CSE and RCC |
| Partial commit | CONTAIN | Execute rollback graph or upstream isolation |
| Analog/digital contradiction | QUARANTINE | Trust independent safety measurement |
| POE violation | ROLLBACK | Re-measure and classify |
| Rollback failure | SAFETY_STOP | Escalate physical containment |
| Receipt write failure | FREEZE_PROMOTION | Preserve local emergency log |
| Learning gate failure | NO_LEARN | Recovery operation may continue safely |

### 28.2 Irreversible actions

Permanent fuse, zeroization, destructive disconnection, or unrecoverable configuration requires:

- explicit irreversible flag;
- proof that reversible alternatives are inadequate;
- dual human approval except immediate life-safety cases;
- physical interlock where practical;
- signed reason;
- verified target identity;
- final warning and cooldown;
- post-action evidence; and
- mandatory incident review.

### 28.3 Human override

An authorized human may:

- block any nonemergency action;
- select a more conservative approved candidate;
- request more evidence;
- initiate safe hold;
- approve a defined high-risk action; or
- command an emergency stop.

The human cannot relabel an unverified outcome as VERIFIED_CLOSED without the required evidence. An override is itself an evidence-bearing action.

---

## 29. Privacy and data governance

- Collect engineering measurements, hashes, event classes, and role identifiers by default.
- Exclude user payloads, message content, video, audio, or personal data unless necessary for a declared embodiment.
- Store raw sensitive evidence separately from the receipt chain.
- Put only hashes, classifications, and minimal derived values in portable receipts.
- Apply role-based and attribute-based access controls.
- Define retention separately for operational evidence, security evidence, learning data, and exported bundles.
- Support redaction without invalidating the original sealed record by using redaction manifests and retained digests.
- Require legal review before processing personal, biometric, location, health, employment, or public-service decision data.

---

## 30. Performance and resource model

### 30.1 Stage budgets

Each deployment defines a signed performance profile:

| Stage | Lab prototype target | Notes |
|---|---:|---|
| Evidence normalization | p95 ≤ 20 ms/item | Excludes slow physical sampling |
| CSE construction | p95 ≤ 100 ms | Up to 100 evidence items |
| Independence and discordance | p95 ≤ 100 ms | Bounded graph |
| Candidate generation | p95 ≤ 250 ms | Maximum 16 candidates |
| Proof and refutation | p95 ≤ 1 s | Bounded MVP rule set |
| Prepare | p95 ≤ 250 ms | Local network |
| Safety-controller actuation | Profile-specific | Hardware limit governs |
| Initial outcome check | ≤ 2 s | Fault-class dependent |
| Stabilized closure | ≤ 60 s | Thermal cases may be longer |
| Offline bundle verification | ≤ 5 s/10,000 events | Reference workstation |

These are targets for the prototype, not measured results.

### 30.2 Bounded-complexity rules

- Evidence items per decision are capped.
- EIG depth and edge types are capped.
- Candidate count is capped.
- Refutation time and state space are bounded.
- A timeout becomes an explicit gate result.
- AI inference may not delay emergency safety action.

---

## 31. Prototype implementation plan

### 31.1 Technology profile

Use mature, replaceable components:

- memory-safe systems language or strongly typed language for the coordinator;
- small C, Rust, or equivalent firmware for the safety MCU;
- deterministic schema validation;
- local relational or append-only storage;
- standard cryptographic library reviewed for the target;
- FPGA vendor-supported partial reconfiguration for the KHEMERA embodiment;
- hardware-in-the-loop test equipment;
- programmable power supply and electronic load;
- oscilloscope or logic analyzer;
- current, voltage, and temperature instrumentation; and
- offline build and verification environment.

No specific vendor is required by the invention.

### 31.2 Repository structure

~~~text
verinox-ecrl/
  contracts/
    cse.schema.json
    evidence.schema.json
    rcc.schema.json
    poe.schema.json
    ocr.schema.json
    learning-decision.schema.json
  core/
    canonical/
    evidence/
    independence/
    state/
    candidate/
    prediction/
    proof/
    refutation/
    referee/
    closure/
    ledger/
  coordinator/
    prepare/
    commit/
    rollback/
  safety-controller/
    firmware/
    protocol/
    test-vectors/
  simulator/
    topology/
    electrical/
    thermal/
    network/
    fault-library/
  adapters/
    fpga/
    power-switch/
    network-switch/
    tpm/
    sensors/
  console/
  tests/
    unit/
    integration/
    determinism/
    security/
    fault-injection/
    hil/
  evidence/
    golden-vectors/
    benchmark-reports/
    signed-bundles/
  docs/
    invention/
    architecture/
    safety/
    operations/
~~~

### 31.3 Build order

1. Define canonical schemas and golden vectors.
2. Implement receipt hash chain and offline verifier.
3. Implement CSE creation and material-change detection.
4. Implement EIG and deterministic DM.
5. Implement RCC compiler with one action class.
6. Implement POE for power isolation.
7. Implement proof kernel and fixed fault-refutation library.
8. Implement software-only prepare/commit simulator.
9. Implement OCR and learning gate.
10. Connect a safety MCU and load switch.
11. Add independent current readback.
12. Run HIL fault scenarios.
13. Add FPGA partial-reconfiguration embodiment.
14. Compare ECRL against the baseline controller.

---

## 32. Twelve-week execution roadmap

| Week | Deliverable | Exit evidence |
|---:|---|---|
| 1 | Invention freeze, inventor log, schemas | Signed design baseline |
| 2 | Canonical serializer and receipt chain | Golden-vector equality |
| 3 | Evidence adapters and CSE | Freshness and mutation tests |
| 4 | EIG and DM | Correlation detection tests |
| 5 | RCC compiler and action catalog | Deterministic capsule hashes |
| 6 | POE simulator | Prediction calibration report |
| 7 | Proof and refutation gate | Seeded counterexample report |
| 8 | Prepare/commit/close software loop | End-to-end simulation receipt |
| 9 | Safety MCU and physical isolation | Bench isolation receipt |
| 10 | Fault injection and rollback | HIL failure matrix |
| 11 | Baseline comparison and repeatability | Benchmark report |
| 12 | Patent evidence pack and design freeze | Filing-ready disclosure package |

Do not wait until week 12 to consult patent counsel if public disclosure is possible.

---

## 33. Validation program

### 33.1 Baseline comparison

Compare ECRL against:

1. threshold monitor plus scripted recovery;
2. digital-attestation-only recovery;
3. prediction-based recovery without evidence closure; and
4. ECRL with full independence, POE, OCR, and learning gate.

### 33.2 Primary metrics

| Metric | Definition | Prototype target |
|---|---|---:|
| False verified closure | Unsafe or incorrect state labeled VERIFIED_CLOSED | 0 in seeded suite |
| Fault propagation | Nodes or services affected beyond origin | ≥30% reduction vs baseline |
| Verified containment time | Trigger to OCR terminal status | ≥20% improvement or justified assurance cost |
| Correlated-evidence detection | Seeded common-dependency cases detected | ≥95% |
| Deterministic replay | Identical inputs produce identical decisions and hashes | 100% |
| Receipt tamper detection | Modified bundles rejected | 100% |
| Unsafe-learning rejection | Nonclosed events blocked from positive learning | 100% |
| Rollback success | Eligible failure cases restored safely | ≥95% |
| Availability floor | Minimum service during reversible recovery | Meet signed scenario target |
| Prediction calibration | Actual result falls within POE | ≥95% for validated fault classes |

Targets must be refined from engineering evidence. A failed target is a design result, not something to hide.

### 33.3 Required fault scenarios

- brownout;
- overcurrent;
- overheating;
- intermittent link;
- corrupt firmware measurement;
- corrupt partial bitstream;
- stale topology;
- common-clock drift;
- forged attestation;
- sensor stuck high;
- sensor stuck low;
- switch stuck closed;
- route reservation failure;
- coordinator restart;
- receipt storage interruption;
- simultaneous node and link fault;
- delayed thermal failure after apparent recovery;
- rollback actuator failure; and
- malicious policy proposal.

### 33.4 Experiment record

Every run records:

- hypothesis;
- baseline;
- hardware and software bill of materials;
- versions and digests;
- topology;
- calibration;
- fault injection;
- expected POE;
- raw measurements;
- deviations;
- OCR;
- unexpected observations;
- video or oscilloscope evidence where useful;
- reviewer; and
- signed bundle root.

### 33.5 Version 2.0 invention-discrimination experiments

The publication package adds a 60-test matrix. The six decisive comparative experiments are:

1. **Shared-root evidence:** show that majority voting passes while claim-scoped CIP blocks a set sharing one hidden dependency.
2. **Spurious desired outcome:** create the desired state through an external event and show that DCOE causal separation prevents false attribution to the recovery action.
3. **Bond substitution:** alter one command parameter after prepare and show that the actuator rejects the RAB.
4. **Delayed failure:** pass immediate checks, then inject a later thermal or electrical excursion and show that MHCL prevents retrospective closure.
5. **Receipt reopening:** invalidate an attestation or calibration root after closure and show that the recovery becomes REOPENED without rewriting history.
6. **Learning influence reversal:** promote a policy using a stable-closed event, revoke that event, and show deterministic identification and containment of every dependent artifact.

---

## 34. Acceptance gates

### 34.1 Gate A: simulation

- Schemas validate.
- Deterministic replay passes.
- Every seeded unsafe action is blocked or safety-stopped.
- OCR never reports VERIFIED_CLOSED when mandatory evidence is missing.

### 34.2 Gate B: bench hardware

- Independent readback detects stuck-switch behavior.
- Safety MCU rejects invalid and expired tokens.
- A digital success claim cannot override contradictory current measurement.
- Rollback or upstream containment works for the defined cases.

### 34.3 Gate C: reconfiguration

- Only signed compatible bitstreams load.
- Static region remains within continuity limits.
- Readback digest and functional probes match.
- Failed reconfiguration produces no positive learning.

### 34.4 Gate D: adversarial evaluation

- Correlated evidence is not counted as independent.
- Split-brain commit is prevented.
- Tampered receipts fail verification.
- Policy weakening fails closed.

### 34.5 Gate E: invention evidence

- A measurable technical effect is demonstrated.
- The exact distinguishing sequence is implemented.
- At least three alternative embodiments are enabled by the disclosure.
- Inventor contributions and dates are documented.
- A professional search has tested the claim elements.

---

## 35. Example test vectors

### TV-01: digital claim contradicts power measurement

- Digital node reports HEALTHY.
- Independent current monitor reports overcurrent.
- Required result: candidate trust shifts toward physical containment; normal digital-only recovery is blocked.

### TV-02: apparent independent sensors share one ADC

- Three sensor values agree.
- EIG shows one ADC and one clock.
- Required result: effective independent-domain count equals one, not three.

### TV-03: state changes after prepare

- Topology changes after token issuance.
- Required result: commit rejected; RCC expires.

### TV-04: action succeeds but stabilization fails

- Switch opens and acknowledgment is valid.
- Temperature continues rising outside POE.
- Required result: not VERIFIED_CLOSED; escalate or upstream isolate.

### TV-05: safe degraded recovery

- Safety limits hold.
- Service floor is lower than target but above emergency minimum.
- Required result: VERIFIED_DEGRADED and learning quarantined.

### TV-06: learning contamination attempt

- A ROLLED_BACK action is labeled successful by an optimization service.
- Required result: learning gate rejects the label because OCR controls eligibility.

---

## 36. Patent-disclosure embodiments

### 36.1 Embodiment A: hardware isolation

Independent analog and authenticated digital evidence trigger an RCC that predicts electrical and network outcomes before a two-stage switch operation. Current readback and route reachability close the recovery.

### 36.2 Embodiment B: dynamic reconfiguration

An RCC binds the static and dynamic hardware states, a signed configuration artifact, power and timing predictions, proof obligations, rollback artifact, partial load, readback digest, and learning eligibility.

### 36.3 Embodiment C: multi-zone containment

A zone coordinator produces an RCC whose blast radius and continuity proof include neighboring zones. Epoch fencing prevents conflicting recovery commits.

### 36.4 Embodiment D: environmental actuator

A remediation RCC binds calibrated environmental evidence, policy approval, predicted physical effect, reversible actuation, post-action measurement, and evidence-qualified learning.

### 36.5 Embodiment E: software and AI recovery

An RCC binds runtime telemetry, attestation, policy state, a rollback package, predicted service outcomes, a configuration commit, post-change probes, and a closure-controlled training decision.

---

## 37. Draft claim strategy

This section is an engineering claim scaffold, not legal advice or a final patent claim set. A patent professional should revise it after a prior-art search.

### 37.1 Independent system claim concept

A recovery-control system comprising:

1. an evidence interface configured to obtain evidence items from multiple source domains;
2. an independence analyzer configured to identify shared dependencies among the evidence items;
3. a state-envelope generator configured to produce a canonical pre-action state;
4. a capsule generator configured to produce an RCC bound to the canonical state, a recovery action, proof obligations, a rollback definition, and a predicted outcome envelope;
5. an assurance gate configured to evaluate the evidence independence, the proof obligations, and one or more refutation tests;
6. an actuation coordinator configured to issue a state-bound prepare authorization and then commit the recovery action;
7. an outcome engine configured to compare post-action evidence with the predicted outcome envelope and issue a terminal OCR; and
8. a learning gate configured to permit or prevent use of the recovery event for modification of future recovery behavior according to the OCR.

The strongest “wherein” clause should state that the same RCC is functionally or cryptographically bound across pre-action evidence, prediction, actuation, measured outcome, closure status, and learning eligibility.

### 37.2 Independent method claim concept

A computer-implemented and cyber-physical recovery method comprising:

1. capturing a canonical state from multiple evidence domains;
2. determining dependencies among those domains;
3. generating a state-bound recovery capsule;
4. generating a predicted post-action envelope;
5. verifying proof obligations and attempting specified refutations;
6. issuing a capsule-bound prepare authorization;
7. committing a physical or digital recovery action;
8. measuring the result using evidence identified by the capsule;
9. assigning a terminal closure status from predicted-versus-measured deviation; and
10. controlling learning eligibility using that closure status.

### 37.3 Independent storage-medium claim concept

A non-transitory computer-readable medium storing instructions that cause one or more processors and an actuator interface to perform the method above.

### 37.4 Dependent claim candidates

1. The evidence domains include an analog measurement and signed digital attestation.
2. The analyzer collapses evidence sharing a sensor, clock, power rail, model, network path, or attestation root.
3. The predicted envelope includes electrical and network values.
4. The action isolates a power or network zone.
5. The action partially reconfigures a programmable device.
6. The prepare authorization expires after a material state change.
7. The safety controller independently rechecks a local precondition.
8. The actuator state is verified by a readback path independent of the command path.
9. The closure status is one of the six statuses defined in this blueprint.
10. Only VERIFIED_CLOSED events are automatically eligible as positive learning examples.
11. VERIFIED_DEGRADED events require human approval before learning.
12. The recovery capsule includes a rollback graph.
13. A counterexample causes the action to be blocked or revised.
14. The system uses epoch fencing to prevent split-brain commit.
15. An emergency safety action creates a retrospective emergency capsule and remains ineligible for positive learning by default.
16. The receipt bundle is verifiable without network access.
17. The system detects circular evidence that derives from a common upstream observation.
18. A cryptographic digest binds topology, policy, firmware, gateware, prediction, and action.
19. An outcome contradiction triggers rollback, quarantine, or upstream isolation.
20. The system assigns a learning weight ceiling from evidence quality.

### 37.5 Claim-drafting cautions

- Do not lead with “AI,” “blockchain,” “digital twin,” or “zero trust.”
- Do not claim all source-project features in one independent claim.
- Preserve the physical or computing technical effect.
- Include enough hardware interaction to avoid an abstract information-processing characterization.
- Keep alternative independent claims for hardware isolation and partial reconfiguration.
- Add narrower claims after the prior-art search identifies crowded elements.

### 37.6 Version 2.0 strongest claim nucleus

The preferred independent claim should require, in one causally linked recovery transaction:

1. claim-specific evidence dependency analysis producing a causal independence proof;
2. an immutable state-bound recovery capsule;
3. intervention and fallback counterfactual outcome envelopes;
4. a one-use actuator-verifiable bond bound to the capsule and recovery epoch;
5. post-action evidence evaluated across multiple closure horizons;
6. causal-attribution and contradiction checks before retrospective closure; and
7. a learning-influence record that is automatically traced and contained when closure is reopened or revoked.

The physical embodiment should require at least one readback path independent of the command path. Separate claims may cover FPGA reconfiguration, power/network isolation, robotic recovery, and software-agent configuration recovery, but the hardware-isolation embodiment is the clearest first claim anchor.

---

## 38. Drawing set for a patent professional

| Figure | Drawing |
|---:|---|
| 1 | Overall ECRL architecture |
| 2 | Evidence Independence Graph and Discordance Matrix |
| 3 | Canonical State Envelope construction |
| 4 | Recovery Candidate Capsule data binding |
| 5 | Proof, refutation, and policy gate |
| 6 | Two-phase cyber-physical prepare and commit |
| 7 | Predicted Outcome Envelope and measurement windows |
| 8 | Outcome Closure Receipt generation |
| 9 | Learning eligibility state machine |
| 10 | Hardware node with main controller, safety MCU, sensors, secure element, and isolation switch |
| 11 | FPGA partial-reconfiguration embodiment |
| 12 | Multi-zone recovery and epoch fencing |
| 13 | Analog/digital contradiction scenario |
| 14 | Rollback and upstream containment graph |
| 15 | Offline receipt bundle verification |

Each drawing should use stable reference numerals and be supported by a matching description.

---

## 39. Prior-art search plan

### 39.1 Search concepts

Search patents and technical literature for combinations of:

- evidence-bound autonomous recovery;
- proof-carrying recovery action;
- predicted outcome envelope plus actuation;
- cyber-physical two-phase recovery commit;
- attestation plus analog fault isolation;
- independent actuator readback plus signed recovery receipt;
- recovery closure receipt;
- fault recovery learning eligibility;
- digital twin verified recovery;
- partial reconfiguration proof and rollback;
- correlated evidence detection in fault-tolerant control; and
- state-bound safety authorization.

### 39.2 Search classes and neighboring fields

Have a professional search:

- fault-tolerant computing;
- distributed commit;
- industrial control and safety PLCs;
- runtime assurance;
- remote attestation;
- self-healing networks;
- FPGA partial reconfiguration;
- digital twins;
- autonomous vehicle fallback;
- reinforcement-learning safety;
- event sourcing and signed audit logs; and
- cyber-physical anomaly detection.

### 39.3 Claim chart

For each reference, chart whether it teaches:

1. state-bound capsule;
2. evidence dependency analysis;
3. proof obligations;
4. refutation;
5. POE;
6. prepare authorization;
7. cyber-physical commit;
8. independent post-action measurement;
9. terminal OCR; and
10. OCR-controlled learning.

The invention is weakened if one reference teaches all elements or if a small, obvious combination of references supplies them without an unexpected technical effect.

---

## 40. Experimental novelty-strengthening plan

The best way to improve the invention is to prove an effect created by the binding, not merely by better components.

### Experiment 1: correlated evidence

Compare a three-sensor majority vote with ECRL when all three values share one ADC or clock. Demonstrate that ECRL avoids false confidence.

### Experiment 2: false digital success

Make the actuator return a successful acknowledgment while the physical switch remains closed. Demonstrate that ECRL prevents false closure.

### Experiment 3: state drift between prediction and action

Change topology after prediction. Demonstrate that the prepare token expires and prevents a stale action.

### Experiment 4: delayed physical outcome

Create a thermal or electrical response that initially appears safe and later leaves the POE. Demonstrate stabilization-window closure and rollback.

### Experiment 5: learning contamination

Feed failed and inconclusive actions into a conventional optimizer and ECRL. Demonstrate that ECRL prevents positive reinforcement from unverified events.

### Experiment 6: integrated technical effect

Measure fault propagation, false closure, recovery time, and service continuity across the four baseline controller configurations in Section 33.

---

## 41. Productization path

### Phase 1: evaluation kit

- Eight-node lab fabric.
- One physical isolation action.
- One partial-reconfiguration action.
- Local console and verifier.
- Fault-injection harness.
- Signed evidence bundles.

### Phase 2: rugged edge zone

- 16–64 nodes.
- Multiple power and network zones.
- Hardware safety certification planning.
- Extended environmental tests.
- Supply-chain evidence.

### Phase 3: multi-zone sovereign fabric

- Independent zone coordinators.
- Epoch fencing and zone quorum.
- Air-gapped update workflow.
- Formalized cross-zone invariants.

### Phase 4: licensed recovery kernel

- Hardware OEM integration.
- Industrial, environmental, robotics, and data-center profiles.
- Patent and interoperability licensing strategy.

---

## 42. Operational roles

| Role | Authority |
|---|---|
| Field operator | Observe, safe hold, approved reversible actions |
| Safety officer | Emergency stop, high-risk approval |
| Security engineer | Trust anchors, attestation, incident quarantine |
| Hardware engineer | Calibration, fault analysis, actuator maintenance |
| Policy owner | Approve policies and invariant versions |
| Model owner | Propose prediction or learning updates |
| Auditor | Verify receipts and evidence bundles |
| Release manager | Promote signed software, firmware, and gateware |
| Patent reviewer | Maintain invention record and disclosure history |

No one role should unilaterally change policy, authorize an irreversible action, and approve the resulting closure.

---

## 43. Decision locks

The following decisions require named human approval:

1. Exact first product embodiment.
2. Safety and continuity invariant owners.
3. Minimum independent evidence domains by action class.
4. Allowed irreversible actions.
5. Hardware platform and safety-controller boundary.
6. Cryptographic profile.
7. Whether any learning occurs online.
8. Data retention and personal-data scope.
9. Patent filing country and timing.
10. Any public demo, publication, sale, investor disclosure, or open-source release before filing.

---

## 44. Risks and unresolved questions

| Risk | Impact | Mitigation |
|---|---|---|
| Prior art contains the full sequence | Patent claims may be narrow | Professional search and claim chart |
| Too many modules obscure invention | Weak unity and enablement | Keep ECRL as one kernel |
| Prediction envelope is poorly calibrated | False block or false closure | Fault-class calibration and conservative bounds |
| Evidence independence is misclassified | False confidence | Explicit dependency schema and red-team |
| Hardware readback is not truly independent | False physical verification | Separate sensor, path, power, and firmware |
| Proof scope is overstated | Invalid assurance claim | Declare assumptions and test gaps |
| Recovery latency is too high | Poor safety or availability | Bounded fast path and local safety controller |
| Learning adds regulatory risk | Deployment friction | Ship MVP with learning disabled or offline |
| Receipts leak sensitive data | Privacy/security exposure | Schema allowlist and redaction manifests |
| Irreversible action is abused | Safety harm | Dual control and physical interlock |

---

## 45. Definition of done

The invention moves from blueprint to evidence-backed prototype only when:

- the ECRL path is implemented end to end;
- at least one real physical actuator is controlled;
- at least one independent physical readback exists;
- correlated evidence is detected in a seeded case;
- a state change invalidates a prepare token;
- an outcome outside the POE cannot be labeled VERIFIED_CLOSED;
- OCR status controls learning eligibility;
- deterministic replay reproduces the decision;
- tampered receipts fail verification;
- rollback and safety-stop paths are demonstrated;
- baseline comparison results are signed; and
- a patent professional has reviewed the prior art and claim scope.

---

## 46. Blueprint completeness scorecard

This table measures document completeness, not patentability or prototype maturity.

| Blueprint category | Weight | Completed | Location |
|---|---:|---:|---|
| Technical problem | 8% | 8% | Sections 3–4 |
| Baseline and prior-art plan | 12% | 12% | Sections 5 and 39 |
| Distinguishing kernel | 15% | 15% | Sections 6 and 15–20 |
| Formal mechanism | 15% | 15% | Sections 14–22 |
| States and data contracts | 10% | 10% | Sections 13, 15, 19, 25 |
| Hardware and software architecture | 10% | 10% | Sections 10–12 and 31 |
| Enabled embodiments | 10% | 10% | Sections 23–24 and 36 |
| Benchmark and validation | 8% | 8% | Sections 33–35 and 40 |
| Failure and safety | 5% | 5% | Sections 27–29 |
| Claim scaffold | 5% | 5% | Section 37 |
| Drawing plan | 2% | 2% | Section 38 |
| **Total blueprint completeness** | **100%** | **100%** | Complete |

### 46.1 Separate maturity score

At the date of this blueprint:

| Dimension | Current evidence-based status |
|---|---:|
| Blueprint and publication-package completeness | 100% |
| Candidate invention distinctiveness estimate | 84% |
| Technical enablement on paper | 95% |
| Publication readiness after IP decision | 98% |
| Patent-document readiness | 82% |
| Prototype implementation | 0% |
| Experimental validation | 0% |
| Targeted technical prior-art positioning | Completed; not a professional patent search |
| Patentability certainty | Cannot be guaranteed |
| Certification readiness | 0% |
| Commercial production readiness | 0% |

After successful implementation, comparative experiments, and professional prior-art review, a realistic target is approximately 88–92% invention-strength confidence. A responsible process cannot promise 100% novelty or patentability.

---

## 47. Immediate next actions

1. Decide whether to seek patent advice or file before public disclosure.
2. Freeze this version and retain its SHA-256 manifest.
3. Select the hardware-isolation embodiment as the first prototype.
4. Create the CIP, RCC, DCOE, RAB, OCR, and Learning Influence schemas.
5. Build the software-only deterministic transaction and offline verifier.
6. Add one safety MCU, one load switch, and an independently powered current or link sensor.
7. Run the 60-test suite and six invention-discrimination experiments.
8. Produce signed comparison evidence against four baselines.
9. Give the disclosure, drawings, search matrix, test results, and conception history to a qualified patent professional.
10. Publish the candidate blueprint only after explicit author authorization.

---

## 48. Final invention statement

The project’s defendable center is not autonomous recovery alone. It is a recovery transaction whose legitimacy remains closed over the full causal chain:

\[
\text{claim-scoped causal independence}
\rightarrow
\text{state-bound capsule}
\rightarrow
\text{dual counterfactual prediction}
\rightarrow
\text{proof and refutation}
\rightarrow
\text{one-use bonded actuation}
\rightarrow
\text{multi-horizon measured closure}
\rightarrow
\text{revocable learning lineage}
\]

If the prototype demonstrates that this closed binding prevents false recovery, spurious causal attribution, fault propagation, delayed false closure, and learning contamination more effectively than the baselines, the concept can become a strong real-invention candidate.

---

## 49. Version 2.0 Formal Invention Kernel

### 49.1 Transaction tuple

The causally bound evidence-closed recovery transaction is:

\[
T=\langle S,C,R,P,F,B,A,O,L,Q\rangle
\]

where:

- (S) is the Canonical State Envelope;
- (C) is the Claim-Scoped Causal Independence Proof set;
- (R) is the Recovery Candidate Capsule;
- (P) is the Dual Counterfactual Outcome Envelope;
- (F) is the proof and refutation result;
- (B) is the One-Time Recovery Actuation Bond;
- (A) is the actuator-signed action record;
- (O) is the multi-horizon observed outcome set;
- (L) is the terminal or superseding closure receipt; and
- (Q) is the Revocable Learning Lineage record.

Every element contains the transaction identifier, recovery epoch, prior-element digests, schema version, producer identity, validity interval, and signature. A digest mismatch breaks the transaction.

### 49.2 Core invariants

**Causal independence invariant**

\[
\forall c\in Claims_{mandatory}: cut(G_c)\ge k_c
\]

**State-binding invariant**

\[
H(S_t)=R.state\_digest=B.state\_digest=A.state\_digest
\]

**Bond singularity invariant**

\[
consume(B)\le1
\]

**Counterfactual closure invariant**

\[
close_{retro}\Rightarrow O\in P_{action}\land sep(O,P_{action},P_{fallback})\ge\theta
\]

**Temporal closure invariant**

\[
RETROSPECTIVE\_CLOSED\Rightarrow windows_{immediate,stable,delayed}=PASS
\]

**Learning lineage invariant**

\[
learn(T)\Rightarrow status(L)\in Allowed\land trace(Q,T)=complete
\]

**Revocation propagation invariant**

\[
revoke(L)\Rightarrow \forall d\in descendants(Q): contain(d)
\]

### 49.3 Required v2.0 objects

~~~json
{
  "causal_independence_proof": {
    "claim_id": "safety.isolated",
    "dependency_hypergraph_digest": "sha256:...",
    "minimum_surviving_cut": 2,
    "required_cut": 2,
    "unknown_dependencies": [],
    "verdict": "PASS"
  },
  "dual_counterfactual_outcome": {
    "action_branch_digest": "sha256:...",
    "fallback_branch_digest": "sha256:...",
    "effect_thresholds": {},
    "separation_threshold": 0.8,
    "uncertainty_profile_digest": "sha256:..."
  },
  "recovery_actuation_bond": {
    "rcc_digest": "sha256:...",
    "state_digest": "sha256:...",
    "actuator_id": "did:example:actuator",
    "command_digest": "sha256:...",
    "recovery_epoch": 41,
    "expires_at": "2026-07-14T00:00:10Z",
    "rollback_digest": "sha256:...",
    "consumption_limit": 1
  },
  "closure_ladder": {
    "immediate": "PASS",
    "stable": "PENDING",
    "retrospective": "PENDING",
    "reopen_triggers": []
  },
  "learning_influence": {
    "source_ocr_digest": "sha256:...",
    "consuming_artifacts": [],
    "rollback_checkpoint": "sha256:...",
    "containment_state": "NOT_REQUIRED"
  }
}
~~~

`did:example:actuator` is a schema illustration, not a deployed identifier.

### 49.4 Deterministic verifier

~~~text
verify_v2(transaction):
    verify_schemas_signatures_epochs_and_digest_chain(transaction)
    require_every_mandatory_claim_has_passing_causal_independence_proof()
    require_state_and_topology_match_recovery_capsule()
    require_action_and_fallback_prediction_branches()
    require_proof_obligations_pass_and_refutations_do_not_succeed()
    require_actuation_bond_is_valid_unconsumed_and_locally_accepted()
    compare_immediate_stable_and_delayed_observations_with_action_envelope()
    compute_action_fallback_separation_and_record_causal_limitations()

    if prohibited_outcome_or_contradiction_observed:
        return REVOKED
    if mandatory_evidence_missing_or_causal_attribution_insufficient:
        return INCONCLUSIVE
    if delayed_window_open:
        return PROVISIONAL_CLOSED_OR_STABLE_CLOSED
    return RETROSPECTIVE_CLOSED

on_new_evidence(closure_receipt, evidence):
    if evidence_invalidates_dependency_state_prediction_or_outcome:
        append_REOPENED_or_REVOKED_receipt()
        trace_and_contain_all_learning_descendants()
~~~

### 49.5 Non-bypass rules

- The coordinator cannot declare its own evidence independent.
- The actuator cannot change a bond parameter.
- An operator cannot promote a provisional result to retrospective closure.
- A digital acknowledgment cannot override contradictory physical readback.
- Missing causal-separation evidence produces INCONCLUSIVE, not VERIFIED.
- Learning cannot discard the source receipt or lineage record.
- Reopening cannot delete or rewrite the earlier signed receipt.

---

## 50. Research and Prior-Art Differentiation

### 50.1 Established neighboring directions

Research already covers runtime assurance and Simplex controller switching, independently checked pre-action safety certificates, reachability-based safety shields, causal digital twins, secure attestation, resilient recovery, tamper-evident provenance, and safe-learning constraints. None of those elements should be claimed individually.

### 50.2 Candidate differentiation after research

The v2.0 position is narrower than generic autonomous recovery. The candidate contribution is the transaction-level dependency that requires all of the following:

1. evidence independence proven separately for each mandatory claim under shared failure domains;
2. action and fallback counterfactual outcome branches bound before actuation;
3. a one-use capability checked by the physical or reconfiguration actuator;
4. closure across immediate, stabilization, and delayed horizons;
5. reopening when later evidence invalidates closure; and
6. deterministic tracing and containment of every learning artifact influenced by the invalidated recovery.

A professional patent search must still test whether one reference or an obvious combination teaches this entire sequence and technical effect.

### 50.3 Technical-effect hypothesis

Compared with attestation-only, prediction-only, majority-vote, and ordinary runtime-assurance baselines, the integrated kernel is expected to reduce:

- false confidence from correlated evidence;
- action authorization after state drift;
- false closure caused by exogenous events;
- false success caused by command acknowledgments;
- delayed failures mislabeled as successful recoveries; and
- propagation of invalid recovery experience into future autonomous behavior.

These are hypotheses until demonstrated by signed comparative experiments.

---

## 51. Publication, Attribution, and License

### 51.1 Recommended public description

> VERINOX AEGISLOOP is Agim Haxhijaha's proposed Sovereign Evidence-Closed Recovery Fabric. Its candidate contribution is a causally bound recovery transaction combining claim-scoped evidence independence, dual counterfactual outcomes, one-use bonded actuation, multi-horizon measured closure, and revocable learning lineage. It is published as a technical blueprint, not as a patent, implemented product, certification, or independent validation.

### 51.2 Citation

Haxhijaha, A. (2026). *VERINOX AEGISLOOP: Sovereign Evidence-Closed Recovery Fabric* (Version 2.0).

### 51.3 Documentation license

The publication package applies Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (`CC BY-NC-ND 4.0`) to the documentation. No patent, trademark, commercial implementation, certification, or warranty right is granted.

### 51.4 AI-assistance disclosure

Artificial intelligence assisted with research organization, comparison, drafting, terminology, formalization, and publication packaging. Agim Haxhijaha supplied the project direction, selected and accepted the final invention architecture, and remains responsible for publication and claims. AI assistance is not inventorship adjudication or independent validation.

---

## 52. Primary Research References

1. Jackson, D., et al. *Certified Control: An Architecture for Verifiable Safety of Autonomous Vehicles*. 2021. https://arxiv.org/abs/2104.06178
2. Mehmood, U., et al. *The Black-Box Simplex Architecture for Runtime Assurance of Autonomous CPS*. 2021. https://arxiv.org/abs/2102.12981
3. Homaei, M., et al. *Causal Digital Twins for Cyber-Physical Security*. 2025. https://arxiv.org/abs/2510.09616
4. Kochdumper, N., et al. *Provably Safe Reinforcement Learning via Action Projection Using Reachability Analysis and Polynomial Zonotopes*. 2022. https://arxiv.org/abs/2210.10691
5. Dong, Y., et al. *Reachability Verification Based Reliability Assessment for Deep Reinforcement Learning Controlled Robotics and Autonomous Systems*. 2022. https://arxiv.org/abs/2210.14991
6. IETF. *RFC 9334: Remote ATtestation procedureS Architecture*. 2023. https://www.rfc-editor.org/rfc/rfc9334.html
7. IETF. *RFC 9711: The Entity Attestation Token*. 2025. https://www.rfc-editor.org/rfc/rfc9711.html
8. IETF. *RFC 9943: An Architecture for Trustworthy and Transparent Digital Supply Chains*. 2026. https://www.rfc-editor.org/rfc/rfc9943.html
9. IETF. *RFC 9942: COSE Receipts*. 2026. https://www.rfc-editor.org/rfc/rfc9942.html
10. W3C. *PROV-O: The PROV Ontology*. https://www.w3.org/TR/prov-o/
11. NIST. *SP 800-160 Vol. 2 Rev. 1: Developing Cyber-Resilient Systems*. 2021. https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final
12. NIST. *SP 800-82 Rev. 3: Guide to Operational Technology Security*. 2023. https://csrc.nist.gov/pubs/sp/800/82/r3/final

---

## 53. Publication Completion Record

- **Document:** `VERINOX_AEGISLOOP.md`
- **Identifier:** VERINOX-AEGISLOOP-ECRL-v2.0-2026-07-14
- **Author and concept originator:** Agim Haxhijaha
- **Version:** 2.0 Publication Candidate
- **Blueprint and package completeness:** 100%
- **Candidate invention distinctiveness estimate:** 84%
- **Publication readiness after IP decision:** 98%
- **Prototype and experimental validation:** 0%; no result claimed
- **Patent status:** no patent or patent-pending claim
- **Research cutoff:** July 14, 2026
- **Public release gate:** intellectual-property decision and explicit author authorization

---

**END OF BLUEPRINT**


---

# v3.0.0 EVIDENCE UPLIFT (2026-07-17)

**ORCID:** 0009-0002-3234-7765 · **DOI:** 10.5281/zenodo.21364737 · **GitHub:** https://github.com/AGIM8003/verinox-aegisloop  
**SSOT:** `VERINOX_AEGISLOOP_v3.0.0_PUBLIC_RESEARCH_EDITION.md`  
**Library:** `from verinox_aegisloop import VerinoxEngine`

## 1. Honest Status Boundary

VERINOX AEGISLOOP is **not** a certified functional-safety product (IEC 61508/ISO 26262), **not** a granted patent, **not** a production CPS controller, **not** peer reviewed, and **not** independently replicated. It is a **Evidence-Closed Recovery Loop (ECRL)** blueprint: claim-scoped independent pre-evidence, dual counterfactual outcome envelopes, one-use actuation bonds, multi-horizon measured closure, and revocable learning lineage bound in a recovery capsule.

## 2. Novelty Declaration

### Layer 1 — Component Novelty

| Component | Novel? | Evidence |
|-----------|--------|----------|
| Independent pre-evidence | PARTIAL | Sensor redundancy exists; claim-scoped independence root checks are the binding claim |
| Dual counterfactual envelopes | PARTIAL | Runtime assurance / Simplex related; dual predicted envelopes in ECRL are integrated |
| One-use actuation bond | YES | Bond reuse detection (`BOND_REUSED`) before second actuation |
| Multi-horizon post-evidence | PARTIAL | Measurement windows exist; capsule-bound multi-horizon closure is the integration point |
| Revocable learning lineage | YES | Learning admitted only after digest-bound capsule closure |
| Sensors / actuators / PLC | NO | Commodity CPS components; VERINOX does not invent transducers |

### Layer 2 — Integration Novelty

Existing stacks offer watchdogs **or** failover **or** digital twins **or** process certification. They miss the ordered ECRL chain: **independent pre-evidence → dual envelopes → one-use bond → actuate → multi-horizon post → capsule closure → learning gate**, with fail-closed verdicts (`EVIDENCE_INDEPENDENT_FAIL`, `ENVELOPE_VIOLATION`, `BOND_REUSED`).

### Layer 3 — Architectural Novelty

**Principle:** Recovery is admitted to learning only when a digest-bound evidence-closed capsule closes.  
**Examiner sentence:** VERINOX AEGISLOOP's distinguishing claim is the Evidence-Closed Recovery Loop that binds independence, dual envelopes, one-use bonds, and measured closure into one admissible capsule — not failover alone.

## 3. Negative Claim Register

1. This is NOT SIL/ASIL or IEC 61508 / ISO 26262 certification.
2. This is NOT a patent grant or Freedom-to-Operate opinion.
3. This is NOT peer reviewed.
4. This is NOT independently third-party replicated.
5. This is NOT a production PLC / CPS controller replacement.
6. This is NOT universal causal discovery.
7. This is NOT HSM-backed trust hardware in the PoC.
8. This is NOT a complete digital twin product.
9. This is NOT medical device clearance.
10. This is NOT PDF-updated until regeneration is performed (**PDF REGENERATION NEEDED**).

## 4. Competitive Positioning

| Approach | Gap |
|----------|-----|
| Classic watchdog / failover | Lacks claim-scoped independence + capsule closure |
| Runtime assurance (Simplex) | Related envelopes; often lacks one-use bond + learning revoke |
| Digital twins | Prediction without bonded measured closure |
| IEC 61508 processes | Process/certification ≠ this executable ECRL artifact |
| ML ops rollback | Rarely binds dual counterfactual envelopes to actuation bonds |

## 5. Prior Art (10+)

Runtime assurance / Simplex; STPA; IEC 61508; ISO 26262; fault trees; dual-redundant sensors; smart contracts (bond analogy); author's ALETHEIA (evidence independence complementary); ROOTFALL (false plurality complementary); classical recovery managers.

## 6. Proof Sketches

**A** Totality of closure verdicts. **B** Shared single source root ⇒ EVIDENCE_INDEPENDENT_FAIL before envelope check. **C** Second actuate on same bond marks reuse ⇒ BOND_REUSED. Gate 8/8.

## 7. Real-World Scenario

Coolant recovery: RTD-1 + RTD-2 independent pre-evidence; valve one-use bond; post temp 72°C within [60,80] → CLOSURE_PASS; same-root sensors fail independence; 91°C violates envelope; double actuate → BOND_REUSED. (`verinox_realworld.py`)

## 8. Standards (honest PARTIAL)

IEC 61508 / ISO 26262: NONE claimed (not certified). EU AI Act high-risk CPS: PARTIAL mapping only. NIST AI RMF: PARTIAL. ISO 27001: NONE claimed.

## 9. Deployment

See `poc/verinox_deploy_manifest.json`. Not a safety-certified deployment.

## 10. Gap Register

G1 no hardware-in-loop validation; G2 no certification body engagement; G3 no third-party replication; G4 **PDF REGENERATION NEEDED**.

## 11. Version Note v3.0.0

Importable `verinox_aegisloop.VerinoxEngine`; full evidence suite; Zenodo/CITATION upgraded; NO SHRINK of v2.0 blueprint content above.

```text
VERINOX_AEGISLOOP_v3_0_0_EVIDENCE_UPGRADE
ECRL_LIBRARY_ADDED
PDF_REGENERATION_NEEDED
```

END OF PUBLICATION.
