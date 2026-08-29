import asyncio
from playwright.async_api import async_playwright, expect


async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("data:text/html,<h1>Async Playwright</h1>")
        await expect(page.get_by_role("heading", name="Async Playwright")).to_be_visible()
        await browser.close()
        print("Async Playwright completed")


if __name__ == "__main__":
    asyncio.run(main())
