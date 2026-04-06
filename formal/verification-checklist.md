
Verification Checklist

This checklist provides a minimal verification path for external reviewers.

Repository-Level Verification
Root README presents UAA as the architecture category
core/foundational-invariants.md exists
formal/execution-semantics.md exists
formal/authorization-artifact-model.md exists
formal/conformance-mapping.md exists
boundary/boundary-definition.md exists
audit/audit-model.md exists
examples/reference_surface/run_demo.py exists
Runtime Verification

Run:

python -m compileall .

Then run:

python examples/reference_surface/run_demo.py

Expected visible behaviors include:

EXECUTED
BLOCKED: replay detected
BLOCKED: no token
BLOCKED: control point not invoked
BLOCKED under invalid or mismatched conditions
Interpretation Rule

UAA should not be evaluated by any single file in isolation.

Verification requires alignment between:

root architecture statement
invariants
formal semantics
artifact model
boundary model
audit model
runnable reference surface
observed deny/allow behavior
