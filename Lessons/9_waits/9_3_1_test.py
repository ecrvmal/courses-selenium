"""
Условие:

На сайте находится кнопка «Добавить элемент» (id="startButton"). При нажатии на неё поочерёдно появляются 5 кнопок с id="dynamicButton".
Кнопки появляются с разной случайной задержкой (от 2 до 6 секунд), а пароль отображается только после успешного нажатия на все 5 кнопок.
Важно:

Если Selenium попытается кликнуть на кнопку до её появления, тест упадёт с ошибкой NoSuchElementException. Чтобы избежать этого, необходимо использовать неявное ожидание implicitly_wait().
Задача: Автоматизация последовательного нажатия динамических кнопок

1️⃣ Используйте .implicitly_wait()  для неявного ожидания.
2️⃣ С помощью Selenium зайдите на сайт-тренажёр.
3️⃣ Нажмите на  5 динамических кнопок (id="dynamicButton").
4️⃣ После нажатия всех 5 кнопок отобразится пароль в id="secretPassword".
5️⃣ Считайте пароль из DOM и вставьте его в поле ниже на Stepik.
Внимание: Пароль отобразится только при использовании Selenium.

Цель: применить неявное ожидание (implicitly_wait()) для работы с динамическими элементами.
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/9/9.3.1/index.html'

with webdriver.Chrome() as browser:
    browser.implicitly_wait(7)
    browser.get(url)
    browser.find_element(By.ID, "startButton").click()
    for _ in range(5):
        browser.find_element(By.ID, "dynamicButton").click()

    pass_text = browser.find_element(By.ID, "secretPassword").text
    print(f'{pass_text=}')
    sleep(3)