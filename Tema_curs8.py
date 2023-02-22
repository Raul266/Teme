'''Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
observație:
- Probabil nu vei găsi un singur website care să cuprindă toate variantele
de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome()
chrome.get('https://www.phptravels.net/')
Login = chrome.find_element(By.ID,"ACCOUNT")
Login.click()
Login = chrome.find_element(By.LINK_TEXT,"Customer Login")
Login.click()
Login = chrome.find_element(By.NAME, "email")
Login.send_keys("albus.raul97@yahoo.ro")
Login = chrome.find_element(By.NAME, "password")
Login.send_keys("parolaraul1")
Login = chrome.find_element(By.CSS_SELECTOR,"label[for = 'rememberchb']")
Login.click()
time.sleep(3)
Login = chrome.find_element(By.CSS_SELECTOR,"button[type = 'submit']")
Login.click()
time.sleep(10)
# In programul anterior este testarea automata a unei logari pe site'ul respectiv