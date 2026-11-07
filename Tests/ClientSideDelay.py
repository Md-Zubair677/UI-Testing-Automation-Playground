from playwright.sync_api import Page, expect

# Verify that client-side processing eventually displays its completion message.
def test_client_side_delay(page: Page):

    # Open the page that runs delayed client-side logic.
    page.goto("http://www.uitestingplayground.com/clientdelay")

    # Locate the button
    btn = page.get_by_role("button", name="Button Triggering Client Side Logic")

    # Click the button
    btn.click()
    page.wait_for_timeout(15000)  # Wait for the client-side logic to complete
    # Locate the success message
    message = page.get_by_text("Data calculated on the client side.")

    # Verify the message
    expect(message).to_be_visible()