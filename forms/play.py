# from playwright.sync_api import Playwright, Locator, Page, sync_playwright, BrowserContext


# class BaseClass:
#     def __init__(self) -> None:
#         self.playwright = Playwright
#         self.browser = None
#         self.context = BrowserContext
#         self.page = Page
#         self.headless = False
#
#     def start(self):
#         playwright = sync_playwright().start()
#         self.browser = playwright.chromium.launch(headless=self.headless)
#         self.context = self.browser.new_context()
#         self.page = self.context.new_page()
#
#     def close(self):
#         # self.context.close()
#         self.browser.close()
#
#     def goto(self, url):
#         goto = self.page.goto(url)
#
#     def search(self, selector: str) -> Locator:
#         result = self.page.locator(self.page, selector)
#         return result



    # def __init__(self):
    #     self.browser = Chromium.launch(headless=False)
    #     self.context = self.browser.new_context()
    #     self.page = self.context.new_page()




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
from playwright.sync_api import Playwright, Locator, Page, sync_playwright, BrowserContext


class Singleton(type):
    _instances = {}


def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
        cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
    return cls._instances[cls]


class Browser(metaclass=Singleton):
    def __init__(self):
        self.__driver = None
        self.headless = False


@property
def driver(self):
    return self.__driver


@driver.setter
def driver(self, value):
    self.__driver = value


def start(self):
    playwright = sync_playwright().start()
    self.browser = playwright.chromium.launch(headless=self.headless)
    self.context = self.browser.new_context()
    self.page = self.context.new_page()


def stop(self):
    self.browser.close()


class BaseClass:
    def __init__(self) -> None:
        self.playwright = Playwright
        self.browser = Browser().driver
        self.context = BrowserContext
        self.page = Page
        self.headless = False


def goto(self, url):
    self.page.goto(url)


def search(self, selector: str) -> Locator:
    result = self.page.locator(selector)
    return result
