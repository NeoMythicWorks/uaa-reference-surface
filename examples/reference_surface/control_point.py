"""
control_point.py - UAA Reference Surface

Verifies an authorization artifact and gates execution.
All verification steps are performed in order. Any failure blocks execution.
"""

import hashlib
import json
import time

from canonicalize import canonical_hash


def _hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


def _recompute_signature(token: dict) -> str:
    payload = json.dumps({
        "attempt_id": token["attempt_id"],
        "action_hash": token["action_hash"],
        "boundary_id": token["boundary_id"],
        "issued_at": token["issued_at"],
        "expires_at": token["expires_at"],
        "nonce": token["nonce"],
    }, sort_keys=True)
    return _hash(payload)


def execute(action: dict, token, boundary: dict, replay_cache) -> None:
    """
    Verify the authorization artifact and gate execution.

    Verification steps (in order):
        1. Token exists (is not None)
        2. Signature is valid
        3. action_hash matches the canonical action
        4. boundary_id matches the current boundary
        5. Nonce has not been used before (replay prevention)
        6. Token has not expired

    If any check fails: print "BLOCKED" and return without executing.
    If all checks pass: print "EXECUTED".
    """
    boundary_id = boundary.get("id", "")

    # Step 1: token exists
    if token is None:
        print("BLOCKED: no token")
        return

    # Step 2: signature valid
    expected_sig = _recompute_signature(token)
    if token.get("signature") != expected_sig:
        print("BLOCKED: invalid signature")
        return

    # Step 3: action_hash matches canonical action representation
    if token.get("action_hash") != canonical_hash(action):
        print("BLOCKED: action hash mismatch")
        return

    # Step 4: boundary_id matches current boundary
    if token.get("boundary_id") != boundary_id:
        print("BLOCKED: boundary_id mismatch")
        return

    # Step 5: nonce not reused
    if not replay_cache.check_and_store(token["nonce"]):
        print("BLOCKED: replay detected (nonce reused)")
        return

    # Step 6: token not expired
    if time.time() > token.get("expires_at", 0):
        print("BLOCKED: token expired")
        return

    print("EXECUTED")
