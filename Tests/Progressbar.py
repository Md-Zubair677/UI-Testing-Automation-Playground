from playwright.sync_api import Page


def test_progressbar(page: Page):
    page.goto("http://uitestingplayground.com/progressbar")

    progressbar = page.get_by_role("progressbar")

    start_btn = page.get_by_role("button", name="Start")
    stop_btn = page.get_by_role("button", name="Stop")

    # start progress
    start_btn.click()

    # check progress
    while True:
        valuenow = int(progressbar.get_attribute("aria-valuenow"))
        print(f"Percent: {valuenow}%")

        # Stop once the progress reaches or exceeds 30.
        if valuenow >= 30:
            break

    # stop progress
    stop_btn.click()

    assert valuenow >= 30