from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/selenium/5.5/3/1.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
script_result = 0
elements = browser.find_elements(By.CLASS_NAME, 'parent')
for el in elements:
    if el.find_element(By.CLASS_NAME, 'checkbox').is_selected():
        script_result += int(el.text)
print(f'{script_result=}')
browser.quit()

