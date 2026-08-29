# Concepts

This module explains apirequestcontext, route mocking, mobile emulation, browsers, and parallelism..

## Three useful layers

`page.request.get(...)` exercises an HTTP endpoint without rendering a page. `page.expect_response(...)` observes the request made by a UI action. `page.route(...)` intercepts a request and can fulfill it with controlled data. Direct API checks are fast; UI checks prove that a user can reach and understand the result; mocks let you test rare server failures without waiting for a real outage.

## Browsers and devices

`--browser chromium`, `--browser firefox`, and `--browser webkit` run the same test against different rendering engines. A device profile changes viewport, user agent, and touch settings together. It is a realistic emulation profile, not proof that every physical phone behaves identically.

## Parallel execution

`pytest -n auto` starts worker processes. A test is parallel-safe when it owns its browser context and data, does not depend on ordering, and does not write to a shared filename. Function-scoped `page` fixtures and unique temporary paths provide that isolation.
