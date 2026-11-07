from playwright.sync_api import Page, expect

# Verify that the green button on the Hidden Layers page is visible and clickable.
def test_hidd_layer(page: Page):
    # Open the Hidden Layer page from the UI Testing Playground.
    page.goto("http://www.uitestingplayground.com/hiddenlayers")

    # Locate the button that is initially hidden behind another element.
    btn = page.locator("button#greenButton")

    # Ensure the button is visible before interacting with it.
    expect(btn).to_be_visible()

    # Click the button to trigger the alert.
    btn.click()