from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.3.3/index.html'
browser = webdriver.Chrome()
browser.get(url)

num_of_troopers= 0
elements_1 = browser.find_elements(By.XPATH, '//a')
for el in elements_1:
    attr = el.get_attribute('stormtrooper')
    print(f'{attr=}')
    if attr.isdigit():
        num_of_troopers += int(attr)
check_field = browser.find_element(By.ID, 'inputNumber')
check_field.send_keys(f'{num_of_troopers}')
check_btn = browser.find_element(By.ID, 'checkBtn')
check_btn.click()
result_field = browser.find_element(By.ID, 'feedbackMessage')
result = result_field.text
time.sleep(30)

print(f'{result=}')
time.sleep(1)
browser.quit()
