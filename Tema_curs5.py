# 1.Funcție care să calculeze și să returneze suma a două numere
def suma_numerelor(a,b):
    suma = a+b
    return suma
print(f'Suma numerelor este {suma_numerelor(3,4)}')

# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
def numar_par_impar(numar):
    if numar % 2 == 0:
        return True
    else:
        return False
print(numar_par_impar(12))

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)
def caractere_nume(nume,prenume, nume_mijlociu):
    litere_nume = len(nume)+len(prenume)+len(nume_mijlociu)
    return litere_nume
print(f'Nr total de caractere {caractere_nume("Albus","Raul","Teodor")}')

# 4. Funcție care returnează aria dreptunghiului
def aria_dreptunghiului(L,l):
    aria = L*l
    return aria
print(f'Aria dreptunghiului este {aria_dreptunghiului(5,2)}')

# 5. Funcție care returnează aria cerculu
def aria_cercului(R):
    pi = 3.14
    aria = pi*R**2
    return aria
print(f'Aria cercului este {aria_cercului(3)}')

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și False dacă nu găsește.
def string(cuvant):
    if 'x' in cuvant:
        return True
    else:
        return False
print(string('abcd'))
print(string('xerox'))

# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y
def propozitie(cuvant):
    i=0
    j=0
    for caracter in cuvant:
        if caracter.islower():
            i+=1
        else:
            j+=1
    print(f'Avem {j} caractere mari')
    print(f'Avem {i} caractere mici')
print(propozitie('ALaBAla'))

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive
def lista_numere(*numere):
    lista = []
    for n in numere:
        if n > 0:
            lista.append(n)
    return lista
print(lista_numere(4, 3, 5, -1, -5, 3, 6, 7))

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale
def numere(x,y):
    if x > y:
        print(f'Primul număr {x} este mai mare decat al doilea nr {y}')
    elif y > x:
        print(f'Al doilea nr {y} este mai mare decat primul nr {x}')
    else:
        print('Numerele sunt egale')
print(numere(5,7))

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False
def numar_set(n,set_de_numere):
        if n not in set_de_numere:
            set_de_numere = set_de_numere.append(n)
            print('am adaugat numărul nou în set')
            return True
        else:
            print('nu am adaugat numărul în set. Acesta există deja')
            return False
print(numar_set(5,[4,6,7,1,8,9]))

# 1. Funcție care primește o lună din an și returnează câte zile are acea luna

def numar_zile_din_luna(luna):
    lunile_anului = {'ianuarie':31, 'februarie':28,'martie':31,'aprilie':30,'mai':31,'iunie':30,'iulie':31,'august':30,
                     'septembrie':30, 'octombrie':31,'noiembrie':30,'decembrie':31}
    for luna in lunile_anului:
        print(lunile_anului.values())
print(numar_zile_din_luna('mai'))



# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)
def calculator(x,y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a ,b,c,d
print(calculator(10,2))

# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
def dictionar(numere):
    lista= {}
    for n in numere:
        if n in lista:
            lista[n] += 1
        else:
            lista[n] = 1
    for key , value  in lista.items():
        return lista
print(dictionar([1, 3, 1, 5, 9, 7, 7, 5, 5]))



# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
def valoarea_maxima(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return print('numerele sunt egale')
print(valoarea_maxima(100,20,30))


# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
def suma_tuturor_numerelor_a_numaruli(numar):
    suma = 0
    while  numar > 0 :
        suma = suma + numar
        numar =  numar -1
    return suma
print(suma_tuturor_numerelor_a_numaruli(4))

# Exerciții Opționale - Bonus

# 1.Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
# numerele comune
# Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
def numerele_comune_din_2_liste(lista1,lista2):
        return set(lista1.intersection(lista2))
print(numerele_comune_din_2_liste({1,1,2,2,3},{2,2,3,4}))


# 2.. Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
# Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
# invalidă.
def reducere_de_pret(pret_produs,procent_reducere):
    suma_redusa=0
    pret_nou = 0
    if procent_reducere > 100:
        return 'Reducere invalida.Mai mare de 100%'
    elif procent_reducere <= 100:
        suma_redusa= pret_produs/100*procent_reducere
        pret_nou = pret_produs - suma_redusa
        return pret_nou
print(reducere_de_pret(100,10))

# 3. Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)
from datetime import datetime
import pytz # am invatat si cum sa imi instalez un package
def data_ora_RO():
    data_ora = pytz.timezone('Europe/Bucharest')
    country_time = datetime.now()
    return country_time.strftime("Data este %d-%m-%y si ora este %H:%M:%S")
print(data_ora_RO())
import pytz
def data_ora_China():
    data_ora  = pytz.timezone('Asia/Shanghai')
    country_time = datetime.now(data_ora)
    return country_time.strftime("Date is %d-%m-%y and time is %H:%M:%S")
print(data_ora_China())


# 4. Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
# Crăciun dacă nu vrei să ne zici cand e ziua ta :)
from datetime import datetime
def zile_pana_la_ziua_de_nastere(*birth):
    today = datetime.today()
    birth = datetime(2023,1,26)
    diff = birth - today
    return diff
print(zile_pana_la_ziua_de_nastere())
