from selenium.webdriver.common.by import By
from pages.home_page import HomePage
class Login(HomePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BTN = (By.CLASS_NAME, "radius")
    LOGOUT_BTN =(By.XPATH,"//i [@class = 'icon-2x icon-signout']")
    ERROR_MSG = (By.XPATH, "//div [@class = 'flash error']")
    SUCCESS_MSG = (By.XPATH, "//div [@class = 'flash success']")

    def login(self, user, parola):
        self.fill_input(*self.USERNAME_INPUT, user)
        self.fill_input(*self.PASSWORD_INPUT, parola)
        self.driver.find_element(*self.LOGIN_BTN).click()
    def logout_btn(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MSG).text
    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MSG).text
