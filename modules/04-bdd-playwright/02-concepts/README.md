# Concepts

This module explains gherkin scenarios, step definitions, outlines, and scenario-scoped page state..

## Translating Gherkin to Python

```gherkin
Scenario: Filter paid orders
  Given I am signed in to the orders page
  When I filter orders by "paid"
  Then I see exactly one order with status "paid"
```

Each sentence is matched by a decorator such as `@given(...)`, `@when(...)`, or `@then(...)`. The decorated function is ordinary Python. Fixtures such as `page` are injected by pytest into the step function, which is why a step definition should not create a second browser behind pytest's back.

Scenario Outlines repeat one scenario using the rows in `Examples`. Tags are labels used to select related scenarios. Keep the feature language about behavior; keep CSS selectors and Playwright mechanics in the step implementation.
