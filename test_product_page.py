import pytest
from .pages.product_page import ProductPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.skip
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
def  test_guest_can_add_product_to_basket(browser, link):
    # открыть страницу
    product_page = ProductPage(browser, link)
    product_page.open()
    # добавить товар в корзину add_to_basket
    product_page.add_to_basket()
    # пройти проверку в алерте методом solve_quiz_and_get_code()
    product_page.solve_quiz_and_get_code()
    # есть сообщение, что товар добавлен в корзину
    # и название товара в сообщении совпадает с названием добавленного
    product_page.should_be_message_product_add_basket_and_name_match()
    # есть сообщение со стоимостью корзины
    # и стоимость совпадает с ценой товара
    product_page.should_be_message_cost_basket_and_cost_match()

@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    # Открываем страницу товара
    product_page = ProductPage(browser, link)
    product_page.open()
    # Добавляем товар в корзину
    product_page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()

@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    # Открываем страницу товара
    product_page = ProductPage(browser, link)
    product_page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()

@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    # Открываем страницу товара
    product_page = ProductPage(browser, link)
    product_page.open()
    # Добавляем товар в корзину
    product_page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page.should_be_message_disappeared()