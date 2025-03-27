from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = 'https://parsinger.ru/selenium/6/6.2.1/index.html'


browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
el = browser.find_element(By.ID , "this_pic")
el.screenshot('the_screenshot.png')
el_text = el.text
print(f'{el_text}')
time.sleep(2)
browser.quit()
