from selenium import webdriver
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url1 = ('https://parsinger.ru/selenium/8/8.1.2/index.html')
final_number = 0
descriptors = []

with webdriver.Chrome() as browser:
    browser.get(url1)
    time.sleep(0.5)
    code_links = browser.find_elements(By.XPATH, "//div[@class='code-links']/a")
    descriptor_0 = browser.current_window_handle
    for code_link in code_links:
        link_ref = code_link.get_attribute('href')
        print(f'{link_ref=}')
        browser.switch_to.new_window("tab")
        browser.get(link_ref)
        # time.sleep(0.2)
        descriptors.append(browser.current_window_handle )
        browser.switch_to.window(descriptor_0)
    # descriptors = browser.window_handles
    print(f'{descriptors=}')
    for descriptor in descriptors:
        browser.switch_to.window(descriptor)
        numbers = browser.find_elements(By.XPATH, "//div[@class='number']")
        while not numbers:
            numbers = browser.find_elements(By.XPATH, "//div[@class='number']")
        for number in numbers:
            print(f'{number.text=}')
            final_number += int(number.text)
            print(f'{final_number=}')
            # browser.switch_to.window(descriptor_0)
            # time.sleep(2)

            # print(f'{code_link.text=}')
    browser.switch_to.window(descriptor_0)
    browser.find_element(By.ID, "sumInput").send_keys(final_number)
    browser.find_element(By.XPATH, "//button[@id='checkButton']").click()
    time.sleep(10)
    pass_text = browser.find_element(By.ID, 'passwordDisplay').text
    print(f'{pass_text=}')



