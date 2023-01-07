from forms.play import BasePage
from playwright.sync_api import Page, expect, Playwright


class BasketForm(BasePage):
    def click_basket(self):
        go_bucket = self.page.locator('.shopping_cart_link')
        go_bucket.click()

    def click_checkout(self):
        checkout = self.page.locator('[id="checkout"]')
        checkout.click()

    def click_remove_btn(self):
        remove = self.page.locator('[id="remove-sauce-labs-backpack"]')
        remove.click()

    def click_continue_btn(self):
        continue_btn = self.page.locator('[id="continue-shopping"]')
        continue_btn.click()

    def go_card_item(self):
        go_card = self.page.locator('[id="item_4_title_link"]')
        go_card.click()

    def exist_basket_icon(self):
        locator = self.page.locator(".shopping_cart_link")
        expect(locator).to_be_visible()

    def burger_icon(self):
        locator = self.page.locator("[id='react-burger-menu-btn']")
        expect(locator).to_be_visible()

    def check_price(self):
        element = self.page.locator(".inventory_item_price").first
        return element.inner_text()
        # text = self.page.locator(".inventory_item_price").text.replace(" ", "")
        # value = list(i for i in text)
        # return str(value[-1])

    def check_exists_basket(self):
        try:
            self.page.locator(".shopping_cart_link")
        except Exception:
            return False
        return True

    def name_item(self):
        try:
            locator = self.page.locator(".cart_item_label a")
        except Exception:
            return False
        return locator.inner_text()

    def description_item(self):
        try:
            locator = self.page.locator(".inventory_item_desc")
        except Exception:
            return False
        return locator.inner_text()

    def price_item(self):
        try:
            locator = self.page.locator(".item_pricebar")
        except Exception:
            return False
        return locator.inner_text()
