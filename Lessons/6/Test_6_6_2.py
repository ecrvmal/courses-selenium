from pprint import pprint

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/selenium/5.5/1/1.html')


browser = webdriver.Chrome()
browser.get(url1)
squares = browser.find_elements(By.CLASS_NAME, 'text-field')
for sq in squares:
    sq.clear()
browser.find_element(By.ID, 'checkButton').click()
time.sleep(20)
browser.quit()
