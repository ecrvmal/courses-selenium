from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/7/7.3.3/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)


actions = ActionChains(browser)
actions.key_down(Keys.CONTROL) \
       .key_down(Keys.ALT) \
       .key_down(Keys.SHIFT) \
       .key_down('T') \
.perform()

actions.key_up(Keys.CONTROL) \
       .key_down(Keys.ALT) \
       .key_down(Keys.SHIFT) \
       .key_down('T') \
.perform()


time.sleep(2)
result_text = browser.find_element(By.XPATH, "//span[@key='access_code']").text
print(f'{result_text=}')
browser.quit()



