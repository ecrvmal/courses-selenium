from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/7/7.4.1/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)

actionChains = ActionChains(browser)

actionChains.scroll_by_amount(0, 1000).perform()
time.sleep(4)
code1 = browser.find_element(By.CLASS_NAME ,'countdown' ).text
print(f'{code1=}')
time.sleep(2)

actionChains.scroll_by_amount(0, 1100).perform()
time.sleep(1)
browser.find_element(By.XPATH, "//input[@placeholder='Введите код']").send_keys(code1[5:])
time.sleep(2)
browser.find_element(By.XPATH, '//button[text()="Проверить"]').click()
time.sleep(20)
result_text = browser.find_element(By.ID, 'final-key').text
print(f'{result_text=}')
time.sleep(5)
browser.quit()



