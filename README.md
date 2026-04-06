# Unified Agency Architecture (UAA)

Unified Agency Architecture (UAA) defines an execution model where:

> Execution authority does not exist by default.

UAA separates:
- **Capability** — the ability to generate an action  
- **Authority** — the permission for that action to execute  

Authority is not implicit. It is derived at runtime through admissibility evaluation and enforced at the execution boundary.

---

## Core Execution Model

All execution must follow:

canonicalize → admissibility → authorization → control point verification → execution / block

If no valid authorization artifact is present at the control point, execution cannot occur.

If verification fails at the control point, execution is denied and no side effects occur.

All execution authority is validated at the control point immediately prior to execution.

No execution path may bypass control point verification.

---

## Foundational Invariants

- Non-default authority  
- Admissibility precedes authority  
- Fail-closed execution  
- Artifact-required execution  
- Control-point verification  
- No effect on block  
- Replay resistance  
- Measurement is not authority  

These invariants define UAA as a deterministic execution authority architecture.

---

## Repository Structure

core/  
formal/  
governance/  
enforcement/  
audit/  
boundary/  
examples/  
  reference_surface/  

- `/core` — execution semantics and invariant definitions  
- `/formal` — formal models, artifact structure, and system definitions  
- `/governance` — boundary state and override logic  
- `/enforcement` — control point and execution enforcement logic  
- `/audit` — verification, logging, and evidence structures  
- `/boundary` — admissibility state definitions  
- `/examples` — runnable reference implementations  

---

## Reference Surface

A minimal executable reference is provided at:

`examples/reference_surface/`

Run:

`python examples/reference_surface/run_demo.py`

This demonstrates:

- admissible execution  
- blocked execution  
- replay rejection  
- deterministic enforcement at the execution boundary  

---

## Category Definition

UAA is not:

- access control  
- policy enforcement  
- monitoring  
- post-hoc auditing  

UAA is:

> An execution authority architecture in which admissibility is evaluated externally and enforced at the point of execution.

---

## Enforcement Model

- Authorization is **per-attempt**, not persistent  
- Authorization artifacts are **non-replayable**  
- Enforcement occurs at **mandatory control points**  
- All execution paths must pass through verification  
- No execution path may bypass enforcement  
- Failure to verify results in **no execution and no effect**  

---

## Scope

This repository defines:

- the execution model  
- the governing invariants  
- the enforcement structure  
- a minimal reference surface  

This is not a production system.

Production implementations extend this with:

- cryptographic signing  
- distributed control planes  
- system-level enforcement integration  
- persistent audit chains  

---

## Status

Category defined  
Reference surface implemented  
Formal specification in progress  

---

## Author

Ashley Harris  
Independent Researcher  
Unified Agency Architecture