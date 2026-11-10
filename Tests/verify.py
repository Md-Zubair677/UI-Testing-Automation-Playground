from playwright.sync_api import Page, expect

def test_verify_text(page: Page):
    # Open the page containing the welcome message.
    page.goto("http://www.uitestingplayground.com/verifytext")

    # Match the complete message while ignoring surrounding whitespace.
    welcome_text = page.locator(
        "xpath=//span[normalize-space(.)='Welcome UserName!']"
    )
    welcome_text.highlight()

    # Verify the expected message is visible.
    expect(welcome_text).to_be_visible()