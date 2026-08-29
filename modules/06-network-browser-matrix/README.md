# Module 06: Network and Browser Matrix

Use APIRequestContext, route mocking, mobile emulation, Chromium/Firefox/WebKit, and safe parallel execution.

This module separates three layers of a web test: the browser UI, the HTTP request behind the UI, and the browser engine rendering the UI. APIRequestContext checks the HTTP layer directly; `page.route()` replaces a response so a rare server failure can be tested deterministically; browser/device options change the rendering environment. These techniques are complementary, not interchangeable.

Read Objectives, Concepts, Exercises, then Verification in order.
