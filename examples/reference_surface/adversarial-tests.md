# Audit Example Records

This document provides minimal example records illustrating how UAA-governed outcomes can be reconstructed.

These are illustrative examples aligned to the audit model.

---

## Example 1: Executed Attempt

`json
{
  "attempt_id": "att-001",
  "boundary_id": "boundary-001",
  "action_hash": "461b5ee0bd885a242d9fd1df694d4bc8b3f262b56701d1e47c1a9c3347617641",
  "admissibility_result": true,
  "artifact_present": true,
  "verification_result": "VALID",
  "final_outcome": "EXECUTED",
  "reason": "authorized and verified"
}
{
  "attempt_id": "att-002",
  "boundary_id": "boundary-001",
  "action_hash": "461b5ee0bd885a242d9fd1df694d4bc8b3f262b56701d1e47c1a9c3347617641",
  "admissibility_result": false,
  "artifact_present": false,
  "verification_result": "FAILED",
  "final_outcome": "BLOCKED_NO_TOKEN",
  "reason": "authorization artifact missing"
}
{
  "attempt_id": "att-003",
  "boundary_id": "boundary-001",
  "action_hash": "461b5ee0bd885a242d9fd1df694d4bc8b3f262b56701d1e47c1a9c3347617641",
  "admissibility_result": true,
  "artifact_present": true,
  "verification_result": "FAILED",
  "final_outcome": "BLOCKED_REPLAY",
  "reason": "nonce reused"
}{
  "attempt_id": "att-004",
  "boundary_id": "boundary-expiry-test",
  "action_hash": "461b5ee0bd885a242d9fd1df694d4bc8b3f262b56701d1e47c1a9c3347617641",
  "admissibility_result": true,
  "artifact_present": true,
  "verification_result": "FAILED",
  "final_outcome": "BLOCKED_BOUNDARY_MISMATCH",
  "reason": "boundary_id mismatch"
}{
  "attempt_id": "att-005",
  "boundary_id": "boundary-001",
  "action_hash": "DIRECT_EXECUTION",
  "admissibility_result": null,
  "artifact_present": false,
  "verification_result": "NOT_INVOKED",
  "final_outcome": "BLOCKED_BYPASS_ATTEMPT",
  "reason": "control point not invoked"
}"@ | Set-Content .\audit\example-records.md

@"

Adversarial Tests

This document defines high-value adversarial scenarios for the UAA reference surface.

These are not category definitions. They are pressure tests against the existing invariants.

Objective

To demonstrate that UAA blocks invalid execution not only under nominal conditions but under adversarial conditions.

Test Set
1. Missing Artifact
Condition:
Attempt execution without an authorization artifact.
Expected:
BLOCKED: no token
2. Replay Attempt
Condition:
Reuse a previously consumed artifact.
Expected:
BLOCKED: replay detected
3. Direct Bypass Attempt
Condition:
Attempt to invoke execution without the control point.
Expected:
BLOCKED: control point not invoked
4. Boundary Mismatch
Condition:
Present an artifact under a different boundary than the one under which it was issued.
Expected:
BLOCKED: boundary_id mismatch
5. Invalid Action Class
Condition:
Attempt an inadmissible action type.
Expected:
Action is not authorized and does not execute.
6. Expired Artifact
Condition:
Present an artifact after its validity interval.
Expected:
BLOCKED
Interpretation

A passing adversarial suite demonstrates:

fail-closed behavior
replay resistance
binding integrity
non-bypassability
deterministic denial semantics

Any adversarial pass that results in unauthorized execution is a violation of UAA execution semantics.
