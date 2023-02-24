''' Ex1: If este tradus ca si Daca, intotdeauna este urmat de o conditie. Daca acea conditie este adevarata afisam,
ramura de IF, daca nu este adevarata acea conditie trecem la ramura de else adica altfel '''
import random

# Ex2: Verifică și afișează dacă x este număr natural sau nu.
x = int(input('intorduceti un numar'))
if x >= 1:
    print('numarul este natural')
else:
    print('numarul nu este natural')

# Ex3:  Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
x = int(input('Introduceti nr'))
if x==0:
    print('numarul este neutru')
elif x > 0:
    print ('numarul este pozitiv')
else:
    print('numarul este negativ')

# EX 4: Verifică și afișează dacă x este între -2 și 13.
x = int(input('Introduceti nr'))
if x >= -2 and x <= 13 :
    print('numarul este cuprins intre -2 si 13')
else:
    print('numarul nu este in intervalul dorit')

# EX 5:Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
x = int(input('introduceti nr x '))
y = int(input('introduceti nr y '))
if x - y < 5:
    print('diferenta numerelor este mai mica decat 5')
else:
    print('diferenta numerelor este mai mare sau egala decat 5')

# EX 6:  Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
x = int(input('Introduceti nr '))
if not(x < 5) and not(x > 27):
    print('x este intre intervalul 5 si 27')
else:
    print('x nu este in intervalul 5 si  27')

# EX 7: x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
# mare.
x = int(input('introduceti nr x '))
y = int(input('introduceti nr y '))
if x == y :
    print(' x si y sunt egale ')
elif x > y:
    print('x este mai mare decat y')
else:
    print('y este mai mare decat x ')

# EX 8: x , y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
x = int(input('introduceti latura x '))
y = int(input('introduceti latura y '))
z = int(input('introduceti latura z '))
if x == y == z :
    print('triunghiul este echilateral')
elif  x == y or  x == z or y == z :
    print(' triunghiul este isoscel')
else:
    print('triunghiul este oarecare')

# EX 9:Citește o literă de la tastatură.
# Verifică și afișează dacă este vocală sau nu
litera = input('Scrie o litera: ')
if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
    print('Litera introdusa este o vocala')
else:
    print('Litera introdusa este o consoana')

# EX 10:Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
nota = int(input('Introduceti nota: '))
if  nota==10: # aici am ales 10 deoarece doar peste 9 e nota A
    print('A')
elif nota <= 0 or nota >10:
    print('nu exista aceasta nota')
elif nota > 8:
    print('B')
elif nota >7:
    print('C')
elif nota >6:
    print('D')
elif nota >4:
    print('E')
elif nota<=4:
    print('F')

# Exercitii obtionale

# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = int(input('intorduceti numarul'))
if len(str(x))>= 4:
    print('x are minim 4 cifre')
else:
    print('x nu are minim 4 cifre')

# 2.Verifică dacă x are exact 6 cifre.
x = int(input('introduceti numarul'))
if len(str(x)) == 6:
    print('x are exact 6 cifre')
else:
    print('x nu are exact 6 cifre')

# 3.Verifică dacă x este număr par sau impar (x e int).
x= int(input('introduceti numarul '))
if x % 2 == 0:
    print('x este numar par')
else:
    print('x este numar impar')

# 4. x, y, z (int)
# Afișează care este cel mai mare dintre ele?
x = int(input('introduceti numarul x '))
y = int(input('introduceti numarul y '))
z = int(input('introduceti numarul z '))
if x > y and x > z:
    print('x= 'f'{x}'' si este cel mai mare numar')
elif y > x and y > z:
    print('y= 'f'{y}'' si este cel mai mare numar')
elif x == y == z:
    print('toate numerele sunt egale')
else:
    print('z= 'f'{z}'' si este cel mai mare numar')

# 5. x, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.
x = int(input('introduceti cate grade are unghiul x '))
y = int(input('introduceti cate grade are unghiul y '))
z = int(input('introduceti cate grade are unghiul z '))
if x >0 and y > 0 and z > 0 and x + y +z <= 180:
    print('triunghiul este valid')
else:
    print('triunghiul nu se poate forma')


# 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citiți de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# # Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
prop = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('introduceti numarul'))
if len(str(x))<len(prop):
    print(prop[:-x])
else:
    print(' numarul introdus are indexul mai mare decat propozitia')

# 7.Același string. Declară un string nou care să fie format din primele 5 caractere
# + ultimele 5
prop = 'Coral is either the stupidest animal or the smartest rock'
prop2 = 'Coral rock'
print(f'{prop[0:5]}{prop[-5:]}')


# 8. Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest
# cuvant
# ● output: 'Coral is either the stupidest animal or the smartest '
prop = 'Coral is either the stupidest animal or the smartest rock'
print(prop.index('rock'))
print(prop.find('rock'))
prop = 'Coral is either the stupidest animal or the smartest rock'
print(prop[0:52])

# 9. Citește de la tastatura un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
x = input('Scrie stringul')
if  x.lower()[0] == x.lower()[-1]:
    print('stringul are prima si ultima litera la fel')
else:
    print('prima si ultima litera din string NU sunt la fel')

# 10. Avand stringul '0123456789'
# ● Afișați doar numerele pare
# ● Afișați doar numerele impare
# (hint: folositi slicing, controlați din pas)
x = '0123456789'
print('numerele pare sunt: ' f'{x[2::2]}')
print('numerele impare sunt: ' f'{x[1::2]}')


# 11. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Luați un numărul ghicit de la utilizator
# Verificați și afișați dacă utilizatorul a ghicit
# Veți avea 3 opțiuni
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# ● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
numar = random.randint(1 , 6)
dice_roll = 3
if numar == dice_roll:
    print(f'Ai ghicit. Felicitari! Ai ales {dice_roll} si zarul a fost {numar}')
elif numar < dice_roll:
    print(f'Ai pierdut.Ai ales un numar mai mare. Ai ales {dice_roll} si a fost {numar}')
elif numar > dice_roll:
    print(f'Ai pierdut. Ai ales un numar mai mic. ai ales {dice_roll} si numarul a fost {numar}')















