import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
    buttons = browser.find_elements(By.XPATH , "//input[@class='buttons']")

    for el in buttons:
        el.click()
        alert_text = browser.switch_to.alert.text
        print(f'{alert_text=}')
        browser.switch_to.alert.accept()
        browser.find_element(By.ID,"input").send_keys(alert_text)
        browser.find_element(By.XPATH, "//input[@value='Проверить']").click()
        time.sleep(0.1)
        pin_code = browser.find_element(By.ID, "result").text

        if pin_code != 'Неверный пин-код':
            print(f'{pin_code=}')
            break

