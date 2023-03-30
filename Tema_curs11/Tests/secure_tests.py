import unittest

from pages.login_page import Login


class SecureTests(unittest.TestCase):
    login_page = Login()

    def setUp(self):
        self.login_page.navigate_to_login_page()

    def test_correct_login_msg(self):
        self.login_page.login('tomsmith', 'SuperSecretPassword!')
        actual = self.login_page.get_success_message()
        expected = 'You logged into a secure area!\n×'
        self.assertEqual(actual, expected, 'Mesajul de success este diferit')

    def test_msg_isdispayed(self):
        self.login_page.login('tomsmith', 'SuperSecretPassword!')
        actual = self.login_page.get_success_message()
        self.assertTrue(actual)

    def test_click_logout(self):
        self.login_page.login('tomsmith', 'SuperSecretPassword!')
        self.login_page.logout_btn()
        actual = self.login_page.driver.current_url
        expected = "https://the-internet.herokuapp.com/login"
        self.assertEqual(actual, expected, "Nu am reusit sa ne delogam")
