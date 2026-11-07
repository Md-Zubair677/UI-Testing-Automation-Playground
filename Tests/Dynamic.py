from playwright.sync_api import sync_playwright, expect

# Start the Playwright browser session and keep it open for the full test flow.
with sync_playwright() as playwright:

    # Launch a Chromium browser in headed mode with a short delay between actions.
    browser = playwright.chromium.launch(headless=False, slow_mo=5000)

    # Open a new browser tab and navigate to the UI Testing Playground home page.
    page = browser.new_page()
    page.goto("http://www.uitestingplayground.com/")

    # Scroll the page slightly so the target link is visible on screen.
    page.mouse.wheel(0, 500)

    # Find the "Dynamic ID" navigation link and click it.
    btn = page.get_by_role("link", name="Dynamic ID")
    btn.highlight()
    btn.click()

    # Confirm the browser navigated to the expected page.
    expect(page).to_have_url("http://www.uitestingplayground.com/dynamicid")

    # Locate the dynamic button on the new page and interact with it.
    btn2 = page.get_by_role("button", name="Button with Dynamic ID")
    btn2.highlight()
    btn2.click()

    # Check that the clicked button remains visible after interaction.
    expect(btn2).to_be_visible()

    # Close the browser after the test steps are complete.
    browser.close()

