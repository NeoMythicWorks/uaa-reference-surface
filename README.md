# UAA Reference Surface

Execution authority does not exist by default.

This repository demonstrates:

- No action executes without per-attempt authorization
- Authorization is verified at execution
- Invalid or replayed authorization = zero execution effect

Run demo:

python .\examples\demo.py

Run full validation:

python .\examples\test_demo.py

## Expected Validation Output

When running:

python .\examples\test_demo.py

You should see:

[PASS] no artifact - no authorization artifact
[PASS] invalid artifact - invalid authorization artifact
[PASS] valid execution - action permitted
[PASS] replay - replay detected
[PASS] boundary mismatch - boundary mismatch

ALL TESTS PASSED

If any line differs, enforcement is not functioning as defined.
