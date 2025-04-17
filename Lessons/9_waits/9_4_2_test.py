"""
Отследите изменение URL и получите пароль!
🔹 Задача: Получить секретный пароль, используя WebDriverWait + EC.url_changes().

1️⃣ Запустите Selenium и откройте сайт-тренажёр.
2️⃣ Нажмите кнопку "Начать", после чего откроется Тестовая страница. Зафиксируйте текущий URL current_url= browser.current_url.
3️⃣ Используйте WebDriverWait + EC.url_changes(), чтобы дождаться изменения текущего URL.
4️⃣ Как только условие из пункта 3 сработает и станет True, извлеките пароль.
5️⃣ Вставьте пароль в поле ниже на платформе Stepik.
🟢 Важно:

URL изменится автоматически через 5 секунд после перехода.
Пароль появится только при использовании Selenium WebDriver.

"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://parsinger.ru/selenium/9/9.4.4/index.html'


with webdriver.Chrome() as browser:
    browser.get(url)
    sleep(2)
    browser.find_element(By.LINK_TEXT, "Начать").click()
    current_url = browser.current_url
    sleep(2)
    WebDriverWait(browser, 10).until(EC.url_changes(current_url))
    pass_test = browser.find_element(By.ID, "password").text

    sleep(2)
    print(f'{pass_test=}')