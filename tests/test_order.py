import string
import random

from forms.basket_form import BasketForm
from forms.sec_order_form import SecOrderForm
from forms.first_order_form import FirstOrderForm
from forms.complete_order_form import CompleteOrderForm
from utils.constants import Url, ERROR


class TestOrder:
    def test_first_order_form_view(self, add_basket):
        page = add_basket
        info = FirstOrderForm(page)
        assert info.check_exists_checkout_info(), "Нет формы информации"
        title = info.check_title_form()
        assert title == "Checkout: Your Information", "Открыта другая форма"

    def test_first_order_form_invalid_value(self, add_basket):
        # Заполнить не все поля и продолжить
        page = add_basket
        info = FirstOrderForm(page)
        info.fill_first_name(random.choices(string.ascii_letters + string.digits, k=5))
        info.continue_btn()
        assert info.check_exists_error() == ERROR.order_first_form_lname, "Не отображается ошибка формы"
        info.clear_aria("[id='first-name']")
        info.continue_btn()
        assert info.check_exists_error() == ERROR.order_first_form_fname, "Не отображается ошибка формы"

    def test_cancel_first_order_form(self, add_basket):
        page = add_basket
        info = FirstOrderForm(page)
        first = info.fill_first_name(random.choices(string.ascii_letters + string.digits, k=5))
        last = info.fill_last_name(random.choices(string.ascii_letters + string.digits, k=5))
        postal = info.fill_postal_code(random.choices(string.ascii_letters + string.digits, k=5))
        info.cancel_btn()
        assert info.current_page() == Url.basket_page_url, "Не страница корзины"
        basket_form = BasketForm(page)
        basket_form.click_checkout()
        assert not info.first_name() == first, "Поле заполнено"
        assert not info.last_name() == last, "Поле заполнено"
        assert not info.postal_code() == postal, "Поле заполнено"

    def test_first_order_form_value(self, add_basket):
        page = add_basket
        info = FirstOrderForm(page)
        info.fill_first_name(random.choices(string.ascii_letters + string.digits, k=5))
        info.fill_last_name(random.choices(string.ascii_letters + string.digits, k=5))
        info.fill_postal_code(random.choices(string.ascii_letters + string.digits, k=5))
        info.continue_btn()
        overview = SecOrderForm(page)
        assert overview.current_page() == Url.checkout_two, "Не страница 2 шага заказа"
        assert overview.check_title_form() == "Checkout: Overview", "Не открыта вторая страница оформления заказа"

    def test_second_order_form_value(self, add_basket):
        page, name, description, price = add_basket
        info = FirstOrderForm(page)
        info.fill_first_name(random.choices(string.ascii_letters + string.digits, k=5))
        info.fill_last_name(random.choices(string.ascii_letters + string.digits, k=5))
        info.fill_postal_code(random.choices(string.ascii_letters + string.digits, k=5))
        info.continue_btn()
        overview = SecOrderForm(page)
        assert name == overview.name_of_item(), "Оформлен другой товар"
        assert description == overview.details_of_item(), "Другое описание товара"
        assert price == overview.price_of_item(), "Неверная цена"

    def test_second_order_form_back(self, add_basket):
        page = add_basket
        info = FirstOrderForm(page)
        info.fill_first_name(random.choices(string.ascii_letters + string.digits, k=5))
        info.fill_last_name(random.choices(string.ascii_letters + string.digits, k=5))
        info.fill_postal_code(random.choices(string.ascii_letters + string.digits, k=5))
        info.continue_btn()
        overview = SecOrderForm(page)
        overview.cancel_button()
        assert overview.current_page() == Url.checkout, "Не страница 1 шага заказа"

    def test_second_order_form_tax(self, add_basket):
        page, _, _, _ = add_basket
        info = FirstOrderForm(page)
        info.fill_first_name(random.choices(string.ascii_letters + string.digits, k=5))
        info.fill_last_name(random.choices(string.ascii_letters + string.digits, k=5))
        info.fill_postal_code(random.choices(string.ascii_letters + string.digits, k=5))
        info.continue_btn()
        overview = SecOrderForm(page)
        assert overview.check_subtotal(), "Нет промежуточного итога"
        assert overview.check_tax(), "Нет налога"
        assert overview.check_total(), "Нет итого"

    def test_final_order_form(self, add_basket):
        page = add_basket
        info = FirstOrderForm(page)
        info.fill_first_name(random.choices(string.ascii_letters + string.digits, k=5))
        info.fill_last_name(random.choices(string.ascii_letters + string.digits, k=5))
        info.fill_postal_code(random.choices(string.ascii_letters + string.digits, k=5))
        info.continue_btn()
        overview = SecOrderForm(page)
        overview.finish_btn()
        complete = CompleteOrderForm(page)
        assert complete.current_page() == Url.complete, "Заказ не завершен"
        assert complete.check_image_pony(), "Нет иконки пони"
        assert complete.check_title_form() == "Checkout: Complete!"
        assert complete.check_complete_form(), "Нет текста об оформленном заказе"
