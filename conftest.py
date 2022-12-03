from pytest import fixture

from forms.play import Browser


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
# @fixture()
# def get_playwright():
#     with sync_playwright() as play:
#         yield play
#
#
# @fixture()
# def app(get_playwright):
#     app = BaseClass()
#     # app.goto()
#     yield app
#     app.close()
@fixture()
def browser():
    browser = Browser()
    browser.start()
    yield browser.driver
    browser.stop()
