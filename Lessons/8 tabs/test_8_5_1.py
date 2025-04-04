import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    buttons = browser.find_elements(By.XPATH , "//input[@class='buttons']")

    for el in buttons:
        el.click()
        browser.switch_to.alert.accept()
        time.sleep(0.1)
        passw = browser.find_element(By.ID, "result").text

        if passw:
            print(f'{passw=}')
            break

