# Execution Semantics

This document defines the canonical execution semantics of Unified Agency Architecture (UAA).

These semantics are normative. They define the minimum execution sequence required for UAA-conformant systems.

---

## 1. Governing Statement

Execution authority does not exist by default.

An action may be generated, proposed, selected, or prepared without possessing authority to execute.
Authority is derived only through runtime admissibility evaluation under an active governing boundary and must be verified immediately before execution.

---

## 2. Canonical Execution Sequence

A UAA-governed execution attempt follows this sequence:

1. Action proposal
2. Canonicalization
3. Boundary resolution
4. Admissibility evaluation
5. Authorization artifact issuance
6. Control-point verification
7. Execution or block
8. Audit record generation

No conformant execution path may omit, reorder, or bypass these stages where they are applicable.

---

## 3. State Model

A proposed action transitions through the following states:

- Proposed
- Canonicalized
- Boundary-bound
- Evaluated
- Authorized
- Verified
- Executed or Blocked
- Recorded

The transition from one state to the next is conditional.
No state implies the next.

---

## 4. Stage Definitions

### 4.1 Action Proposal

An action enters the system as a proposed effect.

A proposal may include:
- action type
- target resource
- parameters
- initiating context
- attempt metadata

Proposal alone confers no authority.

### 4.2 Canonicalization

The proposed action must be transformed into a deterministic canonical representation.

Canonicalization exists to ensure:
- stable hashing
- stable evaluation
- stable binding between action and authorization artifact

If canonicalization fails, execution is blocked.

### 4.3 Boundary Resolution

The active governing boundary must be resolved before admissibility can be evaluated.

Boundary resolution defines the constraint state under which the action will be judged.

Boundary may include:
- allowed action classes
- allowed resources
- contextual restrictions
- override scope if present
- temporal validity constraints

If no valid boundary can be resolved, execution is blocked.

### 4.4 Admissibility Evaluation

The canonical action is evaluated against the active boundary.

Admissibility is a runtime determination.
It answers only whether the proposed action is permitted under the current constraint state.

Admissibility does not execute the action.
Admissibility does not itself confer execution effect.

If admissibility is false or indeterminate, execution is blocked.

### 4.5 Authorization Artifact Issuance

If and only if admissibility succeeds, the system may issue an authorization artifact for that specific attempt.

The artifact must be bound to:
- the canonical action
- the active boundary
- the specific attempt
- the validity interval
- anti-replay data

Artifact issuance is necessary but not sufficient for execution.

### 4.6 Control-Point Verification

Immediately prior to execution, the artifact must be verified at a mandatory control point.

Verification must confirm at minimum:
- artifact integrity
- action binding
- boundary binding
- temporal validity
- anti-replay validity
- attempt validity

If verification fails, execution is blocked.

### 4.7 Execution or Block

After verification, the system resolves to one of two outcomes:

- Executed
- Blocked

There is no third conformant outcome.

If blocked, no governed effect may occur.

### 4.8 Audit Record Generation

The system must emit sufficient evidence to reconstruct:
- what was attempted
- under which boundary
- whether admissibility succeeded
- whether an artifact was issued
- whether execution occurred or was blocked
- why the final outcome was reached

---

## 5. Normative Rules

### R1. Non-Default Authority
Capability is not authority.

### R2. Admissibility Before Authority
Authority may be derived only after admissibility evaluation.

### R3. Artifact-Required Execution
Execution requires a valid authorization artifact.

### R4. Immediate Pre-Execution Verification
Authority must be re-verified at the control point immediately before execution.

### R5. Fail-Closed Resolution
Missing data, missing artifact, evaluation failure, replay detection, or verification failure resolve to block.

### R6. No Effect on Block
A blocked action must not produce the governed effect.

### R7. Replay Resistance
Authorization artifacts must not be reusable across attempts.

### R8. Non-Bypassable Enforcement
No governed execution path may bypass the control point.

### R9. Measurement Non-Authority
Measurement may influence boundary evolution but cannot grant authority on its own.

---

## 6. Failure Semantics

The following conditions must resolve to block:

- canonicalization failure
- missing boundary
- inadmissible action
- indeterminate admissibility
- missing artifact
- malformed artifact
- expired artifact
- replayed artifact
- boundary mismatch
- action mismatch
- verification failure
- control point bypass attempt

All such failures are fail-closed.

---

## 7. Minimal Outcome Semantics

A conformant system must be able to distinguish:

- executed under valid authority
- blocked due to missing authority
- blocked due to invalid authority
- blocked due to replay
- blocked due to boundary mismatch
- blocked due to bypass attempt

These outcomes must be audit-reconstructible.

---

## 8. Conformance Condition

A system is conformant with UAA execution semantics only if:

- every governed execution attempt passes through the canonical sequence
- all normative rules are preserved
- no governed effect can occur without valid control-point verification
- blocked attempts produce no governed effect
