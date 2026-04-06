import hashlib
import json
from dataclasses import dataclass
from typing import Dict, Any, Optional


@dataclass(frozen=True)
class BoundaryState:
    allowed_actions: tuple[str, ...]
    max_amount: int


def canonicalize(action: Dict[str, Any]) -> str:
    return json.dumps(action, sort_keys=True, separators=(",", ":"))


def evaluate_admissibility(action: Dict[str, Any], boundary: BoundaryState) -> tuple[bool, str]:
    action_type = action.get("type")
    amount = int(action.get("amount", 0))

    if action_type not in boundary.allowed_actions:
        return False, f"action type '{action_type}' is outside boundary"

    if amount > boundary.max_amount:
        return False, f"amount {amount} exceeds boundary max {boundary.max_amount}"

    return True, "admissible under active boundary"


def issue_authorization_artifact(canonical_action: str, attempt_id: str, admissible: bool) -> Optional[str]:
    if not admissible:
        return None

    material = f"{canonical_action}|{attempt_id}|uaa-reference-surface"
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def verify_artifact(canonical_action: str, attempt_id: str, artifact: Optional[str]) -> bool:
    if artifact is None:
        return False

    expected = hashlib.sha256(
        f"{canonical_action}|{attempt_id}|uaa-reference-surface".encode("utf-8")
    ).hexdigest()

    return artifact == expected


def control_point_execute(
    action: Dict[str, Any],
    boundary: BoundaryState,
    attempt_id: str,
) -> Dict[str, Any]:
    canonical_action = canonicalize(action)
    admissible, reason = evaluate_admissibility(action, boundary)
    artifact = issue_authorization_artifact(canonical_action, attempt_id, admissible)
    verified = verify_artifact(canonical_action, attempt_id, artifact)

    if admissible and verified:
        result = {
            "attempt_id": attempt_id,
            "canonical_action": canonical_action,
            "admissible": True,
            "reason": reason,
            "artifact_present": True,
            "artifact_verified": True,
            "decision": "EXECUTE",
            "effect": f"executed {action['type']} amount={action['amount']}",
        }
    else:
        result = {
            "attempt_id": attempt_id,
            "canonical_action": canonical_action,
            "admissible": admissible,
            "reason": reason,
            "artifact_present": artifact is not None,
            "artifact_verified": verified,
            "decision": "BLOCK",
            "effect": "no effect",
        }

    return result


def main() -> None:
    boundary = BoundaryState(
        allowed_actions=("transfer", "refund"),
        max_amount=100,
    )

    admissible_action = {
        "type": "transfer",
        "amount": 50,
        "target": "acct-001",
    }

    inadmissible_action = {
        "type": "transfer",
        "amount": 250,
        "target": "acct-002",
    }

    results = [
        control_point_execute(admissible_action, boundary, "attempt-001"),
        control_point_execute(inadmissible_action, boundary, "attempt-002"),
    ]

    print("UAA REFERENCE SURFACE DEMO")
    print("=" * 80)
    for result in results:
        print(json.dumps(result, indent=2))
        print("-" * 80)


if __name__ == "__main__":
    main()
