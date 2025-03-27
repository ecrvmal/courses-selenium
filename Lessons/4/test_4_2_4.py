from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.2.4/index.html'
browser = webdriver.Chrome()
browser.get(url)

elem1 = browser.find_element(By.ID, 'secret-key-button')
elem1.click()
time.sleep(1)
data_text = elem1.get_attribute("data")
print(f'{data_text=}')
time.sleep(1)
browser.quit()
