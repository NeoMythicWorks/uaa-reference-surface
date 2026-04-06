\# UAA Reference Surface



This directory provides a minimal, executable reference surface for Unified Agency Architecture (UAA) enforcement.



It demonstrates the governing principle:



> Execution authority does not exist by default.



All execution attempts are:

1\. Canonicalized

2\. Evaluated for admissibility against a boundary state

3\. Authorized via a per-attempt artifact (if admissible)

4\. Verified immediately before execution at a control point

5\. Either executed (with proof) or blocked (with no effect)



\---



\## Enforcement Flow



canonicalize → admissibility → authorization → control point verification → execution / block



This flow enforces the following invariants:



\- Non-default authority

\- Admissibility precedes authority

\- Fail-closed execution

\- Artifact-required execution

\- Control-point verification

\- No effect on block

\- Replay resistance



\---



\## Files



\- `canonicalize.py`  

&#x20; Deterministic canonical action representation



\- `admissibility.py`  

&#x20; Boundary evaluation (admissible / non-admissible)



\- `authorization.py`  

&#x20; Authorization artifact issuance (per attempt)



\- `replay\_cache.py`  

&#x20; Replay detection and prevention



\- `control\_point.py`  

&#x20; Final verification immediately before execution



\- `run\_demo.py`  

&#x20; End-to-end demonstration of allow + block behavior



\---



\## Running the Reference



From this directory:



