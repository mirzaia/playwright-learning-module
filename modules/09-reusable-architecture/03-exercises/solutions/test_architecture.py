from dataclasses import dataclass
from playwright.sync_api import Page, expect


@dataclass(frozen=True)
class Order:
    order_id: str
    status: str


class OrdersPage:
    def __init__(self, page: Page, base_url: str):
        self.page, self.base_url = page, base_url

    def open_authenticated(self):
        self.page.goto(f"{self.base_url}/login")
        self.page.get_by_label("Email").fill("learner@example.test")
        self.page.get_by_label("Password").fill("playwright-demo")
        self.page.get_by_role("button", name="Sign in").click()

    def filter_by_status(self, status: str):
        self.page.get_by_label("Status").select_option(status)


def test_page_object_expresses_business_intent(page, demo_url):
    orders = OrdersPage(page, demo_url)
    orders.open_authenticated()
    orders.filter_by_status("paid")
    expect(page.get_by_test_id("order-row")).to_have_count(1)
