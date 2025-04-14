"""
🔹 Задача: Дождаться правильного title и получить секретный пароль.

1️⃣ С помощью Selenium зайдите на сайт-тренажёр.
2️⃣ Нажмите кнопку "INITIATE SCAN" для запуска сканирования.
3️⃣ Title страницы начнёт динамически изменяться (пример: "Scanning..." → "Processing..." → "Access Granted").
4️⃣ Используйте WebDriverWait с title_is("Access Granted"), чтобы дождаться нужного заголовка.
5️⃣ Как только title изменится на "Access Granted", пароль появится на странице.
6️⃣ Считайте пароль из DOM и вставьте его в поле ниже на Stepik.
🟢 Внимание: Пароль отобразится только при использовании Selenium.
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/9/9.2.1/index.html')
    browser.find_element(By.ID, "startScan").click()
    element = WebDriverWait(browser, 30).until(EC.title_is("Access Granted"))
    pass_text = browser.find_element(By.ID, "password").text

    print(f'{pass_text=}')
