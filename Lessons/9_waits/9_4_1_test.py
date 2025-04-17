"""
 Задача: Получить секретный пароль, используя WebDriverWait + EC.url_to_be().

1️⃣ Перейдите на главную страницу сайта-тренажёра через Selenium.
2️⃣ Перейти по кнопке  "Правильный путь".
3️⃣ Используя WebDriverWait и EC.url_to_be(), дождитесь смены ссылки на https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure, и только после этого извлекайте пароль.
4️⃣ Вставьте пароль в поле ниже на платформе Stepik.
🟢 Важно:

Ссылка для перехода на правильный путь отличается от финальной ссылки, которую вам нужно дождаться. Она изменится спустя 6 секунд после пребывания на сайте.
Пароль появится только при использовании Selenium, не пытайтесь использовать аргументы или средства которые скрывают Selenium.

"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://parsinger.ru/selenium/9/9.4.3/index.html'
new_url = 'https://parsinger.ru/selenium/9/9.4.3/final.html?key=secure'

with webdriver.Chrome() as browser:
    browser.get(url)
    sleep(2)
    browser.find_element(By.LINK_TEXT, "Правильный путь").click()
    WebDriverWait(browser, 10).until(EC.url_to_be(new_url))
    pass_test = browser.find_element(By.ID, "password").text

    sleep(2)
    print(f'{pass_test=}')