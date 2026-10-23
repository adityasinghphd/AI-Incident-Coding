"""Protocol v3 mechanical assembly of reconciliation difference snapshots.

The model's wire response uses SCHEMA.json and returns only feature_key and
resolution in each difference row. The controller validates that wire response,
calls assemble with exactly the permitted immutable strict/lenient priors, then
validates the returned canonical record with the original reconcile schema and
common.validate_record (the job's VALIDATION_RULES.py reference). Assembly does
not make coding decisions, repair evidence, or replace canonical validation.
"""
from copy import deepcopy

from common import changed_keys, feature_objects


def assemble(record, priors):
    """Return a deep copy with exact prior snapshots added in model row order.

Only differences[*].strict and differences[*].lenient are inserted. Every other
model-authored value, including coding, evidence and resolutions, is preserved.
The input record and priors are never modified or referenced by mutable output
values. Invalid wire rows fail instead of being repaired or silently discarded.
"""
    if not isinstance(priors, dict) or set(priors) != {"strict", "lenient"}:
        raise ValueError("Assembly must use exactly the permitted strict/lenient priors")
    if not isinstance(record, dict) or record.get("stage") != "reconcile":
        raise ValueError("Assembly requires a reconciliation record")
    rows = record.get("differences")
    if not isinstance(rows, list):
        raise ValueError("Reconciliation differences must be an array")

    keys = []
    for row in rows:
        if not isinstance(row, dict) or set(row) != {"feature_key", "resolution"}:
            raise ValueError("Wire difference rows must contain only feature_key and resolution")
        key = row["feature_key"]
        if not isinstance(key, str):
            raise ValueError("Difference feature_key must be a string")
        keys.append(key)
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate difference feature_key")

    strict = priors["strict"]["coding"]
    lenient = priors["lenient"]["coding"]
    if set(keys) != changed_keys(strict, lenient):
        raise ValueError("Reconciliation must log every strict/lenient object difference exactly once")
    strict_features = feature_objects(strict)
    lenient_features = feature_objects(lenient)
    assembled = deepcopy(record)
    for row in assembled["differences"]:
        key = row["feature_key"]
        row["strict"] = deepcopy(strict_features.get(key))
        row["lenient"] = deepcopy(lenient_features.get(key))
    return assembled
