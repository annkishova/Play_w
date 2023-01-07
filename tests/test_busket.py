from forms.basket_form import BasketForm
from forms.shop_form import ShopForm
from utils.constants import Url


class TestBasket:
    def test_open_basket(self, fill_login_and_enter):
        #Авторизация
        page = fill_login_and_enter
        shop = ShopForm(page)
        assert shop.exist_basket_icon(), "Корзина не отображается"
        shop.click_basket()
        current_page = shop.current_page()
        assert Url.basket_page_url == current_page, "Форма корзины не открылась"

    # Тест на добавление в корзину + проверка описания и цены + переход в карточку товара
    def test_add_to_basket(self, fill_login_and_enter):
        #Авторизация
        page = fill_login_and_enter
        shop = ShopForm(page)
        shop.add_basket()
        assert shop.check_exists_item_bucket(), "Товар не добавлен в корзину"
        assert shop.check_exists_item(), "В корзине пусто"
        basket_form = BasketForm(page)
        price_card = basket_form.check_price()
        basket_form.click_basket()
        price_basket = basket_form.check_price()
        assert price_card == price_basket, "Цена товара в корзине и осн странице разные"
        basket_form.go_card_item()
        current_url = basket_form.current_page()
        assert Url.basket_page_url != current_url, "Не выполнен переход к карточке товара"

    def test_check_price(self, fill_login_and_enter):
        #Авторизация
        page = fill_login_and_enter
        shop = ShopForm(page)
        shop.add_basket()
        basket = BasketForm(page)
        price = basket.check_price()
        basket.click_basket()
        price_basket = basket.check_price()
        assert price == price_basket, "Цена товара в корзине и осн странице разные"

    def test_go_to_item_card(self, fill_login_and_enter):
        #Авторизация
        page = fill_login_and_enter
        shop = ShopForm(page)
        shop.add_basket()
        basket = BasketForm(page)
        basket.click_basket()
        basket.go_card_item()
        current_url = basket.current_page()
        assert Url.basket_page_url != current_url, "Не выполнен переход к карточке товара"

    # Тест на удаление из корзины
    def test_delete_item_from_basket(self, fill_login_and_enter):
        #Авторизация
        page = fill_login_and_enter
        shop = ShopForm(page)
        shop.add_basket()
        basket = BasketForm(page)
        basket.click_basket()
        assert basket.check_exists_item(), "В корзине нет товаров"
        basket.click_remove_btn()
        assert not basket.check_exists_item(), "В корзине есть товары"

    #Тест на переход из корзины к оформлению заказа
    def test_checkout_from_basket(self, fill_login_and_enter):
        #Авторизация
        page = fill_login_and_enter
        basket = BasketForm(page)
        basket.click_basket()
        current_url = basket.current_page()
        basket.click_checkout()
        assert Url.checkout != current_url, "Не выполнен переход к оформлению заказа"

    # Продолжение шопинга
    def test_continue_shopping(self, fill_login_and_enter):
        #Авторизация
        page = fill_login_and_enter
        basket = BasketForm(page)
        basket.click_basket()
        current_url = basket.current_page()
        basket.click_continue_btn()
        assert Url.main_page_url != current_url, "Не работает переход к продолжению покупок"
