from playwright.sync_api import Page, expect
from forms.play import BasePage


class LoginForm(BasePage):
    # def __init__(self, page: Page):
    #     self.page = page

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

    def fill_login_username(self, username: str):
        username_f = self.page.locator('[id="username"]')
        username_f.fill(username)

    def click_enter(self):
        enter_f = self.page.locator('[id="login-button"]')
        enter_f.click()

    def clear_username_login(self, empty=""):
        username_f = self.page.locator('[id="user-name"]')
        username_f.fill(empty)

    def clear_password_login(self, empty=""):
        password_f = self.page.locator('[id="password"]')
        password_f.fill(empty)

    def check_exists_error(self):
        try:
            locator = self.page.locator(".error-message-container")
        except Exception:
            return False
        return True
        # expect(locator).to_contain_text("Error: First Name is required")
    # def get_text(self, elem_name):
    #     res = self.driver.find_element(By.XPATH, f"{elem_name}")
    #     return res.text
    # def check_exists_error(self):
    #     try:
    #         locator = self.page.locator(".error-message-container")
    #         # expect(locator).to_contain_text("Error: First Name is required")
    #         expect(locator).to_contain_text("Username is required")
    #     except Exception:
    #         return False
    #     return True

    def check_text(self, elem_name):
        element = self.page.locator(f"{elem_name}").first
        return element.inner_text()
