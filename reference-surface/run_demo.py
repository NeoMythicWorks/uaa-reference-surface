import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from canonicalize import canonicalize
from admissibility import is_admissible
from authorization import issue_token
from control_point import execute
from replay_cache import ReplayCache


def separator(label: str) -> None:
    print(f"\n{'='*60}")
    print(f"  {label}")
    print('='*60)


def main():
    separator("Step 1: Define boundary")
    boundary = {
        "id": "boundary-001",
        "allowed_actions": ["read"],
        "allowed_resources": ["file1"],
    }
    print(boundary)

    cache = ReplayCache()

    separator("Step 2: Create action")
    raw_action = {
        "action_type": "read",
        "resource": "file1",
        "parameters": {"mode": "r"}
    }
    print(raw_action)

    separator("Step 3: Canonicalize")
    canonical = canonicalize(raw_action)
    print(canonical)

    separator("Step 4: Admissibility")
    admissible = is_admissible(canonical, boundary)
    print(admissible)

    separator("Step 5: Issue token")
    if admissible:
        token = issue_token(canonical, boundary["id"])
        print(token)
    else:
        token = None

    separator("Step 6: Execute (expect EXECUTED)")
    execute(canonical, token, boundary, cache)

    separator("Step 7: Replay (expect BLOCKED)")
    execute(canonical, token, boundary, cache)

    separator("Step 8: Invalid action")
    bad = {
        "action_type": "write",
        "resource": "file1",
        "parameters": {}
    }

    bad_canonical = canonicalize(bad)

    separator("Step 9: Admissibility (expect False)")
    print(is_admissible(bad_canonical, boundary))

    separator("Step 10: Execute without token (expect BLOCKED)")
    execute(bad_canonical, None, boundary, cache)


if __name__ == "__main__":
    main()
