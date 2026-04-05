def is_admissible(action: dict, boundary: dict) -> bool:
    """
    Return True only if action_type and resource are both permitted by the boundary.
    Return False otherwise. Result is binary; no intermediate values.

    boundary example:
        {
            "allowed_actions": ["read"],
            "allowed_resources": ["file1"]
        }
    """
    allowed_actions = boundary.get("allowed_actions", [])
    allowed_resources = boundary.get("allowed_resources", [])

    if action.get("action_type") not in allowed_actions:
        return False
    if action.get("resource") not in allowed_resources:
        return False

    return True