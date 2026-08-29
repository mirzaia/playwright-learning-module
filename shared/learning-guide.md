# Theory guide for beginners

This short guide gives the mental model used throughout the modules.

## What is being tested?

A browser test checks a user-visible workflow from the browser boundary: the browser sends HTTP requests, the server returns HTML/JSON, JavaScript changes the page, and the user sees controls and messages. A Playwright test drives the same boundary rather than calling private Python functions inside the application.

## Action versus observation

Every useful test has an action and an observation. “Click Save” is an action. “A confirmation message is visible” is an observation. A test with only actions can pass while the application is broken; a test with only an assertion has no meaningful behavior to exercise.

## Why tests become flaky

Flakiness means the same code sometimes passes and sometimes fails without a product change. Common causes are fixed sleeps, ambiguous selectors, shared cookies, test-order dependencies, random data, and asserting before asynchronous rendering finishes. Playwright locators and web-first assertions address timing, while isolated contexts and explicit test data address state.

## What a failure means

- Import or fixture error: Python/pytest setup failed before the browser test began.
- Browser launch error: the Playwright package exists but its browser binary is missing or unusable.
- Navigation error: the URL could not be reached or the server returned an unexpected result.
- Locator timeout: the expected element was not found or not actionable.
- Assertion failure: the test reached the page, but the observed state differed from the requirement.

Always classify the failure before changing code. The category tells you which layer to inspect.
