from playwright.sync_api import Page, expect

# This test verifies that an AJAX request loads data and displays it on the page.
def test_Ajax(page: Page):
    # Open the UI Testing Playground homepage.
    page.goto("http://www.uitestingplayground.com/")

    # Scroll down so the AJAX Data section is visible on the page.
    page.mouse.wheel(0, 150)

    # Find and click the "AJAX Data" link in the navigation menu.
    ajaxbtn = page.get_by_role("link", name="AJAX Data")
    ajaxbtn.click()

    # Target the button that triggers the AJAX request.
    btn = page.get_by_role("button", name="Button Triggering AJAX Request")

    # Click the button to start the asynchronous data request.
    btn.click()

    # Wait for the AJAX response to complete before checking the result.
    page.wait_for_timeout(16000)

    # Locate the text that appears after the AJAX call finishes.
    ajax_content = page.get_by_text("Data loaded with AJAX get request.")

    # Confirm that the loaded AJAX content is visible on the page.
    expect(ajax_content).to_be_visible()
