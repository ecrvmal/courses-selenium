import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

try:
    # Открываем страницу
    url = 'http://parsinger.ru/2.1/DOM/index2.html'
    driver.get(url)

    # Ищем элемент по ID "text777"
    target_element = driver.find_element(By.ID, "text777")

    # Извлекаем и выводим текст
    extracted_text = target_element.text
    print(f"Извлеченный текст: {extracted_text}")
    time.sleep(1)


finally:
    driver.quit()  # Закрываем браузер