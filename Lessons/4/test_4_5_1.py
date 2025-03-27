from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/1/1.html'
browser = webdriver.Chrome()
browser.get(url)

elements_1 = browser.find_elements(By.XPATH, "//input[@type='text']")
for el in elements_1:
    el.send_keys("Текст")
check_button = browser.find_element(By.XPATH, "//input[@type='button']")
check_button.click()
result_field = browser.find_element(By.ID, 'result')
result = result_field.text
time.sleep(1)

print(f'{result=}')
time.sleep(1)
browser.quit()
