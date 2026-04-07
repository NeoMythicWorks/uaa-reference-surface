# Unified Agency Architecture (UAA)

## Execution authority does not exist by default.

Unified Agency Architecture (UAA) defines an execution-governance model in which:

- Capability is not authority
- Authority does not exist by default
- Authority must be derived at runtime and verified at execution

---

## Definition

Unified Agency Architecture (UAA) is an execution-governance architecture in which execution authority is derived at runtime from admissibility under an active governing boundary.

It separates action generation from execution permission and requires that every path to effectuation pass through a control point where authorization is verified immediately before execution.

---

## Core Principle

> Execution authority does not exist by default.

Systems may generate actions, recommendations, or candidate operations, but no action is permitted to execute unless it is admissible under the active governing boundary and authorized for that specific execution attempt.

---

## Foundational Invariants

1. **Non-Default Authority**  
   No execution is permitted without explicit authorization.

2. **Admissibility Precedes Authority**  
   All actions must be evaluated against a governing boundary before execution authority can exist.

3. **Fail-Closed Execution**  
   If evaluation, artifact issuance, or verification fails, the system produces no effect.

4. **Artifact-Required Execution**  
   Execution requires a valid authorization artifact bound to the specific attempt.

5. **Control Point Verification**  
   Authorization is verified at the execution boundary, not assumed from upstream approval.

6. **No Effect on Block**  
   Rejected or unverifiable actions produce zero side effects.

7. **Monotone Boundary**  
   Constraints may tighten automatically but cannot relax without explicit override.

8. **Measurement Is Not Authority**  
   Metrics, telemetry, and scores may inform constraint state but never grant execution permission.

---

## Execution Sequence

All execution attempts follow this sequence:

`request -> canonicalization -> boundary evaluation -> admissibility decision -> authorization artifact issuance -> control point verification -> execution or block`

Execution is not valid unless this sequence completes successfully at the required enforcement point.

---

## Architectural Separation

UAA separates:

- **Capability**: what a system can generate, propose, or prepare
- **Authority**: what is permitted to execute under the active governing regime

This separation is load-bearing. Capability alone never implies execution permission.

---

## Repository Purpose

This repository provides a minimal reference surface for Unified Agency Architecture (UAA).

It is intended to make the architectural model inspectable and to demonstrate:

- boundary-based admissibility evaluation
- authorization artifact requirement
- verification at the execution boundary
- fail-closed enforcement behavior
- zero-effect blocking semantics

UAA is not a policy suggestion layer, prompt wrapper, or conventional access-control scheme. It defines an execution-governance layer.

---

## Status

Reference Surface v1.0

Formal paper in development for SSRN, Zenodo, and IEEE submission tracks.

---

## Author

Ashley Harris  
Independent Researcher  
Unified Agency Architecture
