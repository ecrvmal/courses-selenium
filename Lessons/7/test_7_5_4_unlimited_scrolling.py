from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/infiniti_scroll_3/')

browser = webdriver.Chrome()
browser.get(url1)
time.sleep(1)

time.sleep(2)
final_summ: int = 0
for i in range(1,6):
    actionChains = ActionChains(browser)
    scrolling_more : bool = True

    while scrolling_more:
        boxes = browser.find_elements(By.XPATH, f"//div[@id='scroll-container_{i}'] / span")
        last_box = boxes[-1]
        for box in boxes:
            if box.get_attribute('class') == 'last-of-list':
                scrolling_more = False
        actionChains.click(last_box).scroll_by_amount(0, 200).perform()

    boxes = browser.find_elements(By.XPATH, f"//div[@id='scroll-container_{i}'] / span")
    for box in boxes:
        final_summ += int(box.text)
print(f'{final_summ=}')

time.sleep(5)
browser.quit()



