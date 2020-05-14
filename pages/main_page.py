from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """Class for working with the main (inherited from the base)"""

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # def go_to_login_page(self):
    #     # log_link = self.browser.find_element(By.CSS_SELECTOR, "#registration_link")
    #     log_link = self.is_element_present(*MainPageLocators.LOGIN_LINK)
    #     #
    #     link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     link.click()
    #
    # def should_be_login_link(self):
    #     # assert self.browser.find_element(By.CSS_SELECTOR, "#registration_link"), "Login link is not presented"
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
