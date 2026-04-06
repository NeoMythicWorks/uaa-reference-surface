# Conformance Mapping

This document defines the binding between UAA invariants, execution semantics, and observable system behavior.

It exists to eliminate ambiguity in how UAA components relate and to demonstrate that the system is internally consistent.

---

## Purpose

UAA is defined by invariants, executed through semantics, and demonstrated through runtime behavior.

This document maps:

Invariant ? Semantic Rule ? Enforcement Mechanism ? Observable Outcome

---

## I1. Non-Default Authority

- Semantic Rule:
  Authority is not present at action proposal or canonicalization.

- Enforcement Mechanism:
  Execution requires a valid authorization artifact at the control point.

- Observable Outcome:
  BLOCKED: no token

---

## I2. Admissibility Precedes Authority

- Semantic Rule:
  Authorization artifact issuance occurs only after admissibility evaluation.

- Enforcement Mechanism:
  Inadmissible actions do not produce executable artifacts.

- Observable Outcome:
  Invalid action evaluates inadmissible and does not execute.

---

## I3. Fail-Closed Execution

- Semantic Rule:
  Any failure in evaluation, authorization, or verification resolves to block.

- Enforcement Mechanism:
  Control-point checks deny execution on any invalid state.

- Observable Outcome:
  Invalid conditions produce BLOCKED

---

## I4. Artifact-Required Execution

- Semantic Rule:
  Execution requires a valid authorization artifact.

- Enforcement Mechanism:
  Control point denies execution when artifact is absent.

- Observable Outcome:
  BLOCKED: no token

---

## I5. Control-Point Verification

- Semantic Rule:
  Authority must be verified immediately before execution.

- Enforcement Mechanism:
  All governed execution paths route through the control point.

- Observable Outcome:
  Direct execution attempts return BLOCKED: control point not invoked

---

## I6. No Effect on Block

- Semantic Rule:
  Blocked actions must not produce governed effects.

- Enforcement Mechanism:
  Effectuation occurs only after successful verification.

- Observable Outcome:
  No executed result is produced for blocked attempts.

---

## I7. Replay Resistance

- Semantic Rule:
  Authorization artifacts are single-use and non-replayable.

- Enforcement Mechanism:
  Nonce tracking via replay cache.

- Observable Outcome:
  BLOCKED: replay detected

---

## I8. Measurement Is Not Authority

- Semantic Rule:
  Observation or telemetry cannot grant execution authority.

- Enforcement Mechanism:
  No measurement path can substitute for authorization artifact issuance.

- Observable Outcome:
  No execution occurs without valid authorization regardless of observation.

---

## Cross-Layer Consistency

Each invariant is:

- defined in /core
- formalized in /formal
- instantiated in /examples/reference_surface
- observable through runtime behavior
- reconstructible through /audit

No invariant is complete unless all five layers align.

---

## Conformance Condition

A system is conformant with UAA only if:

- invariants are preserved across all execution stages
- semantic rules are implemented without contradiction
- enforcement mechanisms are non-bypassable
- observable outcomes match expected invariant behavior
