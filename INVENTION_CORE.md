# Narrow Invention Core

## Technical problem

Autonomous recovery systems may:

- treat evidence from one hidden causal root as independent confirmation;
- authorize an action after state or topology has changed;
- confuse command completion with physical recovery;
- credit a desired outcome to the action when an external event caused it;
- close before delayed instability appears; or
- learn from a recovery later shown to be invalid.

## Proposed transaction

The causally bound evidence-closed recovery transaction is:

\[
T=\langle S,C,R,P,F,B,A,O,L,Q\rangle
\]

| Symbol | Object | Function |
|---|---|---|
| S | Canonical State Envelope | Freezes pre-action state, topology, identity, policy, and evidence roots |
| C | Claim-Scoped Causal Independence Proof | Tests evidence dependencies separately for each mandatory claim |
| R | Recovery Candidate Capsule | Binds state, evidence, action, blast radius, rollback, proofs, and deadlines |
| P | Dual Counterfactual Outcome Envelope | Predicts intervention and safe fallback outcomes with uncertainty |
| F | Proof and refutation result | Checks invariants and attempts specified counterexamples |
| B | One-Time Recovery Actuation Bond | Authorizes only the exact actuator command in the exact recovery epoch |
| A | Actuator-signed action record | Proves local acceptance or rejection and bond consumption |
| O | Multi-horizon observations | Measures immediate, stabilized, and delayed outcomes |
| L | Closure or superseding receipt | Records provisional, stable, retrospective, reopened, or revoked state |
| Q | Revocable Learning Lineage | Traces downstream artifacts influenced by the closure |

## Candidate technical contributions

### 1. Claim-scoped causal independence

Evidence independence is evaluated for each required claim through a dependency hypergraph. Shared power, clock, calibration, firmware, model, network, operator, training-data, and attestation roots are treated as possible common causes. Unknown dependencies lower assurance rather than defaulting to independence.

### 2. Dual counterfactual recovery prediction

The transaction carries both (Y(do(a))) and (Y(do(a_0))), where (a) is the proposed recovery and (a_0) is safe hold, no action, or fallback. Commit requires safe predicted behavior and a policy-defined useful effect. Final attribution requires observations to distinguish the branches within declared uncertainty.

### 3. One-use bonded actuation

The actuator receives a locally verifiable capability bound to capsule, state, command, actuator identity, recovery epoch, expiry, prediction, and rollback. Any change or replay invalidates the bond. Consumption is signed by the actuator or safety root.

### 4. Multi-horizon closure and reopening

Closure progresses from executed-unverified to provisional, stable, and retrospective. Later contradictions can reopen or revoke the result through a new signed receipt; prior history is never erased.

### 5. Revocable learning lineage

Every model, policy, dataset, rule, or reward influenced by an accepted recovery retains lineage to its closure receipt. Reopening triggers deterministic containment and records the selected rollback, retraining, or unlearning response and residual uncertainty.

## Strongest combination claim candidate

A recovery-control system or method that, within one immutable transaction:

1. computes claim-specific causal evidence independence;
2. binds intervention and fallback counterfactual outcomes;
3. issues a one-use actuator-verified capability;
4. measures physical or hardware-attested results over several time horizons;
5. permits retrospective closure only after outcome and attribution checks; and
6. traces and contains downstream learning influence if closure is later invalidated.

At least one readback path should be physically or administratively independent of the command path in the preferred embodiment.

## Concepts expressly not claimed alone

- Simplex or runtime-assurance switching;
- pre-action safety certificates;
- digital twins or causal models;
- two-phase commit;
- attestation or signed receipts;
- fault isolation and rollback;
- sensor fusion or majority voting;
- safe reinforcement-learning shields;
- provenance graphs; or
- machine unlearning.

