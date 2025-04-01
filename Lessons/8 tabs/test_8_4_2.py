import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.2/index.html')

    # Переключаемся на iframe
    iframe1 = browser.find_element(By.ID, "frame1")
    browser.switch_to.frame(iframe1)
    browser.find_element(By.XPATH, "//button[@class='unlock-button']").click()
    browser.switch_to.default_content()

    # Переключаемся на iframe
    iframe2 = browser.find_element(By.ID, "frame2")
    browser.switch_to.frame(iframe2)
    browser.find_element(By.XPATH, "//button[@class='unlock-button']").click()
    browser.switch_to.default_content()

    # Переключаемся на iframe
    iframe3 = browser.find_element(By.ID, "frame3")
    browser.switch_to.frame(iframe3)
    browser.find_element(By.XPATH, "//button[@class='unlock-button']").click()
    browser.switch_to.default_content()

    # Переключаемся на iframe
    iframe4 = browser.find_element(By.ID, "frame4")
    browser.switch_to.frame(iframe4)
    passw = browser.find_element(By.XPATH, "//h2").text
    print(f'{passw=}')
    # browser.switch_to.default_content()


    time.sleep(20)
