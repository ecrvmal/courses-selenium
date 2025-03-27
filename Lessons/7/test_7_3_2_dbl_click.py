from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/7/7.3.2/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)

circle = browser.find_element(By.ID, 'dblclick-area')
actions = ActionChains(browser)
actions.double_click(circle).perform()

time.sleep(2)
result_text = browser.find_element(By.XPATH, "//div[@id='passwordContainer']").text
print(f'{result_text=}')
browser.quit()



