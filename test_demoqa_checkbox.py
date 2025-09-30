from playwright.sync_api import sync_playwright, expect


def test_practice_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto('https://demoqa.com/checkbox')

            home = page.locator('label[for="tree-node-home"]')
            desktop = page.locator('label[for="tree-node-desktop"]')
            expect(home).to_be_visible()
            expect(desktop).to_be_hidden()

            home_row = page.locator(".rct-text", has=home)
            home_row.get_by_title('Toggle').click()

            expect(desktop).to_be_visible()


        finally:
            page.close()
            context.close()
            browser.close()
