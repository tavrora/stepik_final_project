import pytest
import time
import random

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"

@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Открыть страницу регистрации
        login_url = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, login_url)
        login_page.open()
        # Зарегистрировать нового пользователя
        email = str(time.time()) + "@fakemail.org"
        password = str(random.random())
        login_page.register_new_user(email, password)
        # Проверить, что пользователь залогинен
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                           marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def  test_user_can_add_product_to_basket(self, browser, link):
        # Открыть страницу
        product_page = ProductPage(browser, link)
        product_page.open()
        # Добавить товар в корзину add_to_basket
        product_page.add_to_basket()
        # Пройти проверку в алерте методом solve_quiz_and_get_code()
        product_page.solve_quiz_and_get_code()
        # Проверить, что есть сообщение о добавлении и название совпадает
        product_page.should_be_message_product_add_basket_and_name_match()
        # Проверить, что есть сообщение со стоимостью корзины и стоимость совпадает
        product_page.should_be_message_cost_basket_and_cost_match()

    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        # Проверить, что есть сообщение об успехе с помощью is_element_present
        product_page.should_be_success_message()


@pytest.mark.need_review
def  test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_be_message_product_add_basket_and_name_match()
    product_page.should_be_message_cost_basket_and_cost_match()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    # Проверить, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page.should_be_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()


@pytest.mark.basket
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    # Проверить, что в корзине нет товаров
    basket_page.should_be_no_products_in_the_basket()
    # Проверить, что есть текст о том что корзина пуста
    basket_page.should_be_text_that_basket_is_empty()
