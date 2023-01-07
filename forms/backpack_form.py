from forms.play import BasePage
from playwright.sync_api import Page, expect


class ItemFormBack(BasePage):
    def add_basket(self):
        add_backet = self.page.locator('[id="add-to-cart-sauce-labs-backpack"]')
        add_backet.click()

    def check_exists_price_of_item(self):
        locator = self.page.locator(".inventory_details_price")
        expect(locator).to_be_visible()

    def check_exists_name_of_item(self):
        locator = self.page.locator(".inventory_details_name")
        expect(locator).to_be_visible()

    def check_exists_details_of_item(self):
        locator = self.page.locator(".inventory_details_desc")
        expect(locator).to_be_visible()

    def check_exists_image_of_item(self):
        locator = self.page.locator(".inventory_details_img")
        expect(locator).to_be_visible()

    def exist_basket_icon(self):
        locator = self.page.locator(".shopping_cart_link")
        expect(locator).to_be_visible()

    def burger_icon(self):
        locator = self.page.locator("[id='react-burger-menu-btn']")
        expect(locator).to_be_visible()

    def remove_basket(self):
        add_backet = self.page.locator('.btn_secondary.btn_small')
        add_backet.click()

    def check_price(self):
        element = self.page.locator(".inventory_item_price").first
        return element.inner_text()

    def check_exists_item_bucket(self):
        try:
            locator = self.page.locator(".shopping_cart_badge")
            expect(locator).to_be_visible()
        except Exception:
            return False
        return locator.inner_text()

    def back_btn(self):
        back_btn = self.page.locator('.btn_secondary.back')
        back_btn.click()
        return True
