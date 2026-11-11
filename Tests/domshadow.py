from playwright.sync_api import Page, expect


def test_domshadow(page: Page):
    page.goto("http://www.uitestingplayground.com/shadowdom")

    field = page.locator("#editField")
    expect(field).to_have_value("")  # starts empty, as in your screenshot

    # Click the gear, then the copy icon
    page.locator(".button-generate").click()
    expect(field).not_to_have_value("")
    generated_guid = field.input_value()
    print(f"Generated GUID: {generated_guid}")

    btn = page.locator(".fa.fa-clone").nth(0)
    btn.click()

    #

    expect(field).to_have_value(generated_guid)