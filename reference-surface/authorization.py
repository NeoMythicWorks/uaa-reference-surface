import hashlib
import json
import time
import uuid

TOKEN_TTL_SECONDS = 5


def _hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


def issue_token(action: dict, boundary_id: str) -> dict:
    """
    Issue an authorization artifact bound to the canonical action representation
    and the current boundary state.

    Fields:
        attempt_id   - unique identifier for this action attempt
        action_hash  - SHA-256 hash of the canonical action representation
        boundary_id  - identifier of the boundary state at time of issuance
        issued_at    - Unix timestamp of issuance
        expires_at   - Unix timestamp of expiry (issued_at + TOKEN_TTL_SECONDS)
        nonce        - unique value; no two tokens share a nonce
        signature    - SHA-256 hash of all other fields (integrity proof)
    """
    attempt_id = str(uuid.uuid4())
    action_hash = _hash(json.dumps(action, sort_keys=True))
    issued_at = time.time()
    expires_at = issued_at + TOKEN_TTL_SECONDS
    nonce = str(uuid.uuid4())

    payload = json.dumps({
        "attempt_id": attempt_id,
        "action_hash": action_hash,
        "boundary_id": boundary_id,
        "issued_at": issued_at,
        "expires_at": expires_at,
        "nonce": nonce,
    }, sort_keys=True)

    signature = _hash(payload)

    return {
        "attempt_id": attempt_id,
        "action_hash": action_hash,
        "boundary_id": boundary_id,
        "issued_at": issued_at,
        "expires_at": expires_at,
        "nonce": nonce,
        "signature": signature,
    }