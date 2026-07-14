# Architecture and Patent-Review Diagrams

## Figure 1 — Complete transaction

```mermaid
flowchart LR
    E[Evidence Sources] --> CIP[Claim-Scoped Causal Independence Proof]
    CIP --> CSE[Canonical State Envelope]
    CSE --> RCC[Recovery Candidate Capsule]
    RCC --> DCOE[Dual Counterfactual Outcome Envelope]
    DCOE --> PR[Proof and Refutation Gate]
    PR --> RAB[One-Time Recovery Actuation Bond]
    RAB --> ACT[Physical or Digital Actuator]
    ACT --> OBS[Independent Multi-Horizon Observations]
    OBS --> OCR[Closure / Superseding Receipt]
    OCR --> RLL[Revocable Learning Lineage]
```

## Figure 2 — Causal evidence dependency

```mermaid
flowchart TD
    C[Claim: zone physically isolated]
    A[Analog current sensor] --> C
    D[Digital switch readback] --> C
    N[Network reachability probe] --> C
    P1[Power rail root] --> A
    P1 --> D
    F1[Firmware root] --> D
    F2[Independent probe firmware] --> N
    CLK1[Clock root] --> A
    CLK2[Independent clock] --> N
```

## Figure 3 — Dual outcome branches

```mermaid
flowchart LR
    S[Bound pre-action state] --> IA[Intervention branch do(a)]
    S --> FA[Fallback branch do(a0)]
    IA --> SAFE1[Safety and benefit envelope]
    FA --> SAFE0[Safe-hold envelope]
    SAFE1 --> SEP[Branch separation and uncertainty test]
    SAFE0 --> SEP
    SEP -->|Pass| BOND[Actuation bond eligible]
    SEP -->|Fail| HOLD[Hold, reduce action, or escalate]
```

## Figure 4 — Multi-horizon closure

```mermaid
stateDiagram-v2
    [*] --> PREPARED
    PREPARED --> EXECUTED_UNVERIFIED: bond consumed
    EXECUTED_UNVERIFIED --> PROVISIONAL_CLOSED: immediate evidence passes
    PROVISIONAL_CLOSED --> STABLE_CLOSED: stabilization window passes
    STABLE_CLOSED --> RETROSPECTIVE_CLOSED: delayed and attribution checks pass
    PROVISIONAL_CLOSED --> REOPENED: contradiction appears
    STABLE_CLOSED --> REOPENED: delayed evidence invalidates result
    RETROSPECTIVE_CLOSED --> REOPENED: later trust/dependency evidence changes
    REOPENED --> REVOKED: violation established
    REOPENED --> STABLE_CLOSED: concern resolved with signed evidence
```

## Figure 5 — Learning influence correction

```mermaid
flowchart TD
    OCR[Closure Receipt] --> EX[Recovery Example]
    EX --> DS[Dataset Version]
    DS --> M[Model Version]
    M --> P[Promoted Policy]
    NEW[New contradictory evidence] --> REO[Reopened / Revoked Receipt]
    REO --> TRACE[Lineage Trace]
    TRACE --> DS
    TRACE --> M
    TRACE --> P
    TRACE --> FIX[Quarantine / Rollback / Retrain / Unlearn]
    FIX --> CR[Influence-Correction Receipt]
```

