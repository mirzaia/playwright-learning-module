from playwright.sync_api import expect


def test_api_contract(page, demo_url):
    response = page.request.get(f"{demo_url}/api/orders")
    assert response.ok
    assert {"id", "status"} <= set(response.json()[0])


def test_narrow_route_mock(page, demo_url):
    page.route("**/api/orders", lambda route: route.fulfill(json=[]))
    response = page.goto(f"{demo_url}/api/orders")
    assert response is not None and response.json() == []
