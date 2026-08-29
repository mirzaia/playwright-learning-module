from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    # This explicit lifecycle is useful for learning. Pytest-playwright wraps
    # the same responsibilities in fixtures in the later modules.
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://demo.playwright.dev/todomvc/")
    print(page.title())
    browser.close()
