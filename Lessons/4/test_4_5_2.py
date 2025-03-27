from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/2/2.html'
browser = webdriver.Chrome()
browser.get(url)

element_1 = browser.find_element(By.XPATH, "//*[contains(text(), '16243162441624')]")
element_1.click()
result_field = browser.find_element(By.XPATH, "//p[@id='result']")
result = result_field.text
time.sleep(1)

print(f'{result=}')
time.sleep(1)
browser.quit()
