import math
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

result = 0

sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]

with webdriver.Chrome() as browser:
    for the_site in sites:
        browser.switch_to.new_window("tab")
        browser.get(the_site)
        browser.find_element(By.XPATH, "//input[@type='checkbox']").click()
        number = browser.find_element(By.XPATH, "//span[@id='result']").text
        result += math.sqrt(int(number))
        time.sleep(1)

    final_result = round(result, 9)
    print(f'{final_result=}')






    print(f'{result=}')
    
