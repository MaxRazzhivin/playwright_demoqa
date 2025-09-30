import time
from random import choice

from playwright.sync_api import sync_playwright

pages = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.yandex.ru"
]

with sync_playwright() as p:
    # 2 браузера
    chromium = p.chromium.launch(headless=False)
    firefox = p.firefox.launch(headless=False)

    for browser in (chromium, firefox):
        # создаем по 2 независимых констекта
        context_1 = browser.new_context()
        context_2 = browser.new_context()

        for context in (context_1, context_2):
            # создаем по 2 страницы на каждый контекст
            page_1 = context.new_page()
            page_1.goto(choice(pages))
            page_2 = context.new_page()
            page_2.goto(choice(pages))

            time.sleep(10)

            page_1.close()
            page_2.close()

        context_1.close()
        context_2.close()

    chromium.close()
    firefox.close()
