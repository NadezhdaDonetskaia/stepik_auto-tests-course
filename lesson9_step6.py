from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    accept1 = browser.find_element_by_css_selector("button.btn")
    accept1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)
    inp = browser.find_element_by_id("answer")
    inp.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
