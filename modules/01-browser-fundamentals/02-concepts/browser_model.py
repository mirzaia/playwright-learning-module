"""Run with: uv run python 02-concepts/browser_model.py.

This deliberately shows the lifecycle that pytest-playwright normally manages:
Playwright driver -> browser process -> isolated context -> tab/page.
"""
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    # The browser is the engine. Headless means no visible window.
    browser = playwright.chromium.launch(headless=True)
    # A context is a clean profile: cookies and local storage start empty.
    context = browser.new_context()
    # A page is one tab inside that isolated profile.
    page = context.new_page()
    page.goto("data:text/html,<title>Learning</title><h1>First page</h1>")
    print(page.title())
    browser.close()
