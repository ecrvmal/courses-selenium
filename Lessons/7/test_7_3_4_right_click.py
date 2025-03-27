from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/7/7.3.4/index.html'
        '')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)

actionChains = ActionChains(browser)
element = browser.find_element(By.ID ,'context-area' )
actionChains.context_click(element).perform()
time.sleep(1)
browser.find_element(By.XPATH, "//div[@data-action='get_password']").click()

time.sleep(2)
result_text = browser.find_element(By.XPATH, "//span[@key='access_code']").text
print(f'{result_text=}')
time.sleep(2)
browser.quit()



