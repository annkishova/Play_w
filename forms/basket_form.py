from forms.login_form import BasePage
from playwright.sync_api import Page, expect


class BasketForm(BasePage):
    def click_basket(self, page: Page):
        go_bucket = page.locator('.shopping_cart_link')
        go_bucket.click()

    def click_checkout(self, page: Page):
        checkout = page.locator('[id="checkout"]')
        checkout.click()

    def click_remove_btn(self, page: Page):
        remove = page.locator('[id="remove-sauce-labs-backpack"]')
        remove.click()

    def click_continue_btn(self, page: Page):
        continue_btn = page.locator('[id="continue-shopping"]')
        continue_btn.click()

    def go_card_item(self, page: Page):
        go_card = page.locator('[id="item_4_title_link"]')
        go_card.click()

    def exist_basket_icon(self, page: Page):
        locator = page.locator(".shopping_cart_link")
        expect(locator).to_be_visible()

    def burger_icon(self, page: Page):
        locator = page.locator("[id='react-burger-menu-btn']")
        expect(locator).to_be_visible()

    """    
    def check_price(self, value: str):
        text = self.driver.find_element(*self.element.ITEM_PRICE).text.replace(" ", "")
        value = list(i for i in text)
        return str(value[-1])
        
    def check_exists_basket(self):
        try:
            self.driver.find_element(*self.element.SHOPPING_CONT)
        except NoSuchElementException:
            return False
        return True

    def check_exists_item(self):
        try:
            self.driver.find_element(*self.element.ITEM)
        except NoSuchElementException:
            return False
        return True
        """
