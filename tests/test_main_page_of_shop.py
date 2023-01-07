from forms.shop_form import ShopForm
from utils.constants import Url


class TestShopPage:
    def test_view_main_page(self, fill_login_and_enter):
        page = fill_login_and_enter
        shop = ShopForm(page)
        title_text = shop.check_title()
        assert title_text == "PRODUCTS"
        assert shop.check_exists_item(), "Товар не отображается"
        assert shop.exist_basket_icon(), "Иконка корзины не отображается"
        assert shop.burger_icon(), "Нет иконки бургер"
        current_page = shop.current_page()
        assert Url.main_page_url == current_page, "Форма корзины не открылась"

    def test_burger_menu(self, fill_login_and_enter):
        page = fill_login_and_enter
        shop = ShopForm(page)
        shop.click_burger()
        assert shop.check_main_menu(), "Не открылось главное меню"
        shop.click_close_burger()
        assert not shop.check_main_menu(), "Главное меню не закрылось"

    def test_sorted(self, fill_login_and_enter):
        page = fill_login_and_enter
        shop = ShopForm(page)
        shop.click_sort_cont()
        # shop.check_min_price()

    def test_button_on_item(self, fill_login_and_enter):
        page = fill_login_and_enter
        shop = ShopForm(page)
        assert shop.add_basket(), "Нет кнопки добавить в корзину"
        assert shop.click_remove_btn(), "Нет кнопки удалить из корзины"

    def test_icons_on_page(self, fill_login_and_enter):
        page = fill_login_and_enter
        shop = ShopForm(page)
        assert shop.check_icon_link(), "Иконки соцсетей не отображаются"
        assert shop.twitter_btn(), "Нет ссылки на twitter"
        assert shop.facebook_btn(), "Нет ссылки на facebook"
        assert shop.linkedin_btn(), "Нет ссылки на linkedin"
