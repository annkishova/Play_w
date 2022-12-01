from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import playwright

from forms.login_form import LoginForm
from utils.constants import Url
from playwright.async_api import Page, expect


def test_authorization_succesfull_authorization():
    login_form = LoginForm()
    login_form.fill_login_and_enter()
    #current_url = page.url
    expect().to_have_url(Url.main_page_url)
