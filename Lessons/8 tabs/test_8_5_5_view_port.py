import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/window_size/2/index.html')
    inner_width = browser.execute_script("return window.innerWidth")
    inner_height = browser.execute_script("return window.innerHeight")
    bro_size = browser.get_window_size()
    print(f'{inner_width=}')
    print(f'{inner_height=}')
    print(f'{bro_size=}')

    w_margine = bro_size['width'] - inner_width
    h_margine = bro_size['height'] - inner_height
    break_mark = False

    for  size_x in window_size_x:
        if break_mark:
            break
        for size_y in window_size_y:
            browser.set_window_size(size_x + w_margine, size_y + h_margine)
            time.sleep(0.1)
            result = browser.find_element(By.ID, "result").text
            # print(f'{result=}')
            if result != "":
                print(f'{result=}')
                break_mark = True
                break
