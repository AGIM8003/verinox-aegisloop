"""VERINOX types — ECRL recovery capsule vocabulary."""
from __future__ import annotations
from dataclasses import dataclass, field

CLOSURE_PASS = "CLOSURE_PASS"
CLOSURE_FAIL = "CLOSURE_FAIL"
ENVELOPE_VIOLATION = "ENVELOPE_VIOLATION"
BOND_REUSED = "BOND_REUSED"
EVIDENCE_INDEPENDENT_FAIL = "EVIDENCE_INDEPENDENT_FAIL"
LEARNING_REVOKED = "LEARNING_REVOKED"
PENDING = "PENDING"

@dataclass
class PreEvidence:
    evidence_id: str
    claim_scope: str
    source_root: str
    value: float

@dataclass
class OutcomeEnvelope:
    predicted_min: float
    predicted_max: float
    counterfactual_min: float
    counterfactual_max: float

@dataclass
class ActuationBond:
    bond_id: str
    used: bool = False

@dataclass
class PostEvidence:
    evidence_id: str
    measured: float
    horizon: str

@dataclass
class RecoveryCapsule:
    capsule_id: str
    claim_scope: str
    bond_id: str
    envelope: OutcomeEnvelope
    pre_ids: list[str] = field(default_factory=list)
    post_ids: list[str] = field(default_factory=list)
    learning_revoked: bool = False
    digest: str = ""
