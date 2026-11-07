from playwright.sync_api import Page, expect

# This test verifies the page that contains a button selected by its CSS class.
def test_class_attribute(page: Page):

    # Open the Class Attribute page from the UI Testing Playground.
    page.goto("http://www.uitestingplayground.com/classattr")

    # Locate the button using its class selector: button.btn-primary
    btn = page.locator("button.btn-primary")

    # Ensure the button is visible before interacting with it.
    expect(btn).to_be_visible()

    # Register a listener so that when the alert appears, it is automatically accepted.
    page.once("dialog", lambda dialog: dialog.accept())

    # Click the button to trigger the alert.
    btn.click()

# Run this test with:
# pytest class_attribute.py -s -v --headed --slowmo 500 --disable-warnings
