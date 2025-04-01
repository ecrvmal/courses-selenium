import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.3/index.html')

    # Переключаемся на iframe
    iframe1 = browser.find_element(By.XPATH, "//iframe[@src='spiral_1/index.html']")
    browser.switch_to.frame(iframe1)
    browser.find_element(By.XPATH, "//button[@class='button']").click()


    # Переключаемся на iframe
    iframe2 = browser.find_element(By.XPATH, "//iframe[@src='../spiral_2/index.html']")
    browser.switch_to.frame(iframe2)
    browser.find_element(By.XPATH, "//button[@class='button']").click()

    # Переключаемся на iframe
    iframe3 = browser.find_element(By.XPATH, "//iframe[@src='../spiral_3/index.html']")
    browser.switch_to.frame(iframe3)
    browser.find_element(By.XPATH, "//button[@class='button']").click()

    # Переключаемся на iframe
    iframe4 = browser.find_element(By.XPATH, "//iframe[@src='../spiral_4/index.html']")
    browser.switch_to.frame(iframe4)
    browser.find_element(By.XPATH, "//button[@class='button']").click()

    pass_text = browser.find_element(By.XPATH, "//div[@class='password-container']").text
    print(f'{pass_text=}')

    time.sleep(5)
