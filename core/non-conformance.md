# Non-Conformance

## Purpose

This document defines conditions under which a system must not be considered conformant with UAA.

## Core Principle

Execution without valid authorization is non-conformant.

## Conditions

Non-conformance occurs if:

- execution occurs without authorization
- authority exists by default
- authorization is not bound to the action
- control points are bypassable
- enforcement is not external
- blocked actions produce effects
- evaluation is non-deterministic
- admissibility expands silently
- authorization is replayable
- audit chain is incomplete

## Summary

If execution is not strictly governed at the point of effectuation, UAA is not present.
