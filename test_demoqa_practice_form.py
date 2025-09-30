import time
from datetime import datetime
from random import randint

from playwright.sync_api import sync_playwright


def test_practice_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto('https://demoqa.com/automation-practice-form')

            page.type('#firstName', "Robert")
            page.type('#lastName', 'Pattison')
            page.type('#userEmail', f'some_{randint(1,9999)}@yahoo.com')
            page.get_by_text("Male", exact=True).click()
            page.type('#userNumber', '79005647884')

            # Проверяем что дата по умолчанию = сегодня
            current_date_demoqa = page.get_attribute('#dateOfBirthInput', 'value')
            real_current_date = datetime.now().strftime('%d %b %Y')

            assert real_current_date == current_date_demoqa, (f"Ожидали дату "
                                                              f"{real_current_date}, "
                                                              f"получили {current_date_demoqa}")

            # После проверки даты заполняем уже актуальную дату рождения
            page.fill('#dateOfBirthInput', '04.06.1989')


            page.locator('#subjectsInput').click()

            page.keyboard.type('ma', delay=50)
            page.keyboard.press('Tab')

            page.get_by_text("Sports", exact=True).click()
            page.get_by_text("Music", exact=True).click()

            page.type('#currentAddress', 'Somewhere in galaxy')


            page.locator('#state').click()

            page.get_by_text('Haryana').click()

            page.locator('#city').click()

            page.get_by_text('Panipat').click()

            # Проверим текст из футера, что он равен тому, что на сайте

            text_ui = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
            text_from_footer = page.text_content('footer')

            assert text_ui == text_from_footer, ('Текст на сайте футера и из верстки '
                                                 'не совпали')

            # Жмем кнопку Submit
            page.get_by_role('button', name='Submit').click()


            time.sleep(5)


        finally:
            page.close()
            context.close()
            browser.close()
