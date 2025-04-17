"""
Абу и бананы
Помогите Абу найти бананы и получите пароль!

1️⃣ С помощью Selenium зайдите на сайт-тренажёр.
2️⃣ На сайте есть кнопка "Искать бананы", которая при нажатии рандомно открывает копию страницы с другим URL.
3️⃣ Используйте метод .url_contains("...") дождитесь пока в URL будет эта строка текста "qLChv49", это будет сигналом, что вы попали на страницу с бананами.
4️⃣ Кликните по кнопке "Проверить улов" и извлеките пароль из тега <p>.
5️⃣ Вставьте пароль в поле ниже на платформе Stepik.
🟢 Внимание: Кнопка "Искать бананы" отобразится только при использовании Selenium!

📢 Важно: Напоминаю, как работает WebDriverWait(browser, 5).until(EC.url_contains("qLChv49")).

Если условие не вернёт True в течение 5 секунд (то есть, если URL не содержит "qLChv49"), эта строка кода вызовет исключение TimeoutException.

Внимание, спойлер!
Рекомендуется использовать while True, break, continue, try, except, потому что если WebDriverWait не найдёт совпадение в URL, он выбросит исключение TimeoutException. Вам нужно обработать его и перезапустить цикл.

"""
from time import sleep

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://parsinger.ru/selenium/9/9.4.1/3VT6JyXnI7EQqG0632xSAQyD4Z.html'


with webdriver.Chrome() as browser:
    browser.get(url)
    sleep(2)
    pass_found = False

    while not pass_found:
        browser.find_element(By.LINK_TEXT, "Искать бананы").click()
        sleep(1)
        try:
            WebDriverWait(browser, 1).until(EC.url_contains("qLChv49"))
            pass_found = True
        except TimeoutException:
            pass

    sleep(3)
    browser.find_element(By.ID, "checkButton").click() # Button "Проверить улов"
    pass_test = browser.find_element(By.TAG_NAME, "p").text
    sleep(5)
    print(f'{pass_test=}')