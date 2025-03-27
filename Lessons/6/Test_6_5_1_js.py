from pprint import pprint

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/selenium/6/6.5/index.html')
cookie_dict = {
    'name': 'secretKey',    # Любое имя для cookie
    'value': 'selenium123',  # Любое значение для cookie
}

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
el = browser.find_element(By.ID, 'target' )
browser.execute_script("return arguments[0].scrollIntoView(true);", el)

time.sleep(3)
browser.find_element(By.ID, 'target' ).click()
el3 = browser.find_element(By.ID, 'secret-key-container')
el_text = el3.text
time.sleep(10)
print(f'{el_text=}')
browser.quit()
