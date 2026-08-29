# Concepts: Complex Workflows

## Frames

An iframe has its own document. `page.frame_locator("iframe").get_by_role(...)` scopes a locator to that document; a page locator cannot see inside it. Prefer a frame locator over manually searching frames by URL when the iframe element is stable.

## Popups and tabs

```python
with page.expect_popup() as popup_info:
    page.get_by_role("link", name="Open report").click()
report = popup_info.value
report.wait_for_load_state()
```

The context owns both pages. Capture the event while causing the action, then assert on the returned page.

## Dialogs and permissions

Register `page.once("dialog", handler)` before clicking the button that opens an alert/confirm. Permissions such as geolocation belong in `browser.new_context(permissions=[...], geolocation={...})`, because the context defines the browser identity.

## Controlling time

Modern Playwright can install a controllable clock. Freeze or advance time only for tests whose behavior depends on timers; do not use it to make a slow application appear fast.
