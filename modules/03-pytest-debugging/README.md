# Module 03: pytest and Debugging

Use Playwright with pytest fixtures, Arrange–Act–Assert, parametrization, markers, traces, screenshots, videos, and the inspector.

Read Objectives, Concepts, Exercises, then Verification in order.
This module connects Playwright to pytest. pytest discovers functions whose names begin with `test_`, injects fixtures by parameter name, and reports assertion failures with the source line and values involved. A fixture is setup/teardown code with a name; it is not a global variable.

The debugging sequence is deliberate: reproduce one test, run it headed if visibility helps, pause at the failing action, inspect the locator, then use a screenshot or trace to understand what the browser saw. A trace is a timeline containing actions, DOM snapshots, and network information—not merely a screenshot.
