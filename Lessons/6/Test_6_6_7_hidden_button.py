from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/scroll/4/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
script_result = 0
elements = browser.find_elements(By.CLASS_NAME, 'btn')
for el in elements:
    browser.execute_script("return arguments[0].scrollIntoView(true);", el)
    el.click()
    script_result += int(browser.find_element(By.ID,'result').text)
print(f'{script_result=}')
browser.quit()

