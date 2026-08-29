from playwright.sync_api import Page, expect


def test_playwright_is_ready(page: Page):
    page.goto("data:text/html,<title>Ready</title><h1>Playwright ready</h1>")
    expect(page).to_have_title("Ready")
    expect(page.get_by_role("heading", name="Playwright ready")).to_be_visible()
