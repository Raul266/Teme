import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

'''Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
- setUp()
- Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication
tearDown()
Quit browser
● Test 1
- Verifică dacă noul url e corect
● Test 2
- Verifică dacă page title e corect
● Test 3
- Verifică textul de pe elementul xpath=//h2 e corect
● Test 4
- Verifică dacă butonul de login este displayed
● Test 5
- Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
● Test 6
- Lasă goale user și pass
- Click login
- Verifică dacă eroarea e displayed
● Test 7
- Completează cu user și pass invalide
- Click login
- Verifică dacă mesajul de pe eroare e corect
- Este și un x pus acolo extra așa că vom folosi soluția de mai jos
expected = 'Your username is invalid!'
self.assertTrue(expected in actual, 'Error message text is
incorrect')
● Test 8
- Lasă goale user și pass
- Click login
- Apasă x la eroare
- Verifică dacă eroarea a dispărut
● Test 9
- Ia ca o listă toate //label
- Verifică textul ca textul de pe ele să fie cel așteptat (Username și
Password)
- Aici e ok să avem 2 asserturi
● Test 10
- Completează cu user și pass valide
- Click login
- Verifică ca noul url CONTINE /secure
- Folosește un explicit wait pentru elementul cu clasa ’flash succes’
- Verifică dacă elementul cu clasa=’flash succes’ este displayed
- Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
● Test 11
- Completează cu user și pass valide
- Click login
- Click logout
- Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
'''

class Login(unittest.TestCase):
    def click_login(self):
        login = self.chrome.find_element(By.TAG_NAME, "i").click()
    def setUp(self):
        self.chrome: webdriver = webdriver.Chrome()
        self.chrome.get('https://the-internet.herokuapp.com/')
        form = self.chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()

    def tearDown(self):
        self.chrome.quit()

    def test1(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual,expected,'Link-urile NU sunt la fel')

    def test2(self):
        actual = self.chrome.find_element(By.TAG_NAME, "h2").text
        expected = "Login Page"
        self.assertEqual(actual,expected,"Titulul de pe pagina este diferit de ceea ce ne asteptam")

    def test3(self):# nu stiu daca am inteles bine cerinta!?
        actual = self.chrome.find_element(By.XPATH, "//h2").text
        expected = "Login Page"
        self.assertEqual(actual, expected, "Textul afisat nu e corect")

    def test4(self):
        actual = self.chrome.find_element(By.TAG_NAME,"i").text
        expected = "Login"
        self.assertEqual(expected,actual,"Butonul de login nu e afisat in pagina")

    #def test5(self): Nu am inteles cerinta

    def test6(self):# HELP!!!# aici nu stiu daca am facut corect nu am nici o alta idee..
        self.click_login()
        actual = self.chrome.find_element(By.XPATH,'//div[@class="flash error"]')
        self.assertTrue(actual,"Mesajul de eroare NU este afisat")

    def test7(self):
        login_user = self.chrome.find_element(By.NAME, 'username').send_keys('alabala')
        login_pass = self.chrome.find_element(By.NAME, 'password').send_keys('alabala')
        self.click_login()
        actual = self.chrome.find_element(By.XPATH, '//div[@class="flash error"]')
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')
        # aici m-am blocat primesc eroarea asta: self.assertTrue(expected in actual, 'Error message text is incorrect')
        #                     ^^^^^^^^^^^^^^^^^^
        # TypeError: argument of type 'WebElement' is not iterable
        time.sleep(3)
        








