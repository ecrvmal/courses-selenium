from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/7/7.5/index.html')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(0.1)

actions = ActionChains(browser)
final_summ : int = 0
num_cards: int = 0
scroll_cards = True
cards: list[WebElement] = []

while scroll_cards:
    cards = browser.find_elements(By.XPATH, "//div[@class='card']")

    browser.execute_script("return arguments[0].scrollIntoView(true);", cards[-1])
    time.sleep(1)
    browser.execute_script("window.scrollBy(0, 500)")
    time.sleep(1)
    print('scroll down')

    print(f'{len(cards)=}')
    if len(cards) > num_cards:
        num_cards = len(cards)
    else:
        scroll_cards = False

for card in cards:
    browser.execute_script("return arguments[0].scrollIntoView(true);", card)
    card.find_element(By.XPATH, ".//span[@class='like-btn']").click()
    value = card.find_element(By.XPATH, ".//div[@class='number-wrapper']").text
    final_summ += int(value)

print(f'{final_summ=}')

time.sleep(2)
browser.quit()



