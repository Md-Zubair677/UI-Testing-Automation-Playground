from playwright.sync_api import Page, expect

# This test checks a page where a button appears only after a short delay.
def test_load_delay(page: Page):
    # Open the UI Testing Playground homepage.
    page.goto("http://www.uitestingplayground.com/")

    # Scroll down to bring the page section into view.
    page.mouse.wheel(0, 150)

    # Find and click the "Load Delay" link in the main navigation.
    loadbtn = page.get_by_role("link", name="Load Delay")
    loadbtn.click()

    # Locate the button that appears after a delay.
    btn = page.get_by_role("button", name="Button Appearing After Delay")

    # Click the delayed button after the page has loaded enough for it to appear.
    btn.click()

    # Confirm the button is visible and that the browser reached the expected URL.
    expect(btn).to_be_visible()
    expect(page).to_have_url("http://www.uitestingplayground.com/loaddelay")
