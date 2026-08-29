# Module 10: Advanced Network Control

Use Playwright as an observability and simulation tool, not only as a click driver. You will observe requests and responses, wait for the exact API call caused by a UI action, modify a real response, abort selected resources, and understand when HAR replay is appropriate.

These techniques are useful when an environment is slow, an upstream service is unreliable, or a rare error state is difficult to reproduce. They must not be used to hide product defects: keep at least one test against the real integration path.

