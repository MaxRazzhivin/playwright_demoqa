from playwright.sync_api import sync_playwright
import time

''' 
Создаем экзепляр Playwright и запускаем его. 

Запускает движок Playwright и подготавливает драйверы браузеров. 
Возвращает объект Playwright 
'''

playwright = sync_playwright().start()

''' 
Далее, используя объект Playwright, можно запускать браузер и работать с ним.

Стартует процесс Chromium. headless = False - видно окно браузера

По умолчанию Optional[bool] = None, поэтому будет скрывать окно, если не указать явно
'''

browser = playwright.chromium.launch(headless=False)

'''
Создает новую вкладку Page. Технически это еще новый изолированный BrowserContext по 
умолчанию. Вкладка сейчас на about:blank. Мы сохраняем объект Page в переменную page.
'''

page = browser.new_page()

'''
page.goto('https://demoqa.com/') – навигирует эту же вкладку (что создали выше) на 
указанный URL. Никаких «вторых страниц» не создаётся.
'''

page.goto('https://demoqa.com/')

'''
time.sleep(10) – просто ждём 10 секунд, чтобы увидеть окно, 
прежде чем вы его закроете следующей строкой
'''

time.sleep(10)

'''
Закрывает все контексты и вкладки этого браузера
'''
browser.close()

'''
Останавливает Playwright и освобождает ресурсы
'''
playwright.stop()