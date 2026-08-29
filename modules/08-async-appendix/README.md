# Module 08: Async Playwright Appendix

Translate one completed synchronous test to the async Playwright API using await and the async pytest plugin.

Async Playwright has the same browser model and locator concepts as the synchronous API. The difference is control flow: browser operations return awaitable work, so every operation that talks to the browser must be awaited. Do not mix sync and async Playwright objects in one test. This appendix is a translation exercise, not a second curriculum.

Read Objectives, Concepts, Exercises, then Verification in order.
