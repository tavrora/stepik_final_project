from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    FIELD_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    FIELD_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    FIELD_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    BUTTON_ADD_BASKET  = (By.CSS_SELECTOR, ".btn-add-to-basket")

    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    MASSAGE_ADDED_BASKET  = (By.CSS_SELECTOR, "div.alertinner")
    NAME_FROM_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong")

    COST_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    MASSAGE_COST_BASKET  = (By.CSS_SELECTOR, ".alert-info .alertinner")
    COST_FROM_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")

class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini .btn-default")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_FILLING = (By.CSS_SELECTOR, "#basket_formset")