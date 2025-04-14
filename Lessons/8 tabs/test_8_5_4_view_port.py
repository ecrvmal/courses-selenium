import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/window_size/1/')
    inner_width = browser.execute_script("return window.innerWidth")
    inner_height = browser.execute_script("return window.innerHeight")
    bro_size = browser.get_window_size()
    print(f'{inner_width=}')
    print(f'{inner_height=}')
    print(f'{bro_size=}')

    w_margine = bro_size['width'] - inner_width
    h_margine = bro_size['height'] - inner_height

    browser.set_window_size(555 + w_margine, 555 + h_margine)
    time.sleep(2)
    result = browser.find_element(By.ID, "result").text
    print(f'{result=}')