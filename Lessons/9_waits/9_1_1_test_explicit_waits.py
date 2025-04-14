
'''
Задача: Получить секретный пароль, используя WebDriverWait.

1️⃣ С помощью Selenium зайдите на сайт-тренажёр.
2️⃣ На странице находятся 5 кнопок, первые 4 из которых активируется через случайный промежуток времени.
3️⃣ Используйте WebDriverWait, чтобы дождаться активации каждой кнопки и нажать её.
4️⃣ Финальная кнопка станет активной после нажатия всех предыдущих и откроет секретный пароль.
5️⃣ Считайте пароль и вставьте его в поле ниже на платформе Stepik.

'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


url = 'https://parsinger.ru/selenium/9/9.1.1/index.html'

btns = ['button1',  'button2', 'button3', 'button4', 'finalButton', ]


with webdriver.Chrome() as browser:

    browser.get(url)
    for btn in btns:
        WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.ID, btn))).click()

    message_text1 = browser.find_element(By.ID, 'message').text
    message_text2 = browser.find_element(By.ID, 'message2').text
    sleep(4)

    print(f'{message_text1=}')
    print(f'{message_text2=}')


