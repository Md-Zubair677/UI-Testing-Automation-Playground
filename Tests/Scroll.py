from playwright.sync_api import Page, expect

def test_scrollbars(page: Page):
    # Open the page containing the button that requires scrolling.
    page.goto("http://www.uitestingplayground.com/scrollbars")
    btn=page.locator("#hidingButton")
    # Bring the button into the viewport before interacting with it.
    btn.scroll_into_view_if_needed()
    btn.click()
    # Confirm the button is visible after the interaction.
    expect(btn).to_be_visible()