from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/5.7/4/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)

actions = ActionChains(browser)
boxes = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
final_summ : int = 0
num_checkboxes = 0
scroll_checkboxes = True
inputs: list[WebElement] = []

while scroll_checkboxes:
    inputs = browser.find_elements(By.XPATH, "//input[@type='checkbox']")

    browser.execute_script("return arguments[0].scrollIntoView(true);", inputs[-1])
    time.sleep(1)
    browser.execute_script("window.scrollBy(0, 500)")
    time.sleep(1)
    print('scroll down')

    print(f'{len(inputs)=}')
    if len(inputs) > num_checkboxes:
        num_checkboxes = len(inputs)
    else:
        scroll_checkboxes = False


for el in inputs:
    if int(el.get_attribute('value')) % 2 == 0:
        el.click()
time.sleep(3)

# browser.execute_script("window.scrollBy(0, 500)")   # scrolling 500px down
the_button = browser.find_element(By.XPATH, "//button[@class='alert_button']")
# scrolling while button will appear
browser.execute_script("return arguments[0].scrollIntoView(true);", the_button)

the_button.click()
time.sleep(1)

alert_text = browser.switch_to.alert.text
print(f'{alert_text=}')

time.sleep(2)
browser.quit()



