from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_css_selector('body div form h2 [id=num1]').text
    num2 = browser.find_element_by_css_selector('body div form h2 [id=num2]').text
    def sum(a, b):
        return(str(int(a)+int(b)))
    s = sum(num1, num2)
    answer = Select(browser.find_element_by_class_name('custom-select'))
    answer.select_by_visible_text(s)


    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()


finally:
    # успеваем скопировать код за 20 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
