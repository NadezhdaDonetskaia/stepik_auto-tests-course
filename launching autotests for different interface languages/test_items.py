
def test_button_to_be(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = chrome.find_element_by_css_selector('button.btn-primary')
    assert button.is_displayed() == True, "Кнопки добавить в корзину нет на экране"