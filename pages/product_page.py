from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Class for working with the product (inherited from the base)"""
    def add_to_basket(self):
        # Нажать кнопку "Добавить в корзину"
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button.click()

    def should_be_message_product_add_basket_and_name_match(self):
        # Есть сообщение, что товар добавлен в корзину
        assert self.browser.find_element(*ProductPageLocators.MASSAGE_ADDED_BASKET), \
            "Тhere is no message about the successful addition to the basket"
        # Название товара в сообщении совпадает с названием добавленного
        name_product_element = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product = name_product_element.text
        name_from_message_element = self.browser.find_element(*ProductPageLocators.NAME_FROM_MESSAGE)
        name_from_message = name_from_message_element.text
        print(f"\nname_product: {name_product} ============= name_from_message: {name_from_message}\n")
        assert name_product == name_from_message, \
            "Item name in the message does not match the name of the item added"

    def  should_be_message_cost_basket_and_cost_match(self):
        # Есть сообщение со стоимостью корзины
        assert self.browser.find_element(*ProductPageLocators.MASSAGE_COST_BASKET), \
            "There is no message with the cost of the basket"
        # Стоимость совпадает с ценой товара
        cost_product_element = self.browser.find_element(*ProductPageLocators.COST_PRODUCT)
        cost_product = cost_product_element.text
        cost_from_message_element = self.browser.find_element(*ProductPageLocators.COST_FROM_MESSAGE)
        cost_from_message = cost_from_message_element.text
        print(f"cost_product: {cost_product} ============= cost_from_message: {cost_from_message}\n\n")
        assert cost_product == cost_from_message, \
            "Value does not match product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MASSAGE_ADDED_BASKET), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.MASSAGE_ADDED_BASKET), \
            "Success message is not presented, but should be"

    def should_be_message_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.MASSAGE_ADDED_BASKET), \
            "The message did not disappear"