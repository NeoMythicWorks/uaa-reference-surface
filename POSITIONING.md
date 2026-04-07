# Unified Agency Architecture (UAA)

## Category Definition

Unified Agency Architecture (UAA) defines a system category:

Execution authority architectures.

In UAA-conformant systems:

- Execution authority does not exist by default
- Capability is distinct from authority
- Authority must be derived per-attempt through admissibility
- Execution is permitted only after verification at a mandatory control point

---

## Core Claim

UAA establishes that:

Execution authority must be explicitly derived and verified at the point of execution, not assumed from the ability to act.

---

## What This Repository Proves

This repository provides:

- a formal execution model
- a defined invariant set
- a minimal enforcement surface
- deterministic blocking behavior under invalid conditions

Observed outcomes:

- valid execution under admissible conditions
- replay rejection
- execution denial without authorization artifact
- enforcement failure on bypass attempts

---

## What Is Not Included

This repository does not include:

- production enforcement infrastructure
- distributed control plane implementations
- proprietary execution systems

---

## Position

UAA is not an extension of:

- access control systems
- policy engines
- monitoring frameworks

UAA defines a separate architectural category centered on execution authority.

---

## Author

Ashley Harris  
Independent Researcher  
Unified Agency Architecture
