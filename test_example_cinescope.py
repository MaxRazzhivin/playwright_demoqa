import random
import time

from playwright.sync_api import expect

url = 'https://dev-cinescope.coconutqa.ru/register'

def test_cinescope_registration(page):
    page.goto(url)
    username_locator = '[name=fullName]'
    email_locator = '[name=email]'
    password_locator = '[name=password]'
    password_repeat_locator = '[name=passwordRepeat]'
    button_submit_locator = '[type=submit]'

    user_email = f'testqapampam{random.randint(1,9999)}@yahoo.com'

    # # Вариант № 1
    # page.fill(username_locator, 'Жмышенко Петр Евгеньевич')

    # Вариант № 2
    page.locator(username_locator).fill('Жмышенко Петр Евгеньевич')

    # # Вариант № 3
    # page.fill(selector=username_locator, value='Жмышенко Петр Евгеньевич')

    page.locator(email_locator).fill(user_email)
    page.locator(password_locator).fill('Ddojgo@dij34')
    page.locator(password_repeat_locator).fill('Ddojgo@dij34')

    page.locator(button_submit_locator).click()

    page.wait_for_url('https://dev-cinescope.coconutqa.ru/login')
    expect(page.get_by_text('Подтвердите свою почту')).to_be_visible(visible=True)

    time.sleep(10)