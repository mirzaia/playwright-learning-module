from playwright.sync_api import Page, expect


def test_user_facing_locators(page: Page):
    page.set_content('<label for="name">Name</label><input id="name"><button>Save</button><p role="status">Saved</p>')
    page.get_by_label("Name").fill("Ada")
    page.get_by_role("button", name="Save").click()
    expect(page.get_by_role("status")).to_have_text("Saved")


def test_bounded_extraction(page: Page):
    page.set_content('<ul><li>ORD-1001</li><li>ORD-1002</li></ul>')
    assert page.locator("li").all_text_contents() == ["ORD-1001", "ORD-1002"]
