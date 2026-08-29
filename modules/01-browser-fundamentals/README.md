# Module 01: Browser Fundamentals

Learn browser, context, and page lifecycle, navigation, and a standalone synchronous Playwright script before using the pytest page fixture.

The central model is Browser → BrowserContext → Page. A browser is expensive to start, a context isolates cookies and storage, and a page is the tab where navigation and interaction occur. Tests normally receive a clean page fixture so one test cannot accidentally reuse another test's login or local-storage state.

The module first shows the lower-level `sync_playwright()` lifecycle so you can see where resources are created and closed. It then uses pytest-playwright, which manages that lifecycle for you. “Managed for you” does not mean “invisible”: understanding the lifecycle is how you diagnose closed-page and leaked-browser errors.

Read Objectives, Concepts, Exercises, then Verification in order.
