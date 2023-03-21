import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginTema8(unittest.TestCase):

    def setUp(self):
        self.chrome: webdriver = webdriver.Chrome()
        self.chrome.get('https://www.phptravels.net/')
        self.chrome.find_element(By.ID, "ACCOUNT").click()
        self.chrome.find_element(By.LINK_TEXT, "Customer Login").click()

    def tearDown(self):
        self.chrome.quit()

    def login(self, username, password):
        self.chrome.find_element(By.NAME, "email").send_keys(username)
        self.chrome.find_element(By.NAME, "password").send_keys(password)
        self.chrome.find_element(By.CSS_SELECTOR, "label[for = 'rememberchb']").click()

    def click_login(self):
        self.chrome.find_element(By.XPATH, "//button[@type='submit']").click()

    def test1(self):
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/login'
        self.assertEqual(actual, expected, 'Link-urile NU sunt la fel')

    def test2_cont_inexistent(self):
        self.login('raul@yahoo.com', 'Raul1234')
        self.click_login()
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/login/failed'
        self.assertEqual(expected, actual, "Te-ai logat cu un cont gresit")
