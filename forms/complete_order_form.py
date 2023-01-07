from forms.play import BasePage
from playwright.sync_api import Page, expect


class CompleteOrderForm(BasePage):
    def back_button(self):
        back_home_btn = self.page.locator('[id="back-to-products"]')
        back_home_btn.click()

    def check_image_pony(self):
        locator = self.page.locator(".pony_express")
        expect(locator).to_be_visible()
        return True

    def exist_basket_icon(self):
        locator = self.page.locator(".shopping_cart_link")
        expect(locator).to_be_visible()

    def burger_icon(self):
        locator = self.page.locator("[id='react-burger-menu-btn']")
        expect(locator).to_be_visible()

    def check_title_form(self):
        locator = self.page.get_by_title("class='title'")
        expect(locator).to_contain_text("Checkout: Complete!")
        return locator.inner_text()

    def check_complete_form(self):
        locator = self.page.get_by_title("class='complete-text'")
        expect(locator).to_contain_text("dispatched")
        return True
