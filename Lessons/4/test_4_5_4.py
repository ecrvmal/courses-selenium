from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = 'https://parsinger.ru/selenium/3/3.html'
browser = webdriver.Chrome()
browser.get(url)

result = 0
element_1 = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")
for el in element_1:
    result += int(el.text)
time.sleep(1)

print(f'{result=}')
time.sleep(1)
browser.quit()
