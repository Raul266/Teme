#Ex 1 o variabila este o zona din memoria unui calculator care mentine date

#Ex 2 declara si initializeaza cate o variabila de fiecare tip
# String
marca_masina = 'Dacia'
# Int
an_fabricatie = 2015
# Float
pret = 8500.50
# Bool
inmatriculat = True

#Ex 3 utilizeaza functia type pentru a verifica daca au tipul de date asteptat.
print(type('marca_masina'))
print(type(an_fabricatie))
print(type(pret))
print(type(inmatriculat))

#Ex 4 Rotunjeste floatul cu functia round si salveaza acesta modificare in aceeas variabila .verifica tipul acesteia
pret=round(pret)
print(type(pret))
print(pret)

# Ex 5 Floseste ptint() si printeaza in consola 4 propozitii cu variabilele alese
print(f'Am cumparat o masina marca {marca_masina}')
print(f'Este fabricata in anul {an_fabricatie}')
print(f'Pretul de achizitie a fost {pret}')
print(f'Masina este inmatriculata in Romania? {inmatriculat}')

# Ex 6 Citeste de la tastatura numele complet si afiseaza cate caractere are.
nume=input('nume')
prenume = input('prenume')
print(f'{len(nume)+len(prenume)}')

# Ex 7 citeste de la tastatura lungimea si latimea si apoi afiseaza aria unui dreptunghi
lungime = int(input('lungimea'))
latime = int(input('latime'))
aria_dreptunghi = latime * lungime
print(f'Aria dreptunghiului este {aria_dreptunghi}')

# Ex 8 Avand stringul: ' Coral is either the stupidest animal or the smartest rock'
# afiseaza de cate ori apare cuvantul 'the'
propozitie = 'Coral is either the stupidest animal or the smartest rock'
print(propozitie.count(' the '))# daca  NU pun satiu intre ghilimele imi numara si 'the' de la cuvantul 'either'

# Ex 9  Avand stringul: ' Coral is eiTHEr THE stupidest animal or THE smartest rock'
# afiseaza de cate ori apare cuvantul 'the'
propozitie = 'Coral is eiTHEr THE stupidest animal or THE smartest rock'
print(propozitie.count('the'))

# Ex 10 aceelas string verificati daca acest string contine numere
propozitie = 'Coral is either the stupidest animal or the smartest rock'
assert propozitie == 'Coral is either the stupidest animal or the smartest rock'
print('nu are numere')

#EXERCITII OPTIONALE
# 1 citeste de la tastatura un string de dimensiune impara
masina = input('Stringul:')
impar = int(len(masina)/2)
print(masina[impar])

# 2 verifica daca un string e palindrom
palindrom = input("palindrom")
assert palindrom == palindrom[::-1]
print('Stringul este palindrom')

# 3. Folosind cat mai putine linii de cod:
'''- cite??te un string de la tastatur?? (ex: 'alabala portocala');
- salveaz?? fiecare cuv??nt ??ntr-o variabil??;
- printeaz?? ambele variabile pentru verificare.'''

variabila1 , variabila2 = 'alabala' , 'portocala'
print(variabila1, variabila2)


# 4. Exerci??iu:
'''
- cite??te un string de la tastatur?? (ex: alabala portocala);
- salveaz?? primul caracter ??ntr-o variabil?? - indiferent care este el;
- capitalizeaz?? acest caracter peste tot, mai pu??in pentru primul ??i ultimul
caracter => alAbAlA portocAla.
'''
x = input('String')
text = x[1:-1]
xlow = x.lower()
first = xlow[0]
last = xlow[-1]
print(f"{first}{text.replace(first, first.upper())}{last}")

# EX 5
'''
- cite??te un user de la tastatur??;
- cite??te o parol??;
- afi??eaz??: 'Parola pt user x este ***** ??i are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie s??
afi??eze corect.'''
user = input('Scrie user')
parola =input('scrie parola')
caractere = len(parola)
print(f"Parola pentru user {user} este {caractere * '*'} si are {caractere} caractere.")
