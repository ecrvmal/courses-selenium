from pprint import pprint

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/methods/1/index.html')


browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
while True:
    browser.refresh()
    el = browser.find_element(By.ID, 'result' )
    el_text = el.text
    if el_text != 'refresh page':
        print(f'{el_text=}')
        break
browser.quit()
