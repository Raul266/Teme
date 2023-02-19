# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
class Cerc:
    raza = None
    culoare = None
    pi = 3.14
    def __init__(self,raza,  culoare):
        self.raza = raza
        self.culoare = culoare
    def descriere_cerc(self):
        print(f'Raza = {self.raza} si culoarea {self.culoare}')
    def Aria_cerc(self):
        aria = self.pi*self.raza**2
        return aria
    def Diametrul_cerc(self):
        diametrul = self.raza/2
        return diametrul
    def Circumferinta_cerc(self):
        circumferinta = 2*self.pi*self.raza
        return circumferinta

cerc = Cerc(5,'alb')
cerc.descriere_cerc()
print(cerc.Aria_cerc())
print(cerc.Diametrul_cerc())
print(cerc.Circumferinta_cerc())

# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
# descrie().

class Dreptunghi:
    lungime = None
    latime = None
    culoare = None
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare
    def descriere(self):
        print(f'Dreptunghiul are lungimea de {self.lungime} cm,latimea de {self.latime} cm si {self.culoare}')
    def aria(self):
        aria = self.lungime * self.latime
        print(aria)
    def perimetru(self):
        perimetrul = 2*self.lungime + 2*self.latime
        print(perimetrul)
    def schimba_culoare(self,culoare_noua):
        self.culoare = culoare_noua
dreptunghi = Dreptunghi(5,3,'alb')
dreptunghi.descriere()
dreptunghi.aria()
dreptunghi.perimetru()
dreptunghi.schimba_culoare('negru')
dreptunghi.descriere()

# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# ● descrie()
# ● nume_complet()
# ● salariu_lunar()
# ● salariu_anual()
# ● marire_salariu(procent)
class Angajat:
    nume = None
    prenume = None
    salariu = None
    procent = None
    def __init__(self,nume , prenume , salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
    def descriere(self):
        print(f'Ma numesc {self.nume} {self.prenume} si am un salariu de {self.salariu} lei')
    def nume_complet(self):
        print(f'{self.nume} {self.prenume}')
    def salariu_lunar(self):
        print(f'Am un salariu lunar de {self.salariu}')
    def salariu_anual(self):
        salariu_anual = self.salariu*12
        print(f'Salariul anual este de {salariu_anual} lei')
    def marire_salariu(self,procent):
        self.procent = procent
        self.marire_salariu = self.salariu * self.procent/100
        self.salariu_nou = self.marire_salariu + self.salariu
        print(f'Marirea de salariu a fost cu {self.procent} % ,salariul a fost marit cu {self.marire_salariu} lei , iar acuma salariul este de {self.salariu_nou} lei')

angajat = Angajat('Pop', 'Ion',5000)
angajat.descriere()
angajat.nume_complet()
angajat.salariu_lunar()
angajat.salariu_anual()
angajat.marire_salariu(20)

# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)

class Cont:
    iban = None
    titular_cont = None
    sold = None
    def __init__(self,iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')
    def  debitare_cont(self, suma):
        self.sold= self.sold - suma
        print(f'A fost retrasa din cont suma de {suma} lei soldul actual este de {self.sold} lei')
    def creditare_cont(self,suma):
        self.sold = self.sold + suma
        print(f'A fost adaugata in cont suma de {suma} lei, iar soldul actual este de {self.sold} lei')
cont = Cont(123456,'Raul', 100)
cont.afisare_sold()
cont.debitare_cont(10)
cont.debitare_cont(10)
cont.creditare_cont(100)

# TEMA OBTIONALA
# 1. Clasa Factura
# Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
# avea aceeași serie), număr, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# ● schimbă_cantitatea(cantitate)
# ● schimbă_prețul(pret)
# ● schimbă_nume_produs(nume)
# ● generează_factura() - va printa tabelar dacă reușiți
# Factura seria x numar y
# Data: generați automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon | 7 | 700 | 49000
from datetime import datetime
class Factura:
    seria = '123456'
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None
    def __init__(self,numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc
    def genereaza_factura(self):
        nestedList = [['Produs','telefon'],
                 ['Cantitate',7],
                 ['pret_bucata',700],
                 ['Total', 49000]]
        print(f'Factura seria {self.seria} si numarul {self.numar}')
        today = datetime.now()
        print(f'Data: {today}')
        for item in nestedList:
            print('|',item[0],' ' *(11- len(item[0])),'|',item[1])

factura = Factura(1,'bec',3,10)
factura.cantitate = 1
print(f'{factura.cantitate} buc')
factura.pret_buc = 5
print(f'{factura.pret_buc} lei')
factura.nume_produs = 'stilou'
print(f'Produsul este {factura.nume_produs}')
factura.genereaza_factura()


# 2.Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
# culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate mașinile cand ies din fabrica sunt gri
# Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
# Culori disponibile = alegeți voi 5-7 culori
# Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
# ● înmatriculare() - va schimba atributul înmatriculată în True
# ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
# culoare e în opțiunea de culori disponibile, altfel afișați o eroare
# ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
# negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
# accelera până la viteza maximă
# ● franeaza() - mașina se va opri și va avea viteza 0

class Masina:
    model = None
    marca = 'Dacia'
    viteza_maxima = None
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = ('rosu', 'alb','negru', 'albastru', 'galben')
    inmatriculata = False
    culoare_noua = None
    viteza = None
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima
    def descriere(self):
        print(f'Avem masina {self.marca} modelul este {self.model},de culoare {self.culoare}, care atinge viteza maxima de'
              f'{self.viteza_maxima}km/h.Autoturismul este inmatruculat? {self.inmatriculata}')
    def inmatriculare(self):
        self.inmatriculata = True
        print(self.inmatriculata)
    def  vopsire(self,culoare_noua):# !!! aici iar m-am complicat si tot am bagat self. degeaba si nu imi iesea
        culori_disponibile = ('rosu', 'alb', 'negru', 'albastru', 'galben')
        if culoare_noua.lower() in  culori_disponibile:
                print(f'Masina este vopsita in culoarea {culoare_noua}')
        else:
                print('nu exista aceasta culoare')
    def accelereaza(self,viteza):
            # while  0 < viteza < self.viteza_maxima:# !! AICI AM INCERCAT CU AMBELE METODE si am reusit
            if viteza == 0:
                print('Masina este oprita')
            elif viteza < 0:
                print(f'Nu se poate adauga viteza negativa')
            for vit in range(0,viteza+1):
                print(f'Viteza actuala este de {vit} km/h')
                if vit >= self.viteza_maxima:
                    print(f'viteza depaseste viteza maxima de  {self.viteza_maxima}km/h. STOP acceleratie!')
                    break

    def franeaza(self,viteza):
        while 0 < viteza <= self.viteza_maxima:
            viteza = viteza -1
            print(f'Masina a fost franata pana la {viteza}km/h')
        if viteza == 0:
            print('Masina este oprita')
        else:
            print(f'Nu se poate adauga viteza negativa sau viteza mai mare decat {self.viteza_maxima}km/h')

masina = Masina('logan',150)
masina.descriere()
masina.inmatriculare()
masina.vopsire('Negru')
# masina.accelereaza(150)
# masina.franeaza(100)

# 3. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
# Metode:
# ● adauga_task(nume, descriere) - se va adauga in dict
# ● finalizează_task(nume) - se va sterge din dict
# ● afișează_todo_list() - doar cheile
# ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, printăm detalii suplimentare.
# ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l adauge.
# ○ Dacă acesta răspunde nu - la revedere
# ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în dict

class TodoList:
    todo = {}
    def adauga_task(self,nume,descriere):
        self.todo[nume]=descriere
        print(self.todo)
    def finalizeaza_task(self,nume):
        self.todo.pop(nume)
        print(self.todo)
    def afiseaza_todo_list(self):
        print(self.todo.keys())
    def afiseaza_detalii_suplimentare(self,nume_task):
        if nume_task not in self.todo:
            intrebare = input('Introduceti da/nu daca doriti sa adaugeti taskul in lista')
            if intrebare.lower() == 'nu':
                print('La revedere')
            else:
                nume = input('Adauga nume ')
                descriere = input('Adauga descriere')
                self.adauga_task(nume,descriere)
        else:
            print(self.todo[nume_task])




clasa = TodoList()
clasa.adauga_task('seat','alb')
# clasa.finalizeaza_task('seat')
clasa.afiseaza_todo_list() # aici  daca nu comentez clasa.finalizeaza_task imi afiseaza un dict gol
clasa.afiseaza_detalii_suplimentare('logan')

