from selenium import webdriver
import time
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/7/7.1/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)
page_height = browser.execute_script("return document.body.scrollHeight")
browser.execute_script(f"window.scrollTo(0, {page_height})")
time.sleep(10)
print(page_height)
browser.quit()



