import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_shopping_cart(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")

    assert button is not None, f"Button 'Add to cart' is not available"


