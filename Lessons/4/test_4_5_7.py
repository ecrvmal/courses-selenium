from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/7/7.html'


browser = webdriver.Chrome()
browser.get(url)

result_num = 0
element_1 = browser.find_elements(By.TAG_NAME, "option")
for el in element_1:
    print(f'{el.text=}')
    result_num += int(el.text)
time.sleep(1)
print(f'{result_num=}')
browser.find_element(By.ID, 'input_result').send_keys(f'{result_num}')
browser.find_element(By.XPATH, "//input[@value='Отправить']").click()
result = browser.find_element(By.ID, 'result').text
print(f'{result=}')
time.sleep(1)
browser.quit()
