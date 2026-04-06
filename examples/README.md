# UAA Examples

This directory contains the executable example for the UAA reference surface.

## File

- `demo.py`  
  Minimal deterministic execution example

## What the example does

The example runs two attempts:

1. An admissible action
2. An inadmissible action

For each attempt, the program performs the UAA sequence:

1. Canonicalize the action
2. Evaluate admissibility against boundary state
3. Issue authorization artifact only if admissible
4. Verify artifact at the control point
5. Execute or block

## Expected outcome

### Admissible action
The system should:

- mark the action admissible
- issue an authorization artifact
- verify the artifact
- execute the action
- emit a proof-of-execution style record

### Inadmissible action
The system should:

- mark the action inadmissible
- issue no valid authorization artifact
- block execution
- emit a proof-of-block style record

## Why this matters

The example is intentionally small.

Its purpose is not scale.
Its purpose is clarity.

It shows the governing distinction at the center of UAA:

Capability to propose an action is not authority to execute it.
