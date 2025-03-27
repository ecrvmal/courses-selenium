from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/5.7/4/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)

actionChains = ActionChains(browser)
boxes = browser.find_elements(By.XPATH, "//div[@class='item']")
final_summ : int = 0
for box in boxes:
    box.find_element(By.XPATH, "./input[@type='checkbox']").click()
    time.sleep(0.1)
    the_sum = box.find_element(By.XPATH, ".//span[contains(@id, 'result')]").text
    print(f'{the_sum=}')
    if the_sum != "":
        final_summ += int(the_sum)

print(f'{final_summ=}')
time.sleep(2)
browser.quit()



