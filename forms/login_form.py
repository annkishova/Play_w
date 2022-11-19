from playwright.sync_api import Page, Playwright
from forms.play import BaseClass


class LoginForm(BaseClass):
    def __init__(self, playwright: Playwright, base_url: str, page: Page):
        super().__init__(playwright, base_url)
        self.page = page

    def fill_login_and_enter(self, username="standard_user", password="secret_sauce"):
        username_f = self.search('[id="user-name"]')
        username_f.fill(username)
        password_f = self.search('[id="password"]')
        password_f.fill(password)
        enter_f = self.search('[id="login-button"]')
        enter_f.click()

    def fill_login_password(self, password: str):
        password_f = self.search('[id="password"]')
        password_f.fill(password)

    def click_enter(self):
        enter_f = self.search('[id="login-button"]')
        enter_f.click()

    def clear_username_login(self, empty=""):
        username_f = self.search('[id="user-name"]')
        username_f.fill(empty)

    def clear_password_login(self, empty=""):
        password_f = self.search('[id="password"]')
        password_f.fill(empty)
    """
    def fill_login_and_enter(self, username="standard_user", password="secret_sauce"):
        username_f = self.page.locator('[id="user-name"]')
        username_f.fill(username)
        password_f = self.page.locator('[id="password"]')
        password_f.fill(password)
        enter_f = self.page.locator('[id="login-button"]')
        enter_f.click()

    def fill_login_password(self, password: str):
        password_f = self.page.locator('[id="password"]')
        password_f.fill(password)

    def click_enter(self):
        enter_f = self.page.locator('[id="login-button"]')
        enter_f.click()

    def clear_username_login(self, empty=""):
        username_f = self.page.locator('[id="user-name"]')
        username_f.fill(empty)

    def clear_password_login(self, empty=""):
        password_f = self.page.locator('[id="password"]')
        password_f.fill(empty)

    
    def get_text(self, elem_name):
        res = self.driver.find_element(By.XPATH, f"{elem_name}")
        return res.text
        """
