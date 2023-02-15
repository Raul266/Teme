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
while schimbari_efectuate <= schimbari_max:
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