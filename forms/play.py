from playwright.sync_api import Playwright, Locator, Page


class BaseClass:
    def __init__(self, playwright: Playwright, base_url: str):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url

    def close(self):
        self.context.close()
        self.browser.close()

    def goto(self):
        self.page.goto(self.base_url)

    def search(self, selector: str) -> Locator:
        result = self.page.locator(selector)
        return result









# class Play:
#     def __init__(self, page: Page) -> None:
#         # self.playwright = playwright
#         # self.browser = self.playwright.chromium.launch(headless=False)
#         # self.context = self.browser.new_context()
#         # Экземпляр пейдж
#         # self.page = self.context.new_page()
#         self.page = page
#         #self.login_form = LoginForm()
#
#     def search(self, selector: str) -> Locator:
#         result = self.page.locator(selector)
#         return result
#
#     def go_to(self, url: str):
#         self.page.goto(url)
#
#     def close(self):
#         self.page.close()
#         self.context.close()
#         self.browser.close()
# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.context = self.driver.new_context()
#         self.context = self.driver.new_context()
#         self.page = self.context.new_page()
#         self.base_url = "https://www.saucedemo.com/"
#
#     def search(self, selector: str) -> Locator:
#         result = self.driver.locator(selector)
#         return result
#
#     def go_to(self, url: str):
#         self.page.goto(url)
class BasePage:
    def __init__(self, page):
        self.driver = driver