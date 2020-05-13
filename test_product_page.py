from .pages.product_page import ProductPage

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def  test_guest_can_add_product_to_basket(browser):
    # открыть страницу
    product_page = ProductPage(browser, link)
    product_page.open()
    # добавить товар в корзину add_to_basket (и пройти алерт-вход)
    product_page.add_to_basket()
    # есть сообщение, что товар добавлен в корзину
    # и название товара в сообщении совпадает с названием добавленного
    product_page.should_be_message_product_add_basket_and_name_match()
    # есть сообщение со стоимостью корзины
    # и стоимость совпадает с ценой товара
    product_page.should_be_message_cost_basket_and_cost_match()
