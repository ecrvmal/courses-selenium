from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/7/7.2/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)

for i in range(1, 101):
    browser.find_element(By.XPATH, f"//input[@placeholder='Поле {i}']").send_keys('abrakadabra')
    (ActionChains(browser).key_down(Keys.ENTER).
     key_down(Keys.ARROW_DOWN).perform())
    print(f'{i=}')
time.sleep(20)
result_text = browser.find_element(By.XPATH, "//div[@id='hidden-password']").text
print(f'{result_text=}')
browser.quit()



