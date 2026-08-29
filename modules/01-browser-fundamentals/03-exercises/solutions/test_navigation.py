from playwright.sync_api import Page, expect


def test_navigation_and_page_model(page: Page):
    page.goto("data:text/html,<title>Orders</title><h1>Orders portal</h1>")
    expect(page).to_have_title("Orders")
    expect(page.get_by_role("heading", name="Orders portal")).to_be_visible()
