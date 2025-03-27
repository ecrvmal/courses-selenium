from math import ceil

from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/5.7/5/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)

actions = ActionChains(browser)
buttons = browser.find_elements(By.XPATH, f"//button[@class='timer_button']")

for the_button in buttons:
    button_time : int = int(ceil(float(the_button.text))) + 1
    actions.click_and_hold(the_button).pause(button_time).release(the_button).perform()
    print('done')
    # actions.reset_actions()

time.sleep(1)
alert_text = browser.switch_to.alert.text
print(f'{alert_text=}')

time.sleep(2)
browser.quit()



