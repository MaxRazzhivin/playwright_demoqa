import time

from playwright.sync_api import expect


def test_text_box(page):
    page.goto('https://demoqa.com/text-box')

    # Вариант № 1
    username_locator = '#userName'
    email_locator = '#userEmail'
    address_locator = '#currentAddress'
    permanent_address = '#permanentAddress'

    page.fill(username_locator, 'testQa')
    page.fill(email_locator, "my_email@yahoo.com")
    page.fill(address_locator, 'London is a capital of Great Britain')
    page.fill(permanent_address, 'pam-pam-pam')

    page.click('#submit')


    # # вариант № 2
    # page.locator('#userName').fill('testQa')

    # # вариант № 3
    # page.fill(selector='#userName', value='testQa')

    expect(page.locator('#output #name')).to_have_text('Name:testQa')
    expect(page.locator('#output #email')).to_have_text('Email:my_email@yahoo.com')
    expect(page.locator('#output #currentAddress')).to_have_text('Current Address :London is a capital of Great Britain')
    expect(page.locator('#output #permanentAddress')).to_have_text('Permananet Address :pam-pam-pam')

    time.sleep(5)