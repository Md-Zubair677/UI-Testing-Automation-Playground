from playwright.sync_api import Page, expect

# Verify that clicking the button updates its styling to indicate success.
def test_click(page: Page):
    # Open the UI Testing Playground homepage.
    page.goto("http://www.uitestingplayground.com/click")

    # Scroll down so the Click section is visible on the page.
    page.mouse.wheel(0, 150)

    # Locate the button that needs to be clicked.
    btn = page.get_by_role("button", name="Button That Ignores DOM Click Event")

    # Click the button.
    btn.click()

    # Confirm the click changed the button to its success class.
    expect(btn).to_have_class("btn btn-success")
