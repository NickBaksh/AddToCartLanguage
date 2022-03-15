from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_btn_language_shopping_cart(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located
                                    ((By.CSS_SELECTOR, ".btn-add-to-basket")), "No such button: 'Add to cart'")
    assert button is not None, f"Button 'Add to cart' is not available"


