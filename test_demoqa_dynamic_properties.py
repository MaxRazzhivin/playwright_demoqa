import time

from playwright.sync_api import sync_playwright, expect


def test_practice_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        try:
            page.goto('https://demoqa.com/dynamic-properties', wait_until='domcontentloaded')

            button = page.locator('#visibleAfter')
            expect(button).not_to_be_visible()

            page.wait_for_selector(selector='#visibleAfter', timeout=7000,
                                   state='visible')




        finally:
            page.close()
            context.close()
            browser.close()
