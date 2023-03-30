import unittest
from unittest import TestSuite, TestLoader

from HTMLTestRunner import HTMLTestRunner

from Tests.corect_login_tests import CorectLoginTests
from Tests.incorect_login_tests import InorectLoginTests
from Tests.secure_tests import SecureTests

'''EXERCIUTIU:
Impementati 3 pagini intr-un nou proiect BDD cu POM

a. Home page https://the-internet.herokuapp.com/
- Sa aiba cel putin 3 elemente inlcusiv Form Authentication
- Sa contina metode de click pe ele

b. Login page https://the-internet.herokuapp.com/login
- Sa contina user, pass, login_btn si metode pt interactiune cu ele

c. Secure page https://the-internet.herokuapp.com/secure
- Sa contina mesajul de succes si verificare ca e displayed
- Sa contina logout_btn si click pe el'''


class TestsSuite(unittest.TestCase):

    def test_suite(self):
        login_tests = TestSuite()

        login_tests.addTests([
            TestLoader().loadTestsFromTestCase(CorectLoginTests),
            TestLoader().loadTestsFromTestCase(InorectLoginTests),
            TestLoader().loadTestsFromTestCase(SecureTests)
        ])

        runner = HTMLTestRunner(
            title="All Login,Logout,Secure Tests",
            verbosity=1,
            description="Good/Bad login and Secure tests",
            tested_by="Raul",
            report_name="Tests"
        )

        runner.run(login_tests)
