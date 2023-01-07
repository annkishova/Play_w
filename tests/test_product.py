from forms.backpack_form import ItemFormBack
from forms.shop_form import ShopForm
from utils.constants import Url


class TestProduct:
    def test_go_product_page(self, fill_login_and_enter):
        page = fill_login_and_enter
        shop = ShopForm(page)
        shop.go_item()
        current_page = shop.current_page()
        assert Url.product_page == current_page, "Форма товара не открылась"

    def test_view_product_page(self, fill_login_and_enter):
        page = fill_login_and_enter
        shop = ShopForm(page)
        shop.go_item()
        product = ItemFormBack(page)
        assert product.check_exists_details_of_item(), "Нет описания товара"
        assert product.check_exists_price_of_item(), "Нет цены товара"
        assert product.check_exists_name_of_item(), "Нет имени товара"
        assert product.check_exists_image_of_item(), "Нет изображения товара"

    def test_add_product_page(self, fill_login_and_enter):
        page = fill_login_and_enter
        shop = ShopForm(page)
        shop.go_item()
        product = ItemFormBack(page)
        count = product.check_exists_item_bucket()
        product.add_basket()
        assert product.check_exists_item_bucket() == count+1 , "Товар не добавлен в корзину"
        product.remove_basket()
        assert product.check_exists_item_bucket() == count, "Товар не удален из корзины"

    def test_back_from_product_page(self, fill_login_and_enter):
        page = fill_login_and_enter
        shop = ShopForm(page)
        shop.go_item()
        product = ItemFormBack(page)
        current_page = shop.current_page()
        assert product.back_btn(), "Нет кнопки возврата назад"
        assert current_page == Url.main_page_url, "Открыта не главная страница магазина"

    def test_price_product(self, fill_login_and_enter):
        page = fill_login_and_enter
        shop = ShopForm(page)
        price_main = shop.check_price()
        shop.go_item()
        product = ItemFormBack(page)
        price_card = product.check_price()
        assert price_main == price_card, "Цена товара в карточке и осн странице разные"
