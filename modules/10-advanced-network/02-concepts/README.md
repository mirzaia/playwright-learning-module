# Concepts: Network Control

## Observe the causal request

Start waiting before the click: `with page.expect_response("**/api/orders") as info: page.get_by_role("button", name="Refresh").click()`. The response object lets you assert status and JSON. Waiting after the click can miss a fast response.

## Intercept narrowly

`page.route("**/api/orders", handler)` applies a handler to matching requests. `route.continue_()` preserves the real request, `route.fulfill()` supplies deterministic data, and `route.abort()` simulates a blocked dependency. Use a precise pattern and remove or scope the route so it cannot affect another test.

## HAR replay

A HAR is a recorded set of HTTP exchanges. Replay is valuable for a stable third-party dependency or an offline test, but it can become stale. Review the recorded data, avoid secrets, and keep one integration test that uses the real service.

## WebSockets and service workers

Playwright can inspect WebSocket creation and frames. Native routing may not see requests served by a service worker; configure `service_workers="block"` when network interception must be authoritative.
