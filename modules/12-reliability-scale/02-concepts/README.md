# Concepts: Reliability and Scale

## A reliable test has boundaries

It owns its context, data, temporary files, and assertions. It does not depend on order, wall-clock timing, an unbounded external site, or another test's login. Parallel workers expose hidden dependencies; they do not create them.

## Retries are not a fix

A retry can separate a transient infrastructure failure from a deterministic product failure, but a test that passes only on retry is still unhealthy. Record the first failure, keep the trace, and fix the cause. Do not use retries to make a red suite look green.

## Evidence-driven triage

For a failure, preserve the command, browser, worker, URL, screenshot, trace, console errors, and network response. Compare repeated failures by category: locator ambiguity, environment outage, product defect, or test-state contamination.

## Scaling commands

Use `pytest -m smoke` for a quick gate, `pytest -n auto` for independent tests, and explicit `--browser` runs for engine coverage. Keep browser matrices and broad regression suites separate from the fast feedback path.
