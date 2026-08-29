# Concepts

This module explains aaa, fixtures, parametrization, markers, traces, screenshots, and debugging..

## How pytest runs a test

```python
def test_order_is_visible(page, demo_url):
    # Arrange: establish the page state
    page.goto(f"{demo_url}/orders")
    # Act: perform one user action
    page.get_by_label("Status").select_option("paid")
    # Assert: verify the observable result
    expect(page.get_by_test_id("order-row")).to_have_count(1)
```

pytest finds the function because its name starts with `test_`. It sees `page` and `demo_url` as fixture names and asks pytest to provide them. The test should not construct a global page or depend on another test having run first.

## Reading a failure

Start with the bottom assertion message, then find the first frame pointing to your test file. “Locator resolved to 2 elements” means the selector is ambiguous; “waiting for locator” means the expected element never reached the required state; a URL mismatch usually means the preceding action navigated somewhere unexpected. Fix the cause before adding a timeout.

## Debug artifacts

Use `--headed` to see the browser, `PWDEBUG=1` to open the inspector, and `page.pause()` to stop at a chosen line. A screenshot captures one moment; a video captures the run; a trace records actions, DOM snapshots, and network details so a failure can be inspected after the browser closes.
