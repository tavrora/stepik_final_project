from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_BASKET  = (By.CSS_SELECTOR, ".btn-add-to-basket")

    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    MASSAGE_ADDED_BASKET  = (By.CSS_SELECTOR, "div.alertinner")
    NAME_FROM_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")

    COST_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    MASSAGE_COST_BASKET  = (By.CSS_SELECTOR, ".alert-info .alertinner")
    COST_FROM_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")

    # MESSAGE_DISAPPEAR = (By.CSS_SELECTOR, "OLOLOL")

