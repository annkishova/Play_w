import pytest
from playwright.sync_api import sync_playwright

from forms.basket_form import BasketForm
from forms.shop_form import ShopForm


@pytest.fixture(scope="function")
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture()
def start_browser(get_playwright):
    playwright = get_playwright
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")

    yield page

    page.close()
    context.close()
    browser.close()


@pytest.fixture(scope="function")
def fill_login_and_enter(start_browser, username="standard_user", password="secret_sauce"):
    page = start_browser
    page.locator('[id="user-name"]').fill(username)
    page.locator('[id="password"]').fill(password)
    page.locator('[id="login-button"]').click()

    yield page


@pytest.fixture(scope="function")
def add_basket(fill_login_and_enter):
    page = fill_login_and_enter
    shop = ShopForm(page)
    basket_form = BasketForm(page)
    if not shop.check_exists_item_bucket():
        shop.add_basket()
        # basket_form.click_remove_btn()
        # if basket_form.check_exists_item():
        #     basket_form.click_remove_btn()
        # else:
        #     basket_form.click_continue_btn()
    shop.click_basket()
    name = basket_form.name_item()
    description = basket_form.description_item()
    price = basket_form.price_item()
    basket_form.click_checkout()
    yield page, name, description, price
