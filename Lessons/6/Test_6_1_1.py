from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = 'https://parsinger.ru/selenium/6/6.2/index.html'


browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
browser.find_element(By.LINK_TEXT  , "Страница 2").click()
time.sleep(3)
browser.find_element(By.LINK_TEXT  , "Перейти на страницу 3").click()
time.sleep(3)
browser.back()
time.sleep(3)
browser.back()
time.sleep(3)
browser.find_element(By.ID, "getPasswordBtn").click()
time.sleep(6)

time.sleep(1)
browser.quit()
