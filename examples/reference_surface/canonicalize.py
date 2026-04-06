import hashlib
import json

REQUIRED_FIELDS = {"action_type", "resource", "parameters"}

def canonicalize(action: dict) -> dict:
    missing = REQUIRED_FIELDS - action.keys()
    if missing:
        raise ValueError(f"Missing required fields: {sorted(missing)}")

    if not isinstance(action["parameters"], dict):
        raise ValueError("Field 'parameters' must be a dict.")

    return {
        "action_type": action["action_type"],
        "resource": action["resource"],
        "parameters": dict(sorted(action["parameters"].items())),
    }

def canonical_hash(action: dict) -> str:
    canonical = canonicalize(action)
    serialized = json.dumps(canonical, sort_keys=True)
    return hashlib.sha256(serialized.encode()).hexdigest()