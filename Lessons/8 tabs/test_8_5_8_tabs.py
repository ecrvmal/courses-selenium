import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

result = 0

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/blank/3/index.html')

    buttons = browser.find_elements(By.XPATH, "//input[@type='button']")
    for but in buttons :
        but.click()

    descriptors = browser.window_handles
    for descr in descriptors[1:]:
        browser.switch_to.window(descr)
        # title_text = browser.execute_script("return document.title;")  # it works
        title_text = browser.title    # it works
        print(f'{title_text=}')
        result += int(title_text)
    print(f'{result=}')
    
