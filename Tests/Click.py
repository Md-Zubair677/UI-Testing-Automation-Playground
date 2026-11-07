from playwright.sync_api import Page, expect

def test_click(page: Page):
    # Open the UI Testing Playground homepage.
    page.goto("http://www.uitestingplayground.com/click")

    # Scroll down so the Click section is visible on the page.
    page.mouse.wheel(0, 150)

    # Locate the button that needs to be clicked.
    btn = page.get_by_role("button", name="Button That Ignores DOM Click Event")

    # Click the button.
    btn.click()


    # Confirm the button is visible and that the browser reached the expected URL.
    expect(btn).to_have_class("btn btn-success")
