from forms.play import BasePage
from playwright.sync_api import Page, expect


class ItemFormT(BasePage):
    def add_basket(self):
        add_backet = self.page.locator('.btn_primary')
        add_backet.click()

    def remove_basket(self):
        add_backet = self.page.locator('.btn_secondary.btn_small')
        add_backet.click()

    def check_price(self):
        element = self.page.locator(".inventory_item_price").first
        return element.inner_text()

    def check_exists_price_of_item(self):
        locator = self.page.locator(".inventory_details_price")
        expect(locator).to_be_visible()
        return True

    def check_exists_name_of_item(self):
        locator = self.page.locator(".inventory_details_name")
        expect(locator).to_be_visible()
        return True

    def check_exists_details_of_item(self):
        locator = self.page.locator(".inventory_details_desc")
        expect(locator).to_be_visible()
        return True

    def check_exists_image_of_item(self):
        locator = self.page.locator(".inventory_details_img")
        expect(locator).to_be_visible()
        return True

    def check_exists_item_bucket(self):
        try:
            locator = self.page.locator(".shopping_cart_badge")
            expect(locator).to_be_visible()
        except Exception:
            return False
        return locator.inner_text()


