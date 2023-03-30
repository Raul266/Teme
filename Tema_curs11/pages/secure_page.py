from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
class Secure(HomePage):
    LOGOUT_BTN = (By.CLASS_NAME, "button secondary radius")
    Succes_MSG = (By.CLASS_NAME, "flash success")

    def logout(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()
    def success_msg_is_displayed(self):
        return self.driver.find_element(*self.Succes_MSG).is_displayed()
    def success_msg_text(self):
        return self.driver.find_element(*self.Succes_MSG).text
