import time
from playwright.sync_api import sync_playwright, expect


def test_practice_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto('https://demoqa.com/radio-button')

            radio_btn_yes = page.locator('label[for="yesRadio"]')
            expect(radio_btn_yes).to_be_enabled()
            radio_btn_yes.click()
            expect(page.locator('#yesRadio')).to_be_checked()

            expect(page.get_by_text('You have selected Yes')).to_be_visible()


            time.sleep(3)

            radio_btn_impressive = page.locator('label[for="impressiveRadio"]')
            expect(radio_btn_impressive).to_be_enabled()
            radio_btn_impressive.click()
            expect(page.locator('#impressiveRadio')).to_be_checked()

            expect(page.get_by_text('You have selected Impressive')).to_be_visible()

            time.sleep(3)

            expect(page.locator('#noRadio')).to_be_disabled()
            expect(page.locator('#noRadio')).not_to_be_checked()


            radio_btn_no = page.get_by_text('No')
            expect(radio_btn_no).to_be_disabled()


        finally:
            page.close()
            context.close()
            browser.close()
