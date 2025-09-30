from random import randint

from playwright.sync_api import sync_playwright, expect


def test_web_tables_demoqa():
    with sync_playwright() as p:
        chromium_browser = p.chromium.launch(headless=False)

        context = chromium_browser.new_context()
        page = context.new_page()

        page.goto('https://demoqa.com/webtables')

        page.locator('button#addNewRecordButton').filter(has_text='Add').click()
        # page.locator('#addNewRecordButton').get_by_role('button', name='Add').click()

        page.locator('.modal-content').filter(has_text='Registration Form').is_visible()
        expect(page.locator('.modal-content')).to_contain_text('Registration Form')

        page.locator('#firstName[placeholder="First Name"]').fill(value='Some awesome person')

        page.locator('#lastName[placeholder="Last Name"]').fill(value='LastName')

        page.locator('#userEmail[placeholder="name@example.com"]').fill(
            value=f'my_mail{randint(1,9999)}@yahoo.com')

        page.locator('#age[placeholder="Age"]').fill(
            value=f'{randint(1, 150)}')
        page.locator('#salary[placeholder="Salary"]').fill(
            value=f'{randint(100000, 500000)}')
        page.locator('#department[placeholder="Department"]').fill(
            value='IT technology and sleeping')

        page.locator('#submit').click()

        page.close()
        context.close()
        chromium_browser.close()