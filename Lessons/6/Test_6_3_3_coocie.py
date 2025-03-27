from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/selenium/6/6.3.2/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
browser.delete_all_cookies()
time.sleep(20)
browser.quit()
