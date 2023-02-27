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

from selenium.webdriver.chrome.webdriver import WebDriver
'''
Exertcitiu 1 Login:
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome()
chrome.get('https://www.phptravels.net/')
login = chrome.find_element(By.ID,"ACCOUNT").click()
login = chrome.find_element(By.LINK_TEXT,"Customer Login").click()
login = chrome.find_element(By.NAME, "email").send_keys("albus.raul97@yahoo.ro")
login = chrome.find_element(By.NAME, "password").send_keys("parolaraul1")
login = chrome.find_element(By.CSS_SELECTOR,"label[for = 'rememberchb']").click()
time.sleep(3)
login = chrome.find_element(By.CSS_SELECTOR,"button[type = 'submit']").click()
time.sleep(10)
# In programul anterior este testarea automata a unei logari pe site'ul respectiv'''

# Exercitiul 2:
from selenium import webdriver, WebDriverWait
from selenium.webdriver.common.by import By
chrome: WebDriver = webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com/')
formy = chrome.find_element(By.LINK_TEXT, "Autocomplete").click()
formy = chrome.find_element(By.XPATH, '//input[@placeholder = "Enter address"]')# aici as vrea sa scriu in campul asta
# orice as pune nu reusesc nici cum primesc eroare, cand dau search in inspector imi gaseste exact asta, dar cand rulez
# programul primesc eroare.
# chrome.implicitly_wait(5)
# formy = WebDriverWait().until(chrome.find_element(By.XPATH, '//input[@placeholder = "Enter address"]'))
formy.send_keys("Oras Cluj-Napoca")
time.sleep(3)
