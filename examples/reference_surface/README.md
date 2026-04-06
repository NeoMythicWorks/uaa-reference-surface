# UAA Reference Surface

This directory provides a minimal, executable reference surface demonstrating enforcement of the Unified Agency Architecture (UAA) execution model.

This is not an example script.  
This is a constrained execution environment that enforces UAA invariants at the execution boundary.

---

## Governing Principle

> Execution authority does not exist by default.

No action executes unless authority is explicitly derived, issued, and verified.

---

## Execution Model

All execution follows the deterministic sequence:

canonicalize ? admissibility ? authorization ? control point verification ? execution / block

Properties enforced:

- Authority is evaluated per attempt
- Authorization artifacts are required for execution
- Verification occurs immediately before execution
- Failure at any stage results in block with no effect

---

## What This Demonstrates

This reference surface proves:

1. **Admissible execution**
   - Valid action + valid token ? EXECUTED

2. **Replay resistance**
   - Token reuse ? BLOCKED: replay detected

3. **Missing authority**
   - No token ? BLOCKED: no token

4. **Admissibility failure**
   - Invalid action ? not authorized

5. **Control point enforcement**
   - Direct execution bypass ? BLOCKED: control point not invoked

6. **Time-bound authority**
   - Expired token ? BLOCKED

---

## System Components

### canonicalize.py
Deterministic action normalization  
Ensures consistent hashing and evaluation

### admissibility.py
Evaluates action against boundary state  
Returns strict boolean admissibility

### authorization.py
Issues per-attempt authorization artifacts  
Includes:
- action hash binding
- boundary binding
- expiration window
- nonce (replay prevention)

### replay_cache.py
Tracks used nonces  
Prevents token reuse

### control_point.py
Mandatory enforcement layer  
Performs final verification immediately before execution

### run_demo.py
End-to-end execution sequence  
Exercises both allow and deny paths

---

## Running the Reference

From repository root:

`ash
python examples/reference_surface/run_demo.py@"
# UAA Reference Surface

This directory provides a minimal, executable reference surface demonstrating enforcement of the Unified Agency Architecture (UAA) execution model.

This is not an example script.
This is a constrained execution environment that enforces UAA invariants at the execution boundary.

---

## Governing Principle

> Execution authority does not exist by default.

No action executes unless authority is explicitly derived, issued, and verified.

---

## Execution Model

All execution follows the deterministic sequence:

canonicalize ? admissibility ? authorization ? control point verification ? execution / block

Properties enforced:

- Authority is evaluated per attempt
- Authorization artifacts are required for execution
- Verification occurs immediately before execution
- Failure at any stage results in block with no effect

---

## What This Demonstrates

This reference surface proves:

1. **Admissible execution**
   - Valid action + valid token ? EXECUTED

2. **Replay resistance**
   - Token reuse ? BLOCKED: replay detected

3. **Missing authority**
   - No token ? BLOCKED: no token

4. **Admissibility failure**
   - Invalid action ? not authorized

5. **Control point enforcement**
   - Direct execution bypass ? BLOCKED: control point not invoked

6. **Time-bound authority**
   - Expired token ? BLOCKED

---

## System Components

### canonicalize.py
Deterministic action normalization  
Ensures consistent hashing and evaluation

### admissibility.py
Evaluates action against boundary state  
Returns strict boolean admissibility

### authorization.py
Issues per-attempt authorization artifacts  
Includes:
- action hash binding
- boundary binding
- expiration window
- nonce (replay prevention)

### replay_cache.py
Tracks used nonces  
Prevents token reuse

### control_point.py
Mandatory enforcement layer  
Performs final verification immediately before execution

### run_demo.py
End-to-end execution sequence  
Exercises both allow and deny paths

---

## Running the Reference

From repository root:

python examples/reference_surface/run_demo.py

---

## Expected Output

The system must produce the following behaviors:

- EXECUTED
- BLOCKED: replay detected
- BLOCKED: no token
- BLOCKED: control point not invoked
- BLOCKED (expired or invalid authority)

Any deviation indicates a violation of execution invariants.

---

## Enforcement Guarantees

This reference surface enforces:

- Non-default authority
- Admissibility precedes authority
- Fail-closed execution
- Artifact-required execution
- Control-point verification
- No effect on block
- Replay resistance

Execution cannot occur outside the control point.

---

## Scope

This is a minimal enforcement surface.

It omits:

- cryptographic signing
- distributed verification
- persistent audit chains

Those belong to full system implementations.

---

## Role in UAA

This directory represents:

> A concrete instantiation of UAA execution semantics at the smallest possible surface.

It exists to demonstrate that:

- authority can be externalized
- execution can be constrained deterministically
- bypass attempts fail structurally, not procedurally

---

## Conformance Relevance

This reference surface is illustrative, not sufficient for full UAA conformance.

A conformant system must:

- enforce all invariants
- implement non-bypassable control points
- provide verifiable audit evidence
- bind authority to canonical action + boundary + attempt
