import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

    def login_click(self, username, password):
        self.chrome.find_element(By.NAME, 'username').send_keys(username)
        self.chrome.find_element(By.NAME, 'password').send_keys(password)
        self.chrome.find_element(By.TAG_NAME, "i").click()

    def click_login(self):
        self.chrome.find_element(By.TAG_NAME, "i").click()
    def click_logout(self):
        self.chrome.find_element(By.XPATH, '//a [@class = "button secondary radius"]').click()

    def setUp(self):
        self.chrome: webdriver = webdriver.Chrome()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(By.LINK_TEXT, 'Form Authentication').click()

    def tearDown(self):
        self.chrome.quit()

    def test1(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected, 'Link-urile NU sunt la fel')

    def test2(self):
        actual = self.chrome.find_element(By.TAG_NAME, "h2").text
        expected = "Login Page"
        self.assertEqual(actual, expected, "Titulul de pe pagina este diferit de ceea ce ne asteptam")

    def test3(self):  # nu stiu daca am inteles bine cerinta!?
        actual = self.chrome.find_element(By.XPATH, "//h2").text
        expected = "Login Page"
        self.assertEqual(actual, expected, "Textul afisat nu e corect")

    def test4(self):
        actual = self.chrome.find_element(By.TAG_NAME, "i").text
        expected = "Login"
        self.assertEqual(expected, actual, "Butonul de login nu e afisat in pagina")

    def test5(self):
        actual = self.chrome.find_element(By.LINK_TEXT, "Elemental Selenium").get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(actual, expected, "Atributul href al linkului ‘Elemental Selenium’ NU corect")

    def test6(self):
        self.login_click('', '')
        actual = self.chrome.find_element(By.XPATH, '//div[@class="flash error"]')
        self.assertTrue(actual.is_displayed(), "Mesajul de eroare NU este afisat")

    def test7(self):
        self.login_click('alabala', 'alabala')
        actual = self.chrome.find_element(By.XPATH, '//div[@class="flash error"]').text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    def test8(self):
        self.login_click('', '')
        self.chrome.maximize_window()
        self.chrome.find_element(By.CLASS_NAME, "close").click()
        expected = self.chrome.find_element(By.XPATH, '// div[@class = "flash error"]')
        self.assertTrue(expected.is_displayed(), "Eroarea este afisata")
        time.sleep(2)

    def test9(self):
        lista_label = self.chrome.find_elements(By.XPATH, "//label")
        assert lista_label[0].text == "Username"
        assert lista_label[1].text == "Password"

    def test10(self):
        self.login_click('tomsmith', 'SuperSecretPassword!')
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/secure'
        self.assertEqual(actual, expected, "Noul NU url contine '/secure sau este diferit '")

        WebDriverWait(self.chrome, 3).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[@class = 'flash success']")))
        flash_succes = self.chrome.find_element(By.XPATH, "//div[@class = 'flash success']")
        actual = flash_succes.text
        expected = 'secure area!'
        self.assertTrue(flash_succes.is_displayed(), "Elelmentul nu este afisat")
        self.assertTrue(expected in actual, "Mesajul nu contine 'secure arena'")

    def testul11(self):
        self.login_click('tomsmith', 'SuperSecretPassword!')
        self.click_logout()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected, 'Nu ne-am putut deloga')

    '''● Test12 - brute force password hacking
    - Completează user tomsmith
    - Găsește elementul // h4
    - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o potențială parolă.
    - Folosește o structură iterativă prin care să introduci rând pe rând parolele și să apeși pe login.
    - La final testul trebuie să îmi printeze fie
        ‘Nu am reușit să găsesc parola’
        ‘Parola secretă este [parola]’
    '''

    def test12(self):
        parola = self.chrome.find_element(By.XPATH, '//h4').text.split()
        for i in range(len(parola)):
            self.chrome.find_element(By.NAME, 'username').send_keys('tomsmith')
            self.chrome.find_element(By.NAME, 'password').send_keys(parola[i])
            self.click_login()
            if self.chrome.current_url == "https://the-internet.herokuapp.com/secure":
                print(f"Parola secretă este {parola[i]}")
                break
            else:
                print('Nu am reușit să găsesc parola')
        time.sleep(3)