# from forms.login_form import BasePage
from playwright.sync_api import Page, expect, Playwright


from forms.play import BasePage


class ShopForm(BasePage):
    def add_basket(self):
        add_backet = self.page.locator('[id="add-to-cart-sauce-labs-backpack"]')
        add_backet.click()
        return True

    def check_exists_item_bucket(self):
        try:
            locator = self.page.locator(".shopping_cart_badge")
            expect(locator).to_be_visible()
        except Exception:
            return False
        return True

    def check_exists_item(self):
        try:
            locator = self.page.locator(".inventory_item_name")
            expect(locator).to_be_visible()
        except Exception:
            return False
        return True

    def exist_basket_icon(self):
        try:
            locator = self.page.locator(".shopping_cart_link")
            expect(locator).to_be_visible()
        except Exception:
            return False
        return True

    def burger_icon(self):
        try:
            locator = self.page.locator("[id='react-burger-menu-btn']")
            expect(locator).to_be_visible()
        except Exception:
            return False
        return True

    def check_main_menu(self):
        try:
            locator = self.page.locator(".bm-menu")
            expect(locator).to_be_visible()
        except Exception:
            return False
        return True

    def check_title(self):
        try:
            locator = self.page.locator(".title")
            expect(locator).to_be_visible()
        except Exception:
            return False
        return locator.inner_text()

    def click_burger(self):
        go_burger = self.page.locator("[id='react-burger-menu-btn']")
        go_burger.click()

    def click_close_burger(self):
        go_close_burger = self.page.locator(".bm-cross-button")
        go_close_burger.click()

    def click_basket(self):
        go_bucket = self.page.locator('.shopping_cart_link')
        go_bucket.click()

    def click_sort_cont(self):
        go_sort = self.page.locator(".product_sort_container")
        go_sort.click()
        # go_sort_low = self.page.locator("[value='lohi']")
        # go_sort_low.click()
    # def check_sorted_list(self):
    #     sorted_list = self.page.locator(".product_sort_container", has=self.page.locator("option"))
    #     sorted_list.count()

    def check_min_price(self):
        list = []
        results = self.page.locator(".inventory_item_price", has_text="$").all_inner_texts()
        for i in results:
            list.append(i)
        new_list = sorted(list)

    def click_remove_btn(self):
        remove = self.page.locator('[id="remove-sauce-labs-backpack"]')
        remove.click()
        return True

    def check_icon_link(self):
        try:
            locator = self.page.locator(".social")
            expect(locator).to_be_visible()
        except Exception:
            return False
        return True

    def twitter_btn(self):
        locator = self.page.locator('[href="https://twitter.com/saucelabs"]')
        expect(locator).to_be_visible()
        return True

    def facebook_btn(self):
        locator = self.page.locator('[href="https://www.facebook.com/saucelabs"]')
        expect(locator).to_be_visible()
        return True

    def linkedin_btn(self):
        locator = self.page.locator('[href="https://www.linkedin.com/company/sauce-labs/"]')
        expect(locator).to_be_visible()
        return True

    def go_item(self):
        go_item = self.page.locator('[id="item_4_title_link"]')
        go_item.click()

    def check_price(self):
        element = self.page.locator(".inventory_item_price").first
        return element.inner_text()
