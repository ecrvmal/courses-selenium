from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.3.2/index.html'
browser = webdriver.Chrome()
browser.get(url)

elements_1 = browser.find_elements(By.CLASS_NAME, 'block')
for el in elements_1:
    el.find_element(By.TAG_NAME, 'button').click()
passw_text = browser.find_element(By.TAG_NAME, 'password').text

print(f'{passw_text=}')
time.sleep(1)
browser.quit()
