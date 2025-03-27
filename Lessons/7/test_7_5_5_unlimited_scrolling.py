from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/5.7/1/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)


pieces = browser.find_elements(By.XPATH, f"//button[@class='clickMe']")

for i, piece in enumerate(pieces):
    # scroll to make it visible
    browser.execute_script("return arguments[0].scrollIntoView(true);", piece)

    piece.click()
    print(f'Piece {i} clicked')

alert_text = browser.switch_to.alert.text
print(f'{alert_text=}')
time.sleep(2)
browser.quit()



