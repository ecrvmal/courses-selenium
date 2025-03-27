from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/4/4.html'
browser = webdriver.Chrome()
browser.get(url)

result = 0
element_1 = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
for el in element_1:
    el.click()
time.sleep(1)
browser.find_element(By.ID, 'input_result').send_keys(f'{result}')
browser.find_element(By.Xpath, 'input_result').send_keys(f'{result}')
print(f'{result=}')
time.sleep(1)
browser.quit()
