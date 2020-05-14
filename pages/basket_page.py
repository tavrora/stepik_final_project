from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    """Class for working with the basket (inherited from the base)"""
    # в корзине нет товаров
    def should_be_no_products_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FILLING), \
            "Basket is not empty"

    # есть текст о том, что корзина пуста
    def should_be_text_that_basket_is_empty(self):
        basket_empty_message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        # оперделяем текущий язык
        language_curr = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        # заводим словарь с переводами сообщения
        languages_dict = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en": "Your basket is empty.",
            "en-US": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",
        }
        # находим значение по ключу
        message_lang = languages_dict.get(language_curr)
        print(f"\n{message_lang} =============> {basket_empty_message.text}\n")
        assert message_lang in basket_empty_message.text, "No text that the basket is empty"


