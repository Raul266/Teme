import unittest
from unittest import TestSuite, TestLoader
from HTMLTestRunner import HTMLTestRunner

from Tema_curs9 import Login
from TesteCurs8_10.Class_curs8 import LoginTema8
from TesteCurs8_10.bad_login_tests import BadLoginTests
from TesteCurs8_10.good_login_tests import GoodLoginTests

class LoginTestSuits(unittest.TestCase):
    def tests_suite(self):
        login_tests = TestSuite()

        login_tests.addTests([
            TestLoader().loadTestsFromTestCase(Login),
            TestLoader().loadTestsFromTestCase(LoginTema8),
            TestLoader().loadTestsFromTestCase(BadLoginTests),
            TestLoader().loadTestsFromTestCase(GoodLoginTests)
        ])

        runner = HTMLTestRunner(
            title="Tests Tema 8,9,10",
            verbosity=2,
            description='Teste tema 8,9,10',
            tested_by='Raul',
            report_name='Test tema 8,9,10'
        )
        runner.run(login_tests)
