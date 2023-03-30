import unittest
from pages.login_page import Login


class CorectLoginTests(unittest.TestCase):
    login_page = Login()

    def setUp(self):
        self.login_page.navigate_to_login_page()

    def test_login_corect(self):
        self.login_page.login('tomsmith', 'SuperSecretPassword!')
        expected = 'https://the-internet.herokuapp.com/secure'
        actual = self.login_page.driver.current_url
        self.assertEqual(expected, actual, "Nu am reusit sa ne logam")
