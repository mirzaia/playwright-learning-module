from playwright.sync_api import Page, expect


def test_orders_are_filtered_by_status(page: Page, demo_url: str):
    page.goto(f"{demo_url}/login")
    page.get_by_label("Email").fill("learner@example.test")
    page.get_by_label("Password").fill("playwright-demo")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_label("Status").select_option("shipped")
    expect(page.get_by_test_id("order-row")).to_have_count(1)
    expect(page.get_by_text("ORD-1003")).to_be_visible()
