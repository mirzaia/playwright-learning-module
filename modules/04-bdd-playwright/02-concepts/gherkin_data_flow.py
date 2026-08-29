"""This file is explanatory; the executable scenario is in features/orders.feature.

Feature text is specification, decorators bind sentences to Python, pytest
injects fixtures, and Playwright performs the browser action/assertion.
"""

FLOW = [
    "Feature sentence: When I filter orders by \"paid\"",
    "Decorator match: @when(parse(...))",
    "Fixture injection: page and status",
    "Browser action: page.get_by_label(\"Status\").select_option(status)",
    "Observation: expect(...).to_have_count(1)",
]

if __name__ == "__main__":
    print("\\n".join(FLOW))
