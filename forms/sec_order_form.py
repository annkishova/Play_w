from forms.play import BasePage
from playwright.sync_api import Page, expect


class SecOrderForm(BasePage):
    def price_of_item(self):
        locator = self.page.locator(".inventory_item_price")
        expect(locator).to_be_visible()
        return locator.inner_text()

    def name_of_item(self):
        locator = self.page.locator(".inventory_item_name")
        expect(locator).to_be_visible()
        return locator.inner_text()

    def details_of_item(self):
        locator = self.page.locator(".inventory_item_desc")
        expect(locator).to_be_visible()
        return locator.inner_text()

    def finish_btn(self):
        finish_btn = self.page.locator('[id="finish"]')
        finish_btn.click()

    def cancel_button(self):
        cancel_button = self.page.locator('[name="cancel"]')
        cancel_button.click()

    def exist_basket_icon(self):
        locator = self.page.locator(".shopping_cart_link")
        expect(locator).to_be_visible()

    def burger_icon(self):
        locator = self.page.locator("[id='react-burger-menu-btn']")
        expect(locator).to_be_visible()

    def check_title_form(self):
        locator = self.page.get_by_title("class='title'")
        expect(locator).to_contain_text("Checkout: Overview")
        return locator.inner_text()

    def check_subtotal(self):
        locator = self.page.locator(".summary_subtotal_label")
        expect(locator).to_be_visible()
        return True

    def check_tax(self):
        locator = self.page.locator(".summary_tax_label")
        expect(locator).to_be_visible()
        return True

    def check_total(self):
        locator = self.page.locator(".summary_total_label")
        expect(locator).to_be_visible()
        return True
