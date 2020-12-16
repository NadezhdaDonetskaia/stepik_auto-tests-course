import os
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # код, который заполняет обязательные поля
    first_name = browser.find_element_by_xpath('//*[contains(text(), "First name*")]/following::input[1]')
    first_name.send_keys("Name")
    last_name = browser.find_element_by_xpath('//*[contains(text(), "Last name*")]/following::input[1]')
    last_name.send_keys("Last Name")
    mail = browser.find_element_by_css_selector("input[name='email']")
    mail.send_keys("asd@kja")

    input_file = browser.find_element_by_css_selector("input[type='file']")
    current_dir = os.path.abspath(os.path.dirname('lesson8_step8.py'))
    file_path = os.path.join(current_dir, 'lesson8_step8.txt')
    print(file_path)
    input_file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()





"""

current_dir = os.path.abspath(os.path.dirname('lesson6_step8.py'))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'lesson6_step8.py')           # добавляем к этому пути имя файла
#element.send_keys(file_path)
print(current_dir)
print(file_path)
print(os.path.abspath('lesson6_step8.py'))
"""

