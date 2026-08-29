# Concepts

This module explains browser/context/page lifecycle, navigation, and a standalone sync script..

## The browser model

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
```

`sync_playwright()` starts the Playwright driver and guarantees cleanup when the block exits. `launch()` starts a browser process. `new_context()` creates isolated cookies, permissions, and storage. `new_page()` creates a tab. `goto()` navigates that tab and waits for the navigation to reach its normal completion point. In a real test, use the pytest `page` fixture so pytest-playwright creates and closes the browser objects.

## Headed and headless mode

Headless mode has no visible window and is faster for repeated checks. Headed mode is the same browser with a visible window, useful when learning or debugging. Switch with `uv run pytest --headed`; this changes presentation, not the test's assertions.

## Navigation is an observable action

`page.goto(url)` is the action. `expect(page).to_have_url(url)` or `expect(page).to_have_title(title)` is the observation. Keeping those separate makes a failure explainable: you can tell whether navigation failed or the page content was wrong.

Use Playwright's user-facing locators and web-first assertions. Prefer `get_by_role`, `get_by_label`, and `expect(...)`; avoid sleeps and long CSS/XPath chains. Read the annotated examples in this directory before editing the starter.
