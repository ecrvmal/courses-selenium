from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.3.1/index.html'
browser = webdriver.Chrome()
browser.get(url)

elem1 = browser.find_element(By.ID, 'parent_id')
elem1.click()
elem1.find_element(By.CLASS_NAME, 'child_class').click()

pass_text = elem1.find_element(By.CLASS_NAME, 'child_class').get_attribute('password')
print(f'{pass_text=}')
time.sleep(1)
browser.quit()
