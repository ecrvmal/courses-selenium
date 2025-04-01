from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/8/8.3.1/index.html')

with webdriver.Chrome() as browser:
    browser.get(url1)
    time.sleep(0.5)
    browser.find_element(By.ID, 'alertButton').click()
    time.sleep(1)
    alert = browser.switch_to.alert  # Если вы планируете что-то делать с этим событием, можно добавить его в переменную
    print(alert.text)
    time.sleep(1)
    alert.accept()
    time.sleep(1)

    browser.find_element(By.ID, 'promptButton').click()
    time.sleep(2)
    prompt = browser.switch_to.alert
    prompt.send_keys('Alert')
    time.sleep(.5)
    prompt.accept()
    time.sleep(.5)

    browser.find_element(By.ID, 'confirmButton').click()
    time.sleep(2)
    confirm = browser.switch_to.alert
    confirm.accept()  # Замените на .dismiss() чтобы нажать на кнопку "Отмена"
    time.sleep(.5)

    secret_key = browser.find_element(By.ID, 'secretKey').text
    print(f'{secret_key=}')
    time.sleep(15)






