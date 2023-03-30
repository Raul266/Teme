import unittest

from pages.login_page import Login


class InorectLoginTests(unittest.TestCase):
    login_page = Login()

    def setUp(self):
        self.login_page.navigate_to_login_page()

    def test_user_pass_incorect(self):
        self.login_page.login('alabala', 'alabala')

        actual = self.login_page.get_error_message()
        expected = "Your username is invalid!\n×"
        self.assertEqual(actual, expected, "Am reusit sa ne logam cu credentiale gresite")

    def test_empty_password(self):
        self.login_page.login('tomsmith', '')

        actual = self.login_page.get_error_message()
        expected = "Your password is invalid!\n×"
        self.assertEqual(expected, actual, "Am reusit sa ne logam fara parola")
