import pytest
import time
import random
import string

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"

@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # открыть страницу регистрации
        login_url = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, login_url)
        login_page.open()
        # зарегистрировать нового пользователя
        email = str(time.time()) + "@fakemail.org"
        password = str(random.random())
        login_page.register_new_user(email, password)
        # проверить, что пользователь залогинен
        login_page.should_be_authorized_user()

    # @pytest.mark.parametrize('link',
    #                          ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    #                           pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    #                                        marks=pytest.mark.xfail),
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def  test_user_can_add_product_to_basket(self, browser): #link
        # открыть страницу
        product_page = ProductPage(browser, link)
        product_page.open()
        # добавить товар в корзину add_to_basket
        product_page.add_to_basket()
        # пройти проверку в алерте методом solve_quiz_and_get_code()
        # product_page.solve_quiz_and_get_code()
        # есть сообщение, что товар добавлен в корзину
        # и название товара в сообщении совпадает с названием добавленного
        product_page.should_be_message_product_add_basket_and_name_match()
        # есть сообщение со стоимостью корзины
        # и стоимость совпадает с ценой товара
        product_page.should_be_message_cost_basket_and_cost_match()

    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Открываем страницу товара
        product_page = ProductPage(browser, link)
        product_page.open()
        # Добавляем товар в корзину
        product_page.add_to_basket()
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        time.sleep(10)
        product_page.should_be_success_message()

def test_guest_cant_see_success_message(browser):
    # Открываем страницу товара
    product_page = ProductPage(browser, link)
    product_page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    # Открываем страницу товара
    product_page = ProductPage(browser, link)
    product_page.open()
    # Добавляем товар в корзину
    product_page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page.should_be_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()

@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    product_page = ProductPage(browser, link)
    product_page.open()
    # Переходит в корзину по кнопке в шапке сайта
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    # Ожидаем, что в корзине нет товаров
    basket_page.should_be_no_products_in_the_basket()
    # Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_text_that_basket_is_empty()
