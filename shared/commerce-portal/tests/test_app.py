from commerce_portal.app import create_app


def test_login_and_orders_routes():
    client = create_app().test_client()
    assert client.get("/orders").status_code == 302
    response = client.post("/login", data={"email": "learner@example.test", "password": "playwright-demo"})
    assert response.status_code == 302
    assert client.get("/orders").status_code == 200


def test_api_download_and_upload_routes():
    client = create_app().test_client()
    assert len(client.get("/api/orders").json) == 3
    assert client.get("/download/orders.csv").status_code == 200
    response = client.post("/upload", data={"document": (None, "")})
    assert response.status_code == 400
