import re

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/8/8.4.1/')

    # Переключаемся на iframe
    iframe_element = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(iframe_element)

    # Извлекаем HTML содержимое из iframe
    iframe_content = browser.page_source

    print(iframe_content)

    letters = re.findall(r'\*(.*?)\*', iframe_content)  # ['F', 'r', 'a', 'm', 'e', 'M', 'a', 's', 't', 'e', 'r']
    print(f'{letters=}')
    word = ''.join(letters)  # 'FrameMaster'
    print(f'{word=}')