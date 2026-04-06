# Conformance Mapping

This document defines the binding between UAA invariants, execution semantics, and observable system behavior.

It exists to eliminate ambiguity in how UAA components relate and to demonstrate that the system is internally consistent.

---

## 1. Purpose

UAA is defined by invariants, executed through semantics, and demonstrated through runtime behavior.

This document maps:

Invariant ? Semantic Rule ? Enforcement Mechanism ? Observable Outcome

---

## 2. Mapping Table

### I1. Non-Default Authority

- Semantic Rule:
  Authority is not present at action proposal or canonicalization.

- Enforcement Mechanism:
  Execution requires a valid authorization artifact at the control point.

- Observable Outcome:
  BLOCKED: no token

---

### I2. Admissibility Precedes Authority

- Semantic Rule:
  Authorization artifact issuance occurs only after admissibility evaluation.

- Enforcement Mechanism:
  issue_token() is not invoked for inadmissible actions.

- Observable Outcome:
  Inadmissible actions never produce executable artifacts.

---

### I3. Fail-Closed Execution

- Semantic Rule:
  Any failure in canonicalization, admissibility, authorization, or verification resolves to block.

- Enforcement Mechanism:
  Control point returns block on any failed check.

- Observable Outcome:
  All invalid conditions produce BLOCKED

---

### I4. Artifact-Required Execution

- Semantic Rule:
  Execution requires a valid authorization artifact.

- Enforcement Mechanism:
  Control point denies execution when artifact is absent.

- Observable Outcome:
  BLOCKED: no token

---

### I5. Control-Point Verification

- Semantic Rule:
  Authority must be verified immediately before execution.

- Enforcement Mechanism:
  All execution paths route through control_point.py.

- Observable Outcome:
  Direct execution attempts return BLOCKED: control point not invoked

---

### I6. No Effect on Block

- Semantic Rule:
  Blocked actions must not produce governed effects.

- Enforcement Mechanism:
  Execution is gated strictly after verification.

- Observable Outcome:
  No execution output is produced for blocked actions.

---

### I7. Replay Resistance

- Semantic Rule:
  Authorization artifacts are valid for a single use.

- Enforcement Mechanism:
  Nonce tracking via replay cache.

- Observable Outcome:
  BLOCKED: replay detected

---

### I8. Measurement is not Authority

- Semantic Rule:
  Observations or metrics do not grant execution authority.

- Enforcement Mechanism:
  No measurement path feeds directly into authorization.

- Observable Outcome:
  No execution occurs without artifact issuance regardless of system observation.

---

## 3. Cross-Layer Consistency

Each invariant is:

- defined in /core
- enforced in /formal
- instantiated in /examples/reference_surface
- observable via runtime output
- reconstructible via /audit

No invariant exists without:

- a semantic definition
- an enforcement path
- a runtime manifestation

---

## 4. Conformance Condition

A system is conformant with UAA only if:

- invariants are preserved across all execution stages
- semantic rules are implemented without contradiction
- enforcement mechanisms are non-bypassable
- observable outcomes match expected invariant behavior

---

## 5. Interpretation Constraint

UAA must be interpreted as a unified system.

Isolated interpretation of:
- invariants without semantics
- semantics without enforcement
- enforcement without audit

is non-conformant.

Conformance requires cross-layer consistency.

---

