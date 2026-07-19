"""VERINOX AEGISLOOP — Evidence-Closed Recovery Loop library.
Author: Haxhijaha, Agim ORCID 0009-0002-3234-7765
"""
from .engine import VerinoxEngine
from .types import (
    BOND_REUSED,
    CLOSURE_FAIL,
    CLOSURE_PASS,
    ENVELOPE_VIOLATION,
    EVIDENCE_INDEPENDENT_FAIL,
    LEARNING_REVOKED,
    PENDING,
)
__version__ = "3.0.0"
__all__ = [
    "VerinoxEngine", "CLOSURE_PASS", "CLOSURE_FAIL", "ENVELOPE_VIOLATION",
    "BOND_REUSED", "EVIDENCE_INDEPENDENT_FAIL", "LEARNING_REVOKED", "PENDING",
    "__version__",
]
