from selenium import webdriver
import time

url1 = 'https://parsinger.ru/selenium/8/8.1/site1/'
url2 = 'https://parsinger.ru/selenium/8/8.1/site2/'

with webdriver.Chrome() as browser:
    pass
    browser.get("about:blank")
    browser.get(url1)
    title_string = browser.title
    num1 = ''.join(c for c in title_string if c not in '349') # remove chars 3,4,9 from title
    print(f'{num1=}')
    time.sleep(3)

    browser.get(url2)
    title_string = browser.title
    num2 = ''.join(c for c in title_string if c not in '780') # remove chars 3,4,9 from title
    print(f'{num2=}')
    time.sleep(3)

    result = int(num1) + int(num2)
    print(f'{result=}')