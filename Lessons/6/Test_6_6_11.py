from selenium import webdriver
import time
# from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/methods/3/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(3)
cookies = browser.get_cookies()
value_summ : int =0
for cookie in cookies:
    cookie_name = cookie['name']
    print(f'{cookie_name=}')
    if cookie_name.startswith('secret_cookie_'):
        cookie_value = cookie['value']
        print(f'{cookie_value=}')
        value_summ += int(cookie_value)

time.sleep(2)
print(f'{value_summ=}')
browser.quit()

