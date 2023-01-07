import string
import random

from forms.login_form import LoginForm
from utils.constants import Url, ERROR


class TestAuthorization:
    def test_authorization_empty(self, start_browser):
        page = start_browser
        login_page = LoginForm(page)
        login_page.fill_login_and_enter(username="", password="")
        current_page = login_page.current_page()
        assert current_page == Url.login_url, "Переход на страницу магазина без авторизации"
        assert login_page.check_exists_error(), "Не отображается ошибка авторизации "

    def test_authorization_succesfull_authorization(self, start_browser):
        page = start_browser
        login_page = LoginForm(page)
        login_page.fill_login_and_enter()
        current_page = login_page.current_page()
        assert current_page == Url.main_page_url

    def test_authorization_after_clear_value(self, start_browser):
        page = start_browser
        login_page = LoginForm(page)
        login_page.clear_password_login()
        login_page.fill_login_and_enter(username="", password="")
        current_page = login_page.current_page()
        assert not current_page == Url.main_page_url, "Переход на страницу магазина без авторизации"
        assert login_page.check_exists_error(), "Не отображается ошибка авторизации "

    def test_authorization_check_valid_login(self, start_browser):
        page = start_browser
        login_page = LoginForm(page)
        login_page.fill_login_and_enter(password="")
        current_page = login_page.current_page()
        text = login_page.check_text(ERROR.error_pass)
        assert text == "Epic sadface: Password is required"
        assert Url.login_url == current_page, "Переход на страницу магазина без авторизации"

    def test_authorization_check_valid_password(self, start_browser):
        page = start_browser
        login_page = LoginForm(page)
        # Попытка авторизации с валидным паролем и пустым логином
        login_page.fill_login_and_enter(username="")
        assert login_page.check_exists_error(), "Не отображается ошибка авторизации "
        text = login_page.check_text(ERROR.error_name)
        assert text == "Epic sadface: Username is required"
        current_url = login_page.current_page()
        assert Url.login_url == current_url, "Переход на страницу магазина без авторизации"

    def test_authorization_check_invalid_login_password(self, start_browser):
        page = start_browser
        login_page = LoginForm(page)
        # Попытка авторизации с невалидными логином, паролем
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        random_pass = ''.join(random.choices(string.digits, k=5))
        login_page.fill_login_and_enter(username=random_name, password=random_pass)
        current_url = login_page.current_page()
        assert login_page.check_exists_error(), "Не отображается ошибка авторизации "
        text = login_page.check_text(ERROR.invalid_name_pass)
        assert text == "Epic sadface: Username and password do not match any user in this service"
        assert Url.login_url == current_url, "Переход на страницу магазина без авторизации"