from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/6/6.html'


browser = webdriver.Chrome()
browser.get(url)

result_num = ((12434107696 * 3) * 2) + 1
element_1 = browser.find_elements(By.TAG_NAME, "option")
for el in element_1:
    if int(el.text) == result_num:
        el.click()
        break
browser.find_element(By.XPATH, "//input[@value='Отправить']").click()
time.sleep(1)
print(f'{result_num=}')
browser.find_element(By.XPATH, "//input[@value='Отправить']").click()
result = browser.find_element(By.ID, 'result').text
print(f'{result=}')
time.sleep(1)
browser.quit()
