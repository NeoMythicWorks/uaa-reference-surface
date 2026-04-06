# Foundational Invariants

This document defines the foundational invariants of Unified Agency Architecture (UAA).

These invariants are not implementation preferences. They are category-defining conditions. A system that violates any of them is not conformant with UAA.

---

## I1. Non-Default Authority

Execution authority does not exist by default.

The ability to generate, recommend, select, or prepare an action does not by itself confer permission for that action to execute.

Consequence: capability and authority are separate states.

---

## I2. Admissibility Precedes Authority

Authority may only be derived after evaluation of a proposed action against an active governing boundary.

Admissibility is a runtime determination over the action representation and the relevant boundary state.

Consequence: authority cannot be assumed, cached as a permanent entitlement, or inferred from action availability alone.

---

## I3. Fail-Closed Execution

If admissibility cannot be established, authorization cannot be issued.

If authorization cannot be issued, execution cannot proceed.

If verification fails, execution is denied.

Consequence: indeterminacy, evaluation failure, verification failure, or missing authorization all resolve to non-execution.

---

## I4. Artifact-Required Execution

Execution requires a valid authorization artifact bound to the specific attempt.

The artifact must be derived from a successful admissibility determination and presented at the control point immediately prior to execution.

Consequence: execution without a valid artifact is non-conformant.

---

## I5. Control-Point Verification

Authorization must be verified at a mandatory control point on the execution path.

Verification occurs immediately prior to execution and must validate the presented artifact against the attempted action and relevant execution context.

Consequence: pre-execution verification is required; earlier approval alone is insufficient.

---

## I6. No Effect on Block

A blocked action must produce no governed effect.

If admissibility fails, authorization is absent, replay is detected, or verification fails, the governed execution must not occur.

Consequence: denial must prevent effectuation.

---

## I7. Replay Resistance

Authorization artifacts are per-attempt and non-replayable.

An artifact valid for one attempt must not be reusable for another attempt, even if the nominal action appears identical.

Consequence: prior authorization cannot be replayed.

---

## I8. Measurement Is Not Authority

Measurement, scoring, telemetry, prediction, or monitoring output cannot grant execution authority by themselves.

These signals may inform admissibility but do not constitute permission.

Consequence: measurement systems are not governing systems.

---

## I9. Immediate Pre-Execution Validation

Execution authority must be validated at the control point immediately prior to execution.

Consequence: authority is not durable or implied across time.

---

## I10. Non-Bypassable Enforcement

No execution path may bypass control-point verification.

All governed execution must traverse an enforcement interface.

Consequence: enforcement is architectural, not advisory.

---

## Conformance Statement

A system is conformant with UAA only if these invariants are enforced at the execution boundary.
