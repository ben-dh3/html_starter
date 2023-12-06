from playwright.sync_api import Page, expect

# Tests for your routes go here

def test_get_goodbye(page, test_web_address):
    page.goto(f"http://{test_web_address}/goodbye")

    strong_tag = page.locator("strong")

    expect(strong_tag).to_have_text("Bye!")

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""


# === End Example Code ===
