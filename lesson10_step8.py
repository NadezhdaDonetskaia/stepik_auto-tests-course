from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()


try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
    )
    button1 = browser.find_element_by_id('book')
    button1.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)

    button2 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'solve'))
    )

    button2.click()

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
