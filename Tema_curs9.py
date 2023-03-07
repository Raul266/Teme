import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login(unittest.TestCase):
    chrome: WebDriver = webdriver.Chrome()
    chrome.get('https://the-internet.herokuapp.com/')
    form = chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()