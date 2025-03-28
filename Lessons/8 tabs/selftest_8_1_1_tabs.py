"""
Сколько вкладок будет открыто после выполнения следующего кода? -> 4
"""
import time
from selenium import webdriver
with webdriver.Chrome() as browser:
    time.sleep(1)
    browser.get("http://ya.ru")
    browser.switch_to.new_window("tab")
    browser.switch_to.new_window("tab")
    browser.switch_to.new_window("tab")
    time.sleep(5)