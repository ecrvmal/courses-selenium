from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/7/7.3.1/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)

face = browser.find_element(By.ID, 'draggable')
sw_pool = browser.find_element(By.ID, 'target')
actions = ActionChains(browser)
actions.drag_and_drop(face, sw_pool).perform()
time.sleep(20)
result_text = browser.find_element(By.XPATH, "//div[@id='passwordContainer']").text
print(f'{result_text=}')
browser.quit()



