from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/methods/5/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
links = browser.find_elements(By.XPATH, "//a[@href]")
cookie_life = 0
page_value = 0
cookies = browser.get_cookies()
for link in links:
    print(link.get_attribute("href"))
    link.click()
    time.sleep(0.1)
    cookies = browser.get_cookies()[0]
    # print(f'{cookies=}')
    if cookies['expiry'] > cookie_life:
        cookie_life = cookies['expiry']
        page_value = browser.find_element(By.ID, value = 'result').text
    browser.back()
    time.sleep(0.1)
time.sleep(2)
print(f'{page_value=}')
browser.quit()

