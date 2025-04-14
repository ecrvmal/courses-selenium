import math
import re
import time

from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By

result = 0
url = 'https://parsinger.ru/selenium/5.8/5/index.html'

with webdriver.Chrome() as browser:

    browser.get(url)

    iframes = browser.find_elements(By.XPATH, "//iframe")
    for iframe in iframes:
        browser.switch_to.frame(iframe)
        browser.find_element(By.XPATH, "//button[@onclick = 'showNumber()']").click()
        num = browser.find_element(By.XPATH, "//p[@id='numberDisplay']").text
        browser.switch_to.default_content()
        browser.find_element(By.ID, "guessInput").clear()
        browser.find_element(By.ID, "guessInput").send_keys(num)
        browser.find_element(By.ID, "checkBtn").click()

        try:
            alert = browser.switch_to.alert.text
            print(f'{alert=}')
        except NoAlertPresentException:
            pass
        time.sleep(1)
    time.sleep(2)



