# Module 02: Locators and Assertions

Practice resilient user-facing locators, web-first assertions, auto-waiting, and bounded read-only extraction.

An HTML page is a tree of elements. A locator is not the element itself; it is a recipe that Playwright reevaluates when an action or assertion runs. This matters because modern pages re-render elements after clicks and network responses. Prefer the way a user perceives the page—role, label, visible text—before implementation details such as CSS classes.

Assertions are observations, not just Python comparisons. `expect(locator).to_be_visible()` retries until the element is visible or the timeout expires, which handles normal rendering delay. This is why `time.sleep()` is discouraged: sleeping waits a fixed amount without checking whether the page is ready.

Read Objectives, Concepts, Exercises, then Verification in order.
