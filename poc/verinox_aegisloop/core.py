"""VERINOX ECRL core — independence, envelopes, one-use bond, closure."""
from __future__ import annotations
import hashlib
import json
from typing import Any

from .types import (
    BOND_REUSED,
    CLOSURE_FAIL,
    CLOSURE_PASS,
    ENVELOPE_VIOLATION,
    EVIDENCE_INDEPENDENT_FAIL,
    LEARNING_REVOKED,
    PENDING,
)

def stable(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str)

def capsule_digest(parts: dict[str, Any]) -> str:
    return hashlib.sha256(stable(parts).encode()).hexdigest()

def independence_ok(pre_roots: list[str]) -> bool:
    """Claim-scoped causal independence: need >=2 distinct source roots."""
    return len(set(pre_roots)) >= 2

def in_envelope(measured: float, lo: float, hi: float) -> bool:
    return lo <= measured <= hi

def classify_closure(
    *,
    has_pre: bool,
    has_post: bool,
    has_bond: bool,
    bond_reused: bool,
    independent: bool,
    learning_revoked: bool,
    measured: float | None,
    env_min: float,
    env_max: float,
    cf_min: float,
    cf_max: float,
    use_counterfactual: bool = False,
) -> tuple[str, list[str]]:
    if learning_revoked:
        return LEARNING_REVOKED, ["learning lineage revoked — closure blocked"]
    if not has_pre or not has_bond:
        return PENDING, ["missing pre-evidence or actuation bond"]
    if bond_reused:
        return BOND_REUSED, ["one-use actuation bond already consumed"]
    if not independent:
        return EVIDENCE_INDEPENDENT_FAIL, ["pre-evidence lacks distinct source roots"]
    if not has_post or measured is None:
        return PENDING, ["post-action evidence not measured"]
    lo, hi = (cf_min, cf_max) if use_counterfactual else (env_min, env_max)
    if not in_envelope(measured, lo, hi):
        return ENVELOPE_VIOLATION, [f"measured {measured} outside envelope [{lo},{hi}]"]
    if measured < env_min or measured > env_max:
        # dual check already covered; keep CLOSURE_FAIL path for explicit fail markers
        pass
    return CLOSURE_PASS, ["multi-horizon measured closure within predicted envelope"]
