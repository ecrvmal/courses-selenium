import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
    buttons = browser.find_elements(By.XPATH , "//span[@class='pin']")

    for el in buttons:
        el_text = el.text
        browser.find_element(By.XPATH, "//input[@value='Проверить']").click()
        browser.switch_to.alert.send_keys(el_text)
        browser.switch_to.alert.accept()

        time.sleep(0.1)
        pin_code = browser.find_element(By.ID, "result").text

        if pin_code != 'Неверный пин-код':
            print(f'{pin_code=}')
            break

