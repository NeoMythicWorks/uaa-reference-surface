# UAA Reference Surface

This directory provides a minimal, executable reference surface for Unified Agency Architecture (UAA) enforcement.

It demonstrates the governing principle:

> Execution authority does not exist by default.

All execution attempts are:

1. Canonicalized
2. Evaluated for admissibility against a boundary state
3. Authorized only if admissible
4. Bound to a specific attempt
5. Verified again at the control point before execution

If any required condition fails, the action is blocked and produces no effect.

## Purpose

This reference surface exists to show the enforcement shape of UAA in minimal form.

It is not a policy document alone.
It is not an after-the-fact audit layer.
It is not a monitoring-only architecture.

It represents a control architecture in which execution authority is externally derived and verified before effectuation.

## Minimal enforcement sequence

### 1. Canonicalization
The proposed action is reduced into a stable canonical representation.

### 2. Boundary evaluation
The canonical action is checked against the active boundary state.

### 3. Authorization artifact issuance
If and only if the action is admissible, a short-lived authorization artifact is issued for that attempt.

### 4. Control-point verification
The artifact is verified against the canonical action and attempt identity immediately before execution.

### 5. Execution or block
- Valid artifact and admissible action: execute
- Invalid artifact, mismatch, or inadmissible action: block with no effect

## Architectural meaning

This reference surface demonstrates the difference between:

- generating an action
- being authorized to effectuate an action

That distinction is load-bearing.

Without that distinction, capability drifts into authority by default.
UAA exists to prevent that drift.

## What the example proves

The paired example in `../examples/demo.py` shows:

- deterministic canonicalization
- explicit boundary state
- admissibility decision
- per-attempt authorization artifact
- verification at the control point
- proof of execution for admissible action
- proof of block for inadmissible action

## Result

The enforcement surface shown here is minimal on purpose.

Its function is to make the category claim explicit:

A system does not execute because it can.
It executes only when authority has been actively and verifiably established.
