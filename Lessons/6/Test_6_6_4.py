from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/selenium/5.5/3/1.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
fields = browser.find_elements(By.CLASS_NAME, "text-field")
print(f'{fields=}')
for field in fields:
    attr_ind = field.get_attribute('disabled')
    print(f'{attr_ind=}')
    if attr_ind is None:
        field.clear()
browser.find_element(By.ID, "checkButton").click()

time.sleep(10)

browser.quit()

