from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/selenium/5.5/4/1.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
script_result = 0
elements = browser.find_elements(By.CLASS_NAME, 'parent')
for el in elements:
    el_text = el.find_element(By.XPATH,  './textarea[1]').text
    el.find_element(By.XPATH, './textarea[2]').send_keys(el_text)
    el.find_element(By.XPATH, './textarea[1]').clear()
    el.find_element(By.XPATH, './button').click()
time.sleep(30)

browser.quit()

