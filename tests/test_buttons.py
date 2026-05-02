from playwright.sync_api import Page, expect

URL = "https://kitchen.applitools.com/"
BUTTONS = [
    "Alert",
    "API",
    "Canvas",
    "Cookie",
    "Drag & Drop",
    "File Picker",
    "iFrame",
    "Links",
    "Notification",
    "Select",
    "Table",
]


def test_kitchen_buttons_present_and_visible(page: Page):
    """Verify main buttons/links on The Kitchen are present and visible."""
    page.goto(URL)
    page.wait_for_load_state("networkidle")

    for name in BUTTONS:
        locator = page.get_by_role("link", name=name)
        expect(locator).to_be_visible(timeout=5000)

    # save a verification screenshot
    page.screenshot(path="kitchen-buttons-verified.png", full_page=True)
