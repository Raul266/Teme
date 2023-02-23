# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale[::-1]
note_muzicale = ['do', 'si', 'la', 'sol', 'fa', 'mi', 're', 'do']
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

# 2. De câte ori apare ‘do’?
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale.count('do'))

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista1.extend(lista2)
print(lista1)
print(lista1 + lista2)
print(lista1.__add__(lista2))

# 4.
# ● Sortează și afișază lista generată la exercițiul anterior.
# ● Sortează numărul 0 folosind o funcție.
#  ● Afișaza iar lista.
lista = [3, 1, 0, 2, 6, 5, 4]
print(lista)
lista.sort()
print(lista)

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
# ● Lista este goală.
# ● Lista nu este goală.
lista = [3, 1, 0, 2, 6, 5, 4]
if len(lista) > 0:
    print('lista nu este goala')
else:
    print('lista este goala')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
lista = [3, 1, 0, 2, 6, 5, 4]
lista.clear()
print(lista)
del lista[0:7]
print(lista)
del lista



# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
lista = [3, 1, 0, 2, 6, 5, 4]
lista.clear()
if len(lista) > 0:
    print('lista nu este goala')
else:
    print('lista este goala')

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())

# 9. Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print('Ana a luat nota: '  f'{dict1["Ana"]}')
print('Gigel a luat nota: '  f'{dict1["Gigel"]}')
print('Dorel a luat nota: '  f'{dict1["Dorel"]}')

# 10. Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
dict1['Dorel']= 6
print(dict1)

# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
dict1.pop('Gigel')
dict1['Ionica'] = 9
print(dict1)

# 12.
# Set
# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
# ● Afișeaza zile_sapt
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('Luni')
print(zile_sapt)

# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
if weekend.issubset(zile_sapt) :
    print('Weekend este un subset al zilelor saptamanii')
else:
    print('Weekend nu este un subset al zilelor din săptămânii.')

# 14. Afișează diferențele dintre aceste 2 seturi.
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
print(zile_sapt.difference(weekend))

# 15. Afișază intersecția elementelor din aceste 2 seturi.
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
print(zile_sapt.intersection(weekend))

# Exerciții Opționale - grad de dificultate: Mediu spre greu(may need google) .
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări
echipa = {'Raul', 'Dani', 'Ovi', 'Gabi', 'Alex'}
rezerve = {'Cristi','Bogdan','Tudor', 'Mircea'}
schimbari_efectuate = 0
schimbari_max = 3
while schimbari_efectuate < schimbari_max:
    jucator_schimbat = input('scoateti jucator: ')
    jucator_intrat = input('introduceti jucator: ')
    if  jucator_schimbat in echipa and jucator_intrat in rezerve :
        echipa.remove(jucator_schimbat)
        rezerve.remove(jucator_intrat)
        echipa.add(jucator_intrat)
        schimbari_efectuate = schimbari_efectuate + 1
        print(echipa)
        print(f'A intrat jucatorul {jucator_intrat}, si a iesit {jucator_schimbat}, mai ai inca  {3-schimbari_efectuate} schimbari')
    else:
        print(f'Jucatorul {jucator_schimbat} nu e in teren sau {jucator_intrat} nu e pe banca de rezeve')
        print(f'mai ai inca  {3-schimbari_efectuate} schimbari')
print('Ai folosit toate schimbarile')















