# Boundary Definition

This document defines the minimum boundary model for UAA admissibility.

---

## 1. Purpose

A boundary is the active constraint state against which a canonical action is evaluated.

A boundary determines what is admissible at a given execution moment.

---

## 2. Minimum Boundary Responsibilities

A conformant boundary model must be able to express:

- allowed action classes
- allowed resources
- context-sensitive restrictions
- temporal constraints
- explicit override scope, if any

---

## 3. Minimum Boundary Fields

A minimal boundary representation may include:

- id
- llowed_actions
- llowed_resources
- contextual constraints
- temporal validity metadata

---

## 4. Semantic Role

The boundary is not the action.
The boundary is not the artifact.
The boundary is not execution.

The boundary defines the admissibility envelope under which execution authority may or may not be derived.

---

## 5. Boundary Resolution

Before admissibility is evaluated, the active boundary must be resolved.

If no valid boundary can be resolved, the action is blocked.

---

## 6. Boundary Matching

The authorization artifact must remain bound to the boundary under which it was issued.

If the presented boundary at verification time does not match the bound boundary, execution is blocked.

---

## 7. Override Principle

Any expansion of what is admissible must be explicit, attributable, and scope-bound.

Implicit expansion is non-conformant.

---

## 8. Minimal Conformance Condition

A system is conformant with the UAA boundary model only if admissibility is evaluated against an active, resolved boundary and execution is blocked whenever boundary resolution or boundary binding fails.
