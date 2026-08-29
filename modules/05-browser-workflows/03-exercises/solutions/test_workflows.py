from pathlib import Path
from playwright.sync_api import Page, expect


def login(page: Page, demo_url: str):
    """Perform UI login once for this test's isolated page context."""
    page.goto(f"{demo_url}/login")
    page.get_by_label("Email").fill("learner@example.test")
    page.get_by_label("Password").fill("playwright-demo")
    page.get_by_role("button", name="Sign in").click()


def test_authenticated_redirect(page: Page, demo_url: str):
    """A signed-out context should be redirected to the login page."""
    page.goto(f"{demo_url}/account")
    expect(page).to_have_url(f"{demo_url}/login")


def test_download_content(page: Page, demo_url: str, tmp_path: Path):
    """Wait for the download event and verify the bytes, not just its name."""
    login(page, demo_url)
    with page.expect_download() as download_info:
        page.get_by_role("link", name="Download orders").click()
    download_info.value.save_as(tmp_path / "orders.csv")
    assert "ORD-1001" in (tmp_path / "orders.csv").read_text()


def test_upload_content(page: Page, demo_url: str, tmp_path: Path):
    login(page, demo_url)
    sample = tmp_path / "receipt.txt"
    sample.write_text("receipt")
    page.get_by_label("Document").set_input_files(sample)
    page.get_by_role("button", name="Upload document").click()
    expect(page.get_by_text("Upload complete")).to_be_visible()
