from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/8/8.2.1/index.html')

with webdriver.Chrome() as browser:
    browser.get(url1)
    time.sleep(5)
    browser.set_window_size(1200,720)
    browser.find_element(By.ID, "checkSizeBtn").click()
    pass_text = browser.find_element(By.ID, "message").text
    time.sleep(10)
    print(f'{pass_text=}')



