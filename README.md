# Unified Agency Architecture (UAA)

## ## Execution Authority Is Not Default

Unified Agency Architecture (UAA) defines an execution model in which:

- Capability != Authority
- Authority does not exist by default
- Authority must be derived at runtime and verified at execution
  

---

## Core Execution Path

```text
canonicalize -> admissibility -> authorization -> control point verification -> execution / block
No execution path may bypass control point verification.

Failure to verify results in block with no effect.

Why This Exists

Most systems implicitly grant execution authority once an action is generated.

UAA rejects that assumption.

It enforces:

non-default authority
admissibility before execution
per-attempt authorization
mandatory control point verification
fail-closed outcomes
Repository Structure
core/        - invariants
formal/      - execution semantics, artifact model, verification
boundary/    - admissibility state
audit/       - evidence and logging model
examples/    - runnable enforcement surface
Reference Surface (Proof)

Run:

python examples/reference_surface/run_demo.py

Demonstrates:

EXECUTED (valid authority)
BLOCKED: replay detected
BLOCKED: no token
BLOCKED: control point not invoked
BLOCKED: boundary mismatch
Formal Architecture

UAA is defined across:

Invariants
Execution Semantics
Authorization Artifact Model
Boundary Model
Audit Model

Linked via:

formal/conformance-mapping.md

Verification
python -m compileall .
python examples/reference_surface/run_demo.py
Category Definition

UAA is not:

access control
policy engines
monitoring systems

UAA is:

An execution authority architecture enforcing admissibility at the point of execution.

Status
Category defined
Formal layer established
Enforcement surface operational
Conformance mapping complete
Scope Boundary

This repository contains:

architectural definition
formal structure
minimal enforcement surface

This repository does NOT contain:

production enforcement systems
deployment configurations
proprietary execution infrastructure
Author

Ashley Harris
Independent Researcher
Unified Agency Architecture




