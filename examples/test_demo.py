from authorization import issue_authorization_artifact, verify
import json
import sys

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

def assert_case(name, result, expected_msg):
    ok, msg = result
    passed = (msg == expected_msg)

    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {name} - {msg}")

    if not passed:
        return False
    return True

def run_tests():
    action = {"type": "WRITE"}
    good_state = {"allow_execution": True, "boundary": "ledger"}
    bad_state = {"allow_execution": True, "boundary": "other"}

    results = []

    results.append(assert_case(
        "no artifact",
        verify_at_control_point(None, good_state),
        "no authorization artifact"
    ))

    bad = {"payload": "bad", "sig": "bad"}
    results.append(assert_case(
        "invalid artifact",
        verify_at_control_point(bad, good_state),
        "invalid authorization artifact"
    ))

    artifact_ok = issue_authorization_artifact(action, good_state)
    results.append(assert_case(
        "valid execution",
        verify_at_control_point(artifact_ok, good_state),
        "action permitted"
    ))

    results.append(assert_case(
        "replay",
        verify_at_control_point(artifact_ok, good_state),
        "replay detected"
    ))

    artifact_mismatch = issue_authorization_artifact(action, good_state)
    results.append(assert_case(
        "boundary mismatch",
        verify_at_control_point(artifact_mismatch, bad_state),
        "boundary mismatch"
    ))

    if all(results):
        print("\nALL TESTS PASSED")
        sys.exit(0)
    else:
        print("\nTEST FAILURE")
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
