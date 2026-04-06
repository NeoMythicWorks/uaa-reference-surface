# Unified Agency Architecture (UAA)

Unified Agency Architecture (UAA) defines an execution model in which:

> Execution authority does not exist by default.

UAA separates:

- Capability - the ability to generate an action
- Authority - the permission for that action to execute

Authority is derived only at runtime through admissibility evaluation and must be verified at the execution boundary immediately before effectuation.

---

## Why UAA Exists

Most systems treat the ability to act as if it already carries permission to execute.

UAA rejects that model.

It defines an execution architecture where:

- authority is non-default
- admissibility precedes execution
- execution requires a per-attempt authorization artifact
- verification occurs at a mandatory control point
- failure resolves to block with no governed effect

---

## Core Execution Sequence

canonicalize -> admissibility -> authorization -> control point verification -> execution / block

This sequence is the minimum governed path for UAA-conformant execution.

No execution path may bypass control-point verification.

---

## What This Repository Contains

- core/ - foundational invariants
- ormal/ - execution semantics, artifact model, conformance mapping, verification
- oundary/ - boundary definition
- udit/ - audit model and example records
- examples/reference_surface/ - runnable reference surface

---

## What the Reference Surface Proves

Run:

python examples/reference_surface/run_demo.py

The reference surface demonstrates:

- valid execution under verified authority
- replay rejection
- no-token blocking
- boundary mismatch blocking
- direct bypass blocking

This is not a production system. It is a minimal enforcement surface proving the UAA model can be instantiated and verified.

---

## Formal Layers

The architecture is defined across five linked layers:

1. Invariants  
   Non-default authority, fail-closed execution, replay resistance, no effect on block

2. Execution Semantics  
   Normative sequence from proposal to execution or block

3. Authorization Artifact Model  
   Per-attempt, bound, non-replayable, time-bounded authority object

4. Boundary Model  
   Active constraint state under which admissibility is evaluated

5. Audit Model  
   Minimum evidence required to reconstruct execution vs. block outcomes

These layers are linked through ormal/conformance-mapping.md.

---

## How to Verify UAA

1. python -m compileall .
2. python examples/reference_surface/run_demo.py

Expected visible outcomes include:

- EXECUTED
- BLOCKED: replay detected
- BLOCKED: no token
- BLOCKED: control point not invoked

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

## Current Status

- Category defined
- Formal layer established
- Runnable reference surface implemented
- Conformance mapping established

---

## Author

Ashley Harris  
Independent Researcher  
Unified Agency Architecture
