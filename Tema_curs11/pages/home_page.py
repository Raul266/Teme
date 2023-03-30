from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    driver = webdriver.Chrome()
    def navigate_to_login_page(self):
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(By.XPATH, "//a[.='Form Authentication']").click()
    def fill_input(self, by, selector, text):
        self.driver.find_element(by, selector).send_keys(text)


