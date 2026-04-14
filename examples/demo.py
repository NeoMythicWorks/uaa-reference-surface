from authorization import issue_authorization_artifact, verify
import json

_seen = set()

def verify_at_control_point(artifact, required_state):
    if not artifact:
        return False, "no authorization artifact"
    if not verify(artifact):
        return False, "invalid authorization artifact"

    payload = artifact["payload"]
    parsed = json.loads(payload)
    embedded_state = parsed.get("state", {})

    if embedded_state != required_state:
        return False, "boundary mismatch"

    if payload in _seen:
        return False, "replay detected"

    _seen.add(payload)
    return True, "action permitted"

def show(ok, msg):
    print("[EXECUTED]" if ok else "[BLOCKED]", msg)

action = {"type": "WRITE"}
good_state = {"allow_execution": True, "boundary": "ledger"}
bad_state = {"allow_execution": True, "boundary": "other"}

show(*verify_at_control_point(None, good_state))

bad = {"payload": "bad", "sig": "bad"}
show(*verify_at_control_point(bad, good_state))

artifact_ok = issue_authorization_artifact(action, good_state)
show(*verify_at_control_point(artifact_ok, good_state))

show(*verify_at_control_point(artifact_ok, good_state))

artifact_mismatch = issue_authorization_artifact(action, good_state)
show(*verify_at_control_point(artifact_mismatch, bad_state))
