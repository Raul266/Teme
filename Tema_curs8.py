'''Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
- https://www.phptravels.net/
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
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

# Exercitiul 2: #La acest exercitiu am complectat formularul de la 'Autocomplete'
from selenium import webdriver
from selenium.webdriver.common.by import By
'''chrome: WebDriver = webdriver.Chrome()
chrome.implicitly_wait(5)
chrome.get('https://formy-project.herokuapp.com/')
formy = chrome.find_element(By.LINK_TEXT, "Autocomplete").click()
formy = chrome.find_element(By.XPATH, '//input[@placeholder = "Enter address"]').send_keys("Oras Cluj-Napoca")
formy = WebDriverWait(chrome,5).until(expected_conditions.presence_of_element_located((By.XPATH,'//input[@placeholder = "Enter address"]')))
formy = chrome.find_element(By.CSS_SELECTOR, '#street_number').send_keys('Str. Mehedinti nr.58-60')
formy = chrome.find_element(By.ID, 'locality').send_keys('Cluj-Napoca')
formy = chrome.find_element(By.CSS_SELECTOR, '.form-control').send_keys('36000')
formy = chrome.find_element(By.CSS_SELECTOR, "input[placeholder = 'Country']").send_keys('Romania')
time.sleep(3)'''

# Exercitiul 3
chrome: webdriver = webdriver.Chrome()
chrome.get('https://the-internet.herokuapp.com/')
add_remove = chrome.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
add_remove = chrome.find_element(By.XPATH,"//button[1]").click() # facem click pe Add Element
add_remove = chrome.find_element(By.XPATH, '//button[@class = "added-manually"]').click() # facem click pe Delete
add_remove = chrome.find_element(By.TAG_NAME,'h3')
print(add_remove.text) #printam in python titlul de pe site

time.sleep(5)
