from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/selenium/6/6.3.1/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
cookie_data = browser.get_cookie('token_22')
print(f'{cookie_data=}')
time.sleep(2)
browser.quit()
