from pytest import fixture
from playwright.sync_api import sync_playwright
# from playwright.sync_api import sync_playwright
from forms.play import BaseClass
# from playwright.sync_api import Playwright, Locator, Page
# from forms.login_form import LoginForm


# @fixture
# def get_playwright():
#     with sync_playwright() as playwright:
#         yield playwright
#
#
# @fixture
# def app(get_playwright) -> LoginForm:
#     app = Play(get_playwright)
#     yield app
#     app.close()
# @fixture()
# def browser():
#     driver = playwright.chromium.launch(headless=False)
#     yield driver
#     driver.close()
@fixture()
def get_playwright():
    with sync_playwright() as play:
        yield play


@fixture()
def app(get_playwright):
    app = BaseClass(get_playwright, base_url="https://www.saucedemo.com")
    app.goto()
    yield app
    app.close()
