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
