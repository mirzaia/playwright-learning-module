from pytest_bdd import given, then, when
from pytest_bdd.parsers import parse
from playwright.sync_api import Page, expect


def sign_in(page: Page, demo_url: str):
    page.goto(f"{demo_url}/login")
    page.get_by_label("Email").fill("learner@example.test")
    page.get_by_label("Password").fill("playwright-demo")
    page.get_by_role("button", name="Sign in").click()


@given("I am signed in to the orders page")
def signed_in(page: Page, demo_url: str):
    sign_in(page, demo_url)


@when(parse('I filter orders by "{status}"'))
def filter_orders(page: Page, status: str):
    page.get_by_label("Status").select_option(status)


@then(parse('I see exactly one order with status "{status}"'))
def one_order(page: Page, status: str):
    expect(page.get_by_test_id("order-row")).to_have_count(1)
    expect(page.get_by_role("cell", name=status)).to_be_visible()


@then("I see an empty orders message")
def no_orders(page: Page):
    expect(page.get_by_text("No orders found")).to_be_visible()
