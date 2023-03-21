import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()


class AlertTests(unittest.TestCase):

    def test_context_menu_alert(self):
        chrome.get("https://the-internet.herokuapp.com/context_menu")
        action = ActionChains(chrome)
        action.context_click(chrome.find_element(By.ID, "hot-spot")).perform()

        alert = chrome.switch_to.alert

        self.assertEqual(alert.text, "You selected a context menu")

        alert.accept()

    def test_confirm_box(self):
        chrome.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
        chrome.find_element(By.ID, "confirmexample").click()

        chrome.switch_to.alert.dismiss()

        actual = chrome.find_element(By.ID, "confirmreturn").text
        expected = "false"

        self.assertEqual(actual, expected)

    def test_prompt_box(self):
        chrome.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
        chrome.find_element(By.XPATH, "//*[@id='promptexample']").click()

        alert = chrome.switch_to.alert
        alert.send_keys("Nume")
        alert.accept()

        self.assertEqual("Nume", chrome.find_element(By.ID, "promptreturn").text)
