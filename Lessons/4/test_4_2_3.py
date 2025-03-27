from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.2.3/index.html'
browser = webdriver.Chrome()
browser.get(url)

elem1 = browser.find_element(By.ID, 'showTextBtn')
elem1.click()
time.sleep(1)
elem2 = browser.find_element(By.ID, 'text1')
text_pass = elem2.text
elem3 = browser.find_element(By.ID, 'userInput')
elem3.send_keys(text_pass)
elem4 = browser.find_element(By.ID, 'checkBtn')
elem4.click()
elem5 = browser.find_element(By.ID, 'text2')
text_pass2 = elem5.text
print(f'{text_pass2=}')
time.sleep(1)
browser.quit()
