from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/selenium/6/6.3/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
cookies = browser.get_cookies()
for cookie in cookies:
    print(f'{cookie['name']=}')
    print(f'{cookie['value']=}')
time.sleep(2)
browser.quit()
