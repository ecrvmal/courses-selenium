from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/8/8.2.2/index.html')

with webdriver.Chrome() as browser:
    browser.get(url1)
    time.sleep(5)
    window_size = browser.get_window_size()
    result = window_size['width'] + window_size['height']
    pass_text = browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.ID, "checkBtn").click()
    time.sleep(5)
    pass_text = browser.find_element(By.ID, "resultMessage").text
    time.sleep(5)
    print(f'{pass_text=}')



