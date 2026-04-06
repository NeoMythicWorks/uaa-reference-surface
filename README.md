cd C:\\Users\\18177\\OneDrive\\Desktop\\uaa(

echo # UAA Reference Surface

echo.

echo This repository provides a minimal executable proof of \*\*Unified Agency Architecture (UAA)\*\* as an execution-governance control system.

echo.

echo UAA enforces a single governing invariant:

echo.

echo \*\*Execution authority does not exist by default.\*\*

echo.

echo Systems may generate arbitrary actions, but no action is allowed to execute unless authority is explicitly derived at runtime and verified at the control point immediately before execution.

echo.

echo ---

echo.

echo ## What this repository proves

echo.

echo - canonical action representation

echo - admissibility evaluation against an active boundary

echo - authorization artifact issuance per attempt

echo - control-point verification immediately before execution

echo - replay detection and rejection

echo - fail-closed behavior

echo - zero execution without valid authority

echo.

echo ---

echo.

echo ## Run the demo

echo.

echo python examples\\demo.py

echo.

echo Expected behavior:

echo - valid action → EXECUTED

echo - replayed token → BLOCKED

echo - invalid action → rejected

echo - execution without token → BLOCKED

echo.

echo ---

echo.

echo ## Structure

echo.

echo This repository is intentionally minimal and scoped to the execution boundary.

echo.

echo reference-surface/

echo   canonicalize.py

echo   admissibility.py

echo   authorization.py

echo   replay\_cache.py

echo   control\_point.py

echo   run\_demo.py

echo.

echo examples/

echo   README.md

echo   allow-flow.md

echo   boundary-tightening.md

echo   bypass-rejection.md

echo   deny-flow.md

echo   invalid-override.md

echo   replay-rejection.md

echo   valid-override.md

echo.

echo ---

echo.

echo ## Core takeaway

echo.

echo Execution is not governed by what a system can do.

echo Execution is governed by what a system is allowed to do — at the moment of execution.

) > README.md

## Structure

This repository is intentionally minimal and scoped to the execution boundary.

reference-surface/
  canonicalize.py
  admissibility.py
  authorization.py
  replay_cache.py
  control_point.py
  run_demo.py

examples/
  README.md
  allow-flow.md
  boundary-tightening.md
  bypass-rejection.md
  deny-flow.md
  invalid-override.md
  replay-rejection.md
  valid-override.md