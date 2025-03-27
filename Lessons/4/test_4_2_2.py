from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.2.2/index.html'
browser = webdriver.Chrome()
browser.get(url)

elem = browser.find_element(By.ID, 'codeInput')
elem.send_keys("Дрогон")
elem = browser.find_element(By.ID, 'clickButton')
elem.click()
time.sleep(5)
browser.quit()
