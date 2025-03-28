from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/8/8.1/site1/')

with webdriver.Chrome() as browser:
    browser.get("about:blank")
    time.sleep(5)


# print(f'{final_summ=}')

time.sleep(2)
browser.quit()



