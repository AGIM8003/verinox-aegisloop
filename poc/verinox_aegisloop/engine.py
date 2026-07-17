"""VerinoxEngine — Evidence-Closed Recovery Loop.
Author: Haxhijaha, Agim ORCID 0009-0002-3234-7765
"""
from __future__ import annotations
from typing import Any

from .core import capsule_digest, classify_closure, independence_ok
from .types import ActuationBond, OutcomeEnvelope, PostEvidence, PreEvidence, RecoveryCapsule
from .validators import require_float, require_id, require_text

_LIMITS = (
    "Bounded evidence-closed recovery control only. VERINOX does not claim "
    "certified functional safety, patent grant, production CPS deployment, "
    "peer review, or independent replication."
)

class VerinoxEngine:
    """Pre-evidence -> dual envelopes -> one-use bond -> actuate -> post-evidence -> closure.

    Usage:
        e = VerinoxEngine()
        e.add_pre("E1", claim_scope="temp", source_root="sensorA", value=1.0)
        e.add_pre("E2", claim_scope="temp", source_root="sensorB", value=1.1)
        e.set_envelope(predicted_min=0.5, predicted_max=2.0,
                       counterfactual_min=0.0, counterfactual_max=3.0)
        e.issue_bond("B1")
        e.actuate("B1")
        e.add_post("P1", measured=1.2, horizon="t+5m")
        print(e.close("CAP1", claim_scope="temp")["verdict"])
    """

    def __init__(self) -> None:
        self._pre: dict[str, PreEvidence] = {}
        self._post: dict[str, PostEvidence] = {}
        self._bonds: dict[str, ActuationBond] = {}
        self._envelope: OutcomeEnvelope | None = None
        self._learning_revoked = False

    def add_pre(self, evidence_id: str, *, claim_scope: str, source_root: str, value: float) -> PreEvidence:
        evidence_id = require_id("evidence_id", evidence_id)
        if evidence_id in self._pre:
            raise ValueError(f"duplicate pre evidence: {evidence_id}")
        ev = PreEvidence(
            evidence_id=evidence_id,
            claim_scope=require_text("claim_scope", claim_scope),
            source_root=require_text("source_root", source_root),
            value=require_float("value", value),
        )
        self._pre[evidence_id] = ev
        return ev

    def set_envelope(
        self,
        *,
        predicted_min: float,
        predicted_max: float,
        counterfactual_min: float,
        counterfactual_max: float,
    ) -> OutcomeEnvelope:
        self._envelope = OutcomeEnvelope(
            predicted_min=require_float("predicted_min", predicted_min),
            predicted_max=require_float("predicted_max", predicted_max),
            counterfactual_min=require_float("counterfactual_min", counterfactual_min),
            counterfactual_max=require_float("counterfactual_max", counterfactual_max),
        )
        return self._envelope

    def issue_bond(self, bond_id: str) -> ActuationBond:
        bond_id = require_id("bond_id", bond_id)
        if bond_id in self._bonds:
            raise ValueError(f"duplicate bond: {bond_id}")
        b = ActuationBond(bond_id=bond_id, used=False)
        self._bonds[bond_id] = b
        return b

    def actuate(self, bond_id: str) -> dict[str, Any]:
        bond_id = require_id("bond_id", bond_id)
        if bond_id not in self._bonds:
            raise ValueError(f"unknown bond: {bond_id}")
        b = self._bonds[bond_id]
        if b.used:
            self._bond_reuse_attempted = True
            return {"ok": False, "reason": "bond already used"}
        b.used = True
        return {"ok": True, "bond_id": bond_id}

    def add_post(self, evidence_id: str, *, measured: float, horizon: str = "primary") -> PostEvidence:
        evidence_id = require_id("evidence_id", evidence_id)
        if evidence_id in self._post:
            raise ValueError(f"duplicate post evidence: {evidence_id}")
        ev = PostEvidence(
            evidence_id=evidence_id,
            measured=require_float("measured", measured),
            horizon=require_text("horizon", horizon),
        )
        self._post[evidence_id] = ev
        return ev

    def revoke_learning(self) -> None:
        self._learning_revoked = True

    def close(self, capsule_id: str, *, claim_scope: str, bond_id: str | None = None) -> dict[str, Any]:
        capsule_id = require_id("capsule_id", capsule_id)
        claim_scope = require_text("claim_scope", claim_scope)
        pre = [p for p in self._pre.values() if p.claim_scope == claim_scope]
        roots = [p.source_root for p in pre]
        bond = None
        if bond_id:
            bond = self._bonds.get(bond_id)
        elif self._bonds:
            bond = next(iter(self._bonds.values()))
        posts = list(self._post.values())
        measured = posts[-1].measured if posts else None
        env = self._envelope
        # Detect bond reuse attempt: if bond used AND we try close after second actuate fail path
        bond_reused = False
        if bond is not None and bond.used:
            # one-use: closing after successful single use is OK; reuse means actuate was attempted twice
            # Track via a side flag if actuate returned not ok previously — approximate:
            # If caller issues close without ever actuating, bond.used is False.
            # If actuate succeeded once, used True — that is normal for closure.
            # BOND_REUSED is signaled when actuate is called on already-used bond, then close checks marker.
            bond_reused = getattr(self, "_bond_reuse_attempted", False)

        verdict, reasons = classify_closure(
            has_pre=bool(pre),
            has_post=bool(posts),
            has_bond=bond is not None,
            bond_reused=bond_reused,
            independent=independence_ok(roots),
            learning_revoked=self._learning_revoked,
            measured=measured,
            env_min=env.predicted_min if env else 0.0,
            env_max=env.predicted_max if env else 0.0,
            cf_min=env.counterfactual_min if env else 0.0,
            cf_max=env.counterfactual_max if env else 0.0,
        )
        parts = {
            "capsule_id": capsule_id,
            "claim_scope": claim_scope,
            "pre": [p.evidence_id for p in pre],
            "post": [p.evidence_id for p in posts],
            "verdict": verdict,
            "reasons": reasons,
            "envelope": env.__dict__ if env else None,
            "bond_id": bond.bond_id if bond else None,
        }
        digest = capsule_digest(parts)
        return {
            "verdict": verdict,
            "reasons": reasons,
            "capsule_digest": digest,
            "limits": _LIMITS,
            "details": parts,
        }

    def mark_bond_reuse_attempt(self) -> None:
        self._bond_reuse_attempted = True

    def issue_recovery_capsule(self, capsule_id: str, *, claim_scope: str) -> dict[str, Any]:
        d = self.close(capsule_id, claim_scope=claim_scope)
        return {
            "type": "recovery_capsule",
            "capsule_id": capsule_id,
            "verdict": d["verdict"],
            "capsule_digest": d["capsule_digest"],
            "limits": _LIMITS,
        }
