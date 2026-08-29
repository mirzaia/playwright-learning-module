from playwright.sync_api import Page, expect


def test_api_request(page: Page, demo_url: str):
    """Use the browser's request client to check HTTP data without rendering UI."""
    response = page.request.get(f"{demo_url}/api/orders")
    assert response.ok
    assert response.json()[0]["id"] == "ORD-1001"


def test_mocked_api_error(page: Page, demo_url: str):
    """A route mock makes a rare server response reproducible for every learner."""
    page.route("**/api/orders", lambda route: route.fulfill(status=500, body="error"))
    page.goto(f"{demo_url}/api/orders")
    expect(page).to_have_url(f"{demo_url}/api/orders")
