# Unified Agency Architecture (UAA)

Unified Agency Architecture (UAA) is a governance architecture for deterministic execution control.

Its governing principle is:

> Execution authority does not exist by default.

UAA separates capability from authority.

A system may be capable of proposing, constructing, or transmitting an action without possessing the authority to effectuate it.

Execution authority is derived only when a proposed action is:

1. Canonicalized
2. Evaluated for admissibility against an active boundary state
3. Bound to a specific execution attempt
4. Authorized through a verifiable artifact
5. Re-verified at the required control point immediately before execution

If admissibility is not established, if verification fails, or if authorization is absent, execution does not occur.

This is fail-closed by design.

## What this repository shows

This repository provides a minimal UAA reference surface.

It is not a generic demo repository.
It is a structured enforcement surface that demonstrates the category claim in executable form.

The repository is organized around three functions:

- `README.md`  
  Category definition and governing claims

- `reference-surface/`  
  Minimal formal reference surface for UAA enforcement logic

- `examples/`  
  Executable example showing canonicalization, admissibility evaluation, authorization artifact issuance, control-point verification, and deterministic execution or block

## Governing architectural claims

The reference surface demonstrates the following core properties:

- **Non-default authority**  
  Authority is never assumed from capability

- **Admissibility precedes authority**  
  Boundary evaluation comes before authorization

- **Artifact-required execution**  
  Execution requires a valid authorization artifact

- **Control-point verification**  
  Authorization must be re-verified at the execution boundary

- **Fail-closed execution**  
  Missing or invalid authority results in no effect

- **Attempt binding**  
  Authorization is scoped to a specific execution attempt

- **Deterministic auditability**  
  The decision path is reconstructible from the execution record

## Minimal repository structure

.
├── README.md
├── reference-surface/
│   └── README.md
└── examples/
    ├── README.md
    └── demo.py

## Interpretation

This repository should be read as a minimal category-defining reference surface for UAA.

It is intended to communicate one point clearly:

A system that can act is not, by that fact alone, authorized to act.

Under UAA, effectuation requires independently derived execution authority at the moment of execution.
