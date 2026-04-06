# Audit Model

This document defines the minimum audit model for UAA-governed execution.

---

## 1. Purpose

Audit records exist to make execution outcomes reconstructible.

A conformant audit layer must make it possible to distinguish:

- what was attempted
- what boundary governed the attempt
- whether authority was derived
- whether execution occurred
- whether the attempt was blocked
- why the final outcome occurred

---

## 2. Minimum Record Types

A minimal UAA audit model should support:

- execution attempt record
- execution success record
- execution block record

These may be unified or separated, but the information must be reconstructible.

---

## 3. Minimum Fields

A minimal audit record should include:

- ttempt_id
- oundary_id
- ction_hash or canonical action identifier
- dmissibility_result
- rtifact_present
- erification_result
- inal_outcome
- eason

Optional but useful:
- timestamps
- nonce
- actor or initiator metadata
- correlation identifiers

---

## 4. Outcome Semantics

The audit model must distinguish at minimum:

- EXECUTED
- BLOCKED_NO_TOKEN
- BLOCKED_REPLAY
- BLOCKED_BOUNDARY_MISMATCH
- BLOCKED_BYPASS_ATTEMPT
- BLOCKED_INADMISSIBLE
- BLOCKED_VERIFICATION_FAILURE

---

## 5. Proof Requirements

A conformant audit layer must support reconstruction of:

- proof of execution
- proof of block

Proof of execution and proof of block are mutually exclusive outcomes for a governed attempt.

---

## 6. Non-Conformant Audit Patterns

The following are non-conformant as sole audit mechanisms:

- generic success/failure logs without attempt binding
- logs that cannot distinguish block reasons
- logs emitted only after effectuation
- logs lacking boundary or action binding

---

## 7. Minimal Conformance Condition

A system is conformant with the UAA audit model only if audit records are sufficient to reconstruct whether a governed attempt executed or was blocked and why.
