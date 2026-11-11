from playwright.sync_api import Page, expect

def test_nbsp(page: Page):
    page.goto("http://www.uitestingplayground.com/nbsp")
    btn=page.get_by_role("button", name="My Button")
    btn.highlight()

    btn.click()
    expect(btn).to_be_visible()