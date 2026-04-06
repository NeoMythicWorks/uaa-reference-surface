# Authorization Artifact Model

This document defines the minimum model for UAA authorization artifacts.

---

## 1. Purpose

An authorization artifact is the per-attempt instrument by which execution authority is conveyed to the control point for verification.

It is not a standing permission.
It is not a role.
It is not a durable entitlement.

It is a constrained, attempt-specific authorization object.

---

## 2. Minimum Binding Requirements

A conformant artifact must be bound to:

- canonical action representation
- active boundary identity
- attempt identity
- validity interval
- anti-replay value

---

## 3. Minimum Fields

A minimum artifact model includes:

- ttempt_id
- ction_hash
- oundary_id
- issued_at
- expires_at
- 
once
- signature or equivalent integrity proof

Additional fields may be added, but these bindings may not be omitted.

---

## 4. Required Properties

### Per-Attempt
An artifact authorizes one attempt only.

### Non-Replayable
A used artifact must not be reusable.

### Time-Bound
An artifact must have a validity interval.

### Boundary-Bound
An artifact must not validate under a different boundary.

### Action-Bound
An artifact must not validate for a different action.

### Integrity-Protected
An artifact must support verification against tampering.

---

## 5. Verification Requirements

The control point must verify:

- action hash equality
- boundary identity equality
- current time within validity interval
- nonce unused
- integrity proof valid

Any failure resolves to block.

---

## 6. Non-Conformant Substitutes

The following are not authorization artifacts in the UAA sense:

- role membership alone
- API key alone
- session alone
- user identity alone
- static permission flag
- post-hoc logging marker

---

## 7. Conformance Condition

A system is conformant with the UAA artifact model only if execution depends on a valid, bound, non-replayable, time-bounded artifact verified at the control point.
