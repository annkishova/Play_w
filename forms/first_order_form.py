# from forms.login_form import BasePage
from playwright.sync_api import Page, expect
from forms.play import BasePage


class FirstOrderForm(BasePage):
    def continue_btn(self):
        continue_btn = self.page.locator('[id="continue"]')
        continue_btn.click()

    def cancel_btn(self):
        cancel_btn = self.page.locator('[name="cancel"]')
        cancel_btn.click()

    def check_title_form(self):
        locator = self.page.get_by_title("class='title'")
        expect(locator).to_contain_text("Checkout: Your Information")
        return locator.inner_text()

    def cancel_button(self):
        cancel_button = self.page.locator('[name="cancel"]')
        cancel_button.click()

    def fill_first_name(self, first_name: str):
        fill_first_name = self.page.locator('[id="first-name"]')
        fill_first_name.fill(first_name)

    def first_name(self):
        try:
            locator = self.page.locator('[id="first-name"]')
            expect(locator).to_be_visible()
        except Exception:
            return False
        return locator.inner_text()

    def fill_last_name(self, last_name: str):
        fill_last_name = self.page.locator('[id="last-name"]')
        fill_last_name.fill(last_name)

    def last_name(self):
        try:
            locator = self.page.locator('[id="last-name"]')
            expect(locator).to_be_visible()
        except Exception:
            return False
        return locator.inner_text()

    def fill_postal_code(self, postal_code: str):
        fill_postal_code = self.page.locator('[id="postal-code"]')
        fill_postal_code.fill(postal_code)

    def postal_code(self):
        try:
            locator = self.page.locator('[id="postal-code"]')
            expect(locator).to_be_visible()
        except Exception:
            return False
        return locator.inner_text()

    def exist_basket_icon(self):
        locator = self.page.locator(".shopping_cart_link")
        expect(locator).to_be_visible()

    def burger_icon(self):
        locator = self.page.locator("[id='react-burger-menu-btn']")
        expect(locator).to_be_visible()

    def check_exists_checkout_info(self):
        try:
            locator = self.page.locator(".checkout_info")
            expect(locator).to_be_visible()
        except Exception:
            return False
        return True

    def check_exists_error(self):
        try:
            locator = self.page.locator(".error-message-container")
            expect(locator).to_be_visible()
        except Exception:
            return False
        return locator.inner_text()

    def clear_aria(self, elem, empty=""):
        aria = self.page.locator(f'{elem}')
        aria.fill(empty)
