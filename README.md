\# UAA Reference Surface



This repository provides a minimal executable proof of \*\*Unified Agency Architecture (UAA)\*\* as an execution-governance control system.



UAA enforces a single governing invariant:



\*\*Execution authority does not exist by default.\*\*



Systems may generate arbitrary actions, but no action is allowed to execute unless authority is explicitly derived at runtime and verified at the control point immediately before execution.



\---



\## What this repository proves



This reference surface demonstrates that execution can be governed externally with:



\- canonical action representation

\- admissibility evaluation against an active boundary

\- authorization artifact issuance per attempt

\- control-point verification immediately before execution

\- replay detection and rejection

\- fail-closed behavior

\- zero execution without valid authority



\---



\## Run the demo



From the repository root:



Expected behavior:



\- valid action → EXECUTED  

\- replayed token → BLOCKED (replay detected)  

\- invalid action → rejected at admissibility  

\- execution without token → BLOCKED  



\---



\## Why this matters



Most systems collapse capability and authority:



If a system can produce an action, it is often allowed to execute it.



UAA separates these concerns:



\- capability → what can be generated  

\- authority → what is allowed to execute  



This repository demonstrates that separation in executable form.



\---



\## Repository role



This is the \*\*reference surface\*\* for UAA.



It is designed to:

\- be runnable

\- be inspectable

\- prove enforcement behavior



It is not a full production system and does not include full infrastructure, cryptographic deployment, or distributed enforcement layers.



\---



\## Structure



\---



\## Core takeaway



Execution is not governed by what a system can do.



Execution is governed by what a system is allowed to do — at the moment of execution.

