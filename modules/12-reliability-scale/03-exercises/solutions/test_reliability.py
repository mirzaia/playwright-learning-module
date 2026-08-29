import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_smoke_has_a_clear_boundary(page):
    page.goto("data:text/html,<h1>Critical path</h1>")
    expect(page.get_by_role("heading", name="Critical path")).to_be_visible()
