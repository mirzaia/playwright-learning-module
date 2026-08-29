from playwright.sync_api import expect


def test_frame_locator(page):
    page.set_content('<iframe srcdoc="<button>Pay</button>"></iframe>')
    expect(page.frame_locator("iframe").get_by_role("button", name="Pay")).to_be_visible()


def test_popup_event(page):
    page.set_content('<button onclick="window.open(\'about:blank\')">Open report</button>')
    with page.expect_popup() as popup_info:
        page.get_by_role("button", name="Open report").click()
    popup = popup_info.value
    popup.set_content("<h1>Report</h1>")
    expect(popup.get_by_role("heading", name="Report")).to_be_visible()
