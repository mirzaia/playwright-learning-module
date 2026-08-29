# Module 04: pytest-bdd with Playwright

Map Gherkin scenarios to step definitions and isolated Playwright pages. Never use module-global page state.

BDD adds a translation layer. A `Feature` describes a user capability, a `Scenario` describes one example, and each Given/When/Then sentence maps to a Python step function. The step function still uses ordinary pytest fixtures and Playwright assertions. When a scenario fails, inspect the chain in order: feature text → matching decorator → fixture setup → browser action → assertion.

Read Objectives, Concepts, Exercises, then Verification in order.
