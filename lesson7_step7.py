from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    chest = browser.find_element_by_css_selector('img')
    x = chest.get_attribute("valuex")
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
