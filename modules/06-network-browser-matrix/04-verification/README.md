# Verification

Run `pytest --browser chromium -q` from the module directory. A completed module has a passing solution-equivalent test, no unhandled browser resources, and a learner who can explain every assertion and fixture involved.

Checklist:

- [ ] `uv sync` succeeds.
- [ ] Required browser binaries are installed.
- [ ] Starter exercise was attempted before reading the solution.
- [ ] Tests pass without `time.sleep()` or shared mutable page state.
- [ ] Failure output and artifacts can be located and explained.
