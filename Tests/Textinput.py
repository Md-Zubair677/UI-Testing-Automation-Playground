from playwright.sync_api import Page, expect


# Verify that the entered text becomes the button's new label.
def test_text_input(page: Page):
    # Open the page containing the text-input example.
    page.goto("http://uitestingplayground.com/textinput")

    # Enter the label to assign to the button.
    input = page.get_by_label("Set New Button Name")
    input.fill("great stuff")

    # Apply the entered label by clicking the button.
    btn = page.locator("button.btn-primary")
    btn.click()

    # Confirm the button now displays the text that was entered.
    expect(btn).to_have_text("great stuff")