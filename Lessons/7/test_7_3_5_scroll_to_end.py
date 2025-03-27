from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/7/7.3.5/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)

actionChains = ActionChains(browser)
element = browser.find_element(By.ID ,'scrollable-container-left' )
actionChains.click(element).send_keys(Keys.END).perform()
time.sleep(1)
element = browser.find_element(By.ID ,'scrollable-container-right' )
actionChains.click(element).send_keys(Keys.END).perform()
time.sleep(1)

time.sleep(2)
result_text = browser.find_element(By.XPATH, "//span[@key='access_code']").text
print(f'{result_text=}')
time.sleep(2)
browser.quit()



