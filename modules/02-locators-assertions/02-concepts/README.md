# Concepts

This module explains resilient locators, web-first assertions, auto-waiting, and safe extraction..

## Finding elements

```python
page.get_by_role("button", name="Save")
page.get_by_label("Email")
page.get_by_text("Order complete")
page.get_by_test_id("order-row")
```

The first three describe the interface as a user or assistive technology sees it. A test id is an explicit contract between the application and its tests. CSS is a fallback for cases where no meaningful user-facing contract exists. A locator can match zero, one, or many elements; actions usually require exactly one, while collection methods intentionally handle many.

## Actions and assertions

```python
page.get_by_label("Email").fill("learner@example.test")
page.get_by_role("button", name="Save").click()
expect(page.get_by_role("status")).to_have_text("Saved")
```

`fill` and `click` wait for an element to be usable. `expect` retries the observation. A timeout means Playwright never saw the expected state; inspect the locator, URL, response, and page screenshot before increasing the timeout.

## Extraction

`locator.all_text_contents()` returns current visible text as Python strings. Use extraction only when the purpose is to inspect data; for a user workflow, prefer an assertion that describes the expected behavior. Never use extraction to bypass access controls or a site's usage rules.
