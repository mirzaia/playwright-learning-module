# Concepts

This module explains the same workflow using async playwright and await..

## Sync versus async

The synchronous API lets Python pause at `page.goto(...)` until the operation completes. The async API returns awaitable work, so the event loop can schedule other tasks while the browser driver is waiting:

```python
await page.goto("https://example.com")
await expect(page.get_by_role("heading")).to_be_visible()
```

The locator and assertion ideas do not change. The required change is control flow: browser calls and async assertions must be awaited, and an async function must run inside an event loop. Use one style consistently in a test.
