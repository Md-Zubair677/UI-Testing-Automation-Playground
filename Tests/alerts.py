from playwright.sync_api import Page

def test_alerts(page: Page):
    page.goto("http://www.uitestingplayground.com/alerts")

    # Handle Alert
    
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Alert").click()
    

    # Handle Confirm
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()

    # Handle Prompt with a custom value
    page.once("dialog", lambda dialog: dialog.accept("Hello Playwright"))
    page.get_by_role("button", name="Prompt").click()