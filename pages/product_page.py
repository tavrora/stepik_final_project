from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Class for working with the product (inherited from the base)"""
    def add_to_basket(self):
        # нажать кнопку "Добавить в корзину"
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET)
        button.click()
        # пройти проверку в алерте методом solve_quiz_and_get_code()
        self.solve_quiz_and_get_code()

    def should_be_message_product_add_basket_and_name_match(self):
        # есть сообщение, что товар добавлен в корзину
        assert self.browser.find_element(*ProductPageLocators.MASSAGE_ADDED_BASKET), \
            "Тhere is no message about the successful addition to the basket"
        # название товара в сообщении совпадает с названием добавленного
        name_product_element = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product = name_product_element.text
        name_from_message_element = self.browser.find_element(*ProductPageLocators.NAME_FROM_MESSAGE)
        name_from_message = name_from_message_element.text
        print(f"\nname_product: {name_product} ============= name_from_message: {name_from_message}\n")
        assert name_product == name_from_message, \
            "Item name in the message does not match the name of the item added"

    def  should_be_message_cost_basket_and_cost_match(self):
        # есть сообщение со стоимостью корзины
        assert self.browser.find_element(*ProductPageLocators.MASSAGE_COST_BASKET), \
            "There is no message with the cost of the basket"
        # стоимость совпадает с ценой товара
        cost_product_element = self.browser.find_element(*ProductPageLocators.COST_PRODUCT)
        cost_product = cost_product_element.text  # == 9,99&nbsp;£
        cost_from_message_element = self.browser.find_element(*ProductPageLocators.COST_FROM_MESSAGE)
        cost_from_message = cost_from_message_element.text  # == 19,98&nbsp;£
        print(f"cost_product: {cost_product} ============= cost_from_message: {cost_from_message}\n\n")
        assert cost_product == cost_from_message, \
            "Value does not match product price"