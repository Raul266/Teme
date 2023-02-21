# 1.Având lista:
# mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
# 'Fiat', 'Trabant', 'Opel']
# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for i in range(0,len(mașini)):
    print(f'Mașina mea preferată este {mașini[i]}')
import random

for marca in mașini:
    print(f'Masina mea preferata este {marca}')

i=0
while i<len(mașini):
    print(f'Masina mea preferata este {mașini[i]}')
    i+=1

# 2. Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrise cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for i in range(1,len(mașini)):
    mașini[i]=mașini[i].upper()
else:
    print(mașini)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
for i in range(0,len(mașini)):
    if mașini[i] == 'Mercedes':
        print(f'Am găsit mașina dorită de dvs {mașini[i]}')
        break


# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant' , 'Opel']
for i in mașini:
    if i == 'Lăstun' or i == 'Trabant':
        continue
    print(f'S-ar putea sa va placa masina {i}')

# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant' , 'Opel']
masini_vechi = []
for masina in mașini:
    if masina == 'Lăstun'  or masina == 'Trabant':
        mașini.remove(masina)
        masini_vechi.append(masina)
        mașini.append('Tesla')
print(f'Modelele vechi sunt {masini_vechi}')
print(f'Modelele noi sunt {mașini}')

# 6. Având dict:
# pret_masini = {
# 'Dacia': 6800,
# 'Lăstun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.

pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
for masini in pret_masini:
    if pret_masini.get(masini) < 15000:
        print(f'Masina care se incadreaza in buget {masini}')

for masini, pret in pret_masini.items():
    print(f'Masina {masini} si pretul {pret} ')

for masini in pret_masini:
    if pret_masini.get(masini) < 15000:
        print(f'Pentru un buget de sub 15000 euro puteți alege mașină {masini}')

# 7. Având lista:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
j = 0
for i in numere:
    if i == 3:
        j +=1
print(f'3 apare de {j} ori')

# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
sum = 0
for i in numere:
    sum += i
print(f'Suma numerelor din lista este {sum}')

# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(0,len(numere)-1):
    for j in range(i+1,len(numere)):
        if(numere[i] > numere[j]):
            numere[i],numere[j] = numere[j],numere[i]
print(f'Cel mai mare numar din lista este {numere[-1]}')


# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
lista_noua = []
for i in numere:
    if i<=0:
        lista_noua.append(i)
    else:
        i = i * (-1)
        lista_noua.append(i)
print(lista_noua)

# EXERCITII OBTIONALE
# 1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
# # Itereaza prin listă alte_numere
# # Populează corect celelalte liste
# # Afișeaza cele 4 liste la final
for i in alte_numere:
    if  i > 0 and i % 2 != 0:
        numere_pozitive.append(i)
        numere_impare.append(i)
    elif  i > 0 and i % 2 == 0 :
        numere_pozitive.append(i)
        numere_pare.append(i)
    elif i < 0 and i % 2 == 0:
        numere_negative.append(i)
        numere_pare.append(i)
    elif i < 0 and i % 2 != 0:
        numere_negative.append(i)
        numere_impare.append(i)
print(f'Negative {numere_negative}')
print(f'Pozitive {numere_pozitive}')
print(f'Pare {numere_pare}')
print(f'Impare{numere_impare}')
#
# 2. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(0,len(alte_numere)-1):
    for j in range(i+1,len(alte_numere)):
        if(alte_numere[i] > alte_numere[j]):
            alte_numere[i],alte_numere[j] = alte_numere[j],alte_numere[i]
        print(alte_numere)
print(f'Lista sortata {alte_numere}')


# 3. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
# User alege un număr
# Programul îi spune:
# ● Nr secret e mai mare
# ● Nr secret e mai mic
# ● Felicitări! Ai ghicit!0'))
# !!! Daca rezolv asa problema programul ruleaza singur pana ghiceste numarul
numar_secret = random.randint(1,30)
numar_ghicit = random.randint(1,30)
while numar_ghicit!=numar_secret:
    numar_ghicit = random.randint(1,30)
    if numar_ghicit > numar_secret:
        print(f'Nr ghicit {numar_ghicit} este mai mare decat numarul secret')
    elif numar_ghicit < numar_secret:
        print(f'Nr ghicit {numar_ghicit} este mai mic decat numarul secret')
    else:
        print('Felicitari! Ai ghicit')

#!!! Daca rezolv asa programul in cere numarul pana cand il ghicesti
numar_secret = random.randint(1,30)
numar_ghicit = int(input('Introduceti numarul '))
while numar_ghicit!=numar_secret:
    numar_ghicit =  int(input('Introduceti numarul '))
    if numar_ghicit > numar_secret:
        print(f'Nr ghicit {numar_ghicit} este mai mare decat numarul secret')
    elif numar_ghicit < numar_secret:
        print(f'Nr ghicit {numar_ghicit} este mai mic decat numarul secret')
    else:
        print('Felicitari! Ai ghicit')

# 4. Alege un număr de la tastatură
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
i = 0
x = int(input('introduceti nr x '))
while i<x:
    i += 1
    j=1
    while j<i:
        j += 1
        print(i,end='')
    print(i)

