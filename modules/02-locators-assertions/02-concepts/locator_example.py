"""A small locator example with comments explaining each test decision."""
from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.set_content('<label for="email">Email</label><input id="email"><button>Save</button><p role="status">Ready</p>')

    # Labels and roles describe the interface, so they survive many DOM refactors.
    page.get_by_label("Email").fill("junior@example.test")
    page.get_by_role("button", name="Save").click()

    # expect retries while the page changes; a bare is_visible() check does not.
    expect(page.get_by_role("status")).to_have_text("Ready")
    browser.close()
