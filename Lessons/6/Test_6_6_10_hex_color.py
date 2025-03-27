from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url1 = ('https://parsinger.ru/selenium/5.5/5/1.html')
url2 = ('https://parsinger.ru/selenium/5.5/5/test/test.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)
container = browser.find_element(By.ID, 'main-container')
big_boxes = container.find_elements(By.XPATH, './div')
print(f'{len(big_boxes)=}')
for big_box in big_boxes:
    big_box_hex = big_box.find_element(By.TAG_NAME, 'span').text
    print(f'{big_box_hex=}')

    # select from list
    big_box.find_element(By.XPATH, f".//option[contains(text(), '{big_box_hex}')]").click()
    time.sleep(0.2)

     # press_button, find by attribute
    # / html / body / div / div[1] / div / button[1]
    big_box.find_element(By.XPATH, f"./ div / button[@data-hex='{big_box_hex}']").click()
    time.sleep(0.2)

    # mark checkbox
    big_box.find_element(By.XPATH, f"./ input [@type='checkbox']").click()
    time.sleep(0.2)

    # mark checkbox
    big_box.find_element(By.XPATH, f"./ input [@type='text']").send_keys(big_box_hex)
    time.sleep(0.2)

    # Push button with teext
    big_box.find_element(By.XPATH, f"./ button[contains(text(), 'Проверить')]").click()
browser.find_element(By.XPATH, f".// button[contains(text(), 'Проверить все элементы')]").click()

time.sleep(15)
browser.quit()

