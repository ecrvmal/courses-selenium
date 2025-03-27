from pprint import pprint

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/selenium/6/6.3.3/index.html')
cookie_dict = {
    'name': 'secretKey',    # Любое имя для cookie
    'value': 'selenium123',  # Любое значение для cookie
}

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
browser.add_cookie(cookie_dict)
pprint(browser.get_cookies())
time.sleep(20)
browser.refresh()
el = browser.find_element(By.ID, "password")
el_text = el.text
time.sleep(10)
print(f'{el_text=}')
browser.quit()
