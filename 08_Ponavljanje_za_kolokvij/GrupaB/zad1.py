'''
Napisati program koji broji broj slova
u tekstu koristeci rječnike.
Ključevi rječnika su slova,
a vrijednosti broj ponavljanja.

Provjeriti pojavljuju li se u tekstu
engleski znakovi (x, y, w) ili brojevi.

Iz rječnika dohvatiti uređene parove
slova i broj ponavljanja te iterirati kroz for petlju i ispisati.
'''

tekst = "Napisati program koji broji broj slova u tekstu koristeci rječnike. Ključevi rječnika su slova, a vrijednosti broj ponavljanja. Provjeriti pojavljuju li se u tekstu engleski znakovi (x, y, w) ili brojevi. Iz rječnika dohvatiti uređene parove slova i broj ponavljanja te iterirati kroz for petlju i ispisati."

tekst = tekst.lower() # pretvaramo tekst u mala slova

print(tekst)

slova = {}

for slovo in tekst: # Prolazimo kroz sva slova u tekstu
    slova[slovo] = slova.get(slovo, 0) + 1
    #if slovo not in slova: # Ako slovo ne postoji u rijecniku
    #    slova[slovo] = 1 # postavimo ga na 1
    #else: # ako postoji
    #    slova[slovo] += 1 # uvecamo za 1

print(slova)
print("Broj ponavljanja slova a:", slova.get("a"))

tekst = "Programiranje 2"

#if "x" in tekst or "y" in tekst or "w" in tekst:
#    print("Engleski tekst!")

import re
regex = r"[xyw\d]"
result = re.search(regex, tekst)
if result:
    print("Engleski tekst ili broj!")
    print(result)

# 1. nacin
parovi = []
for key in slova:
    par = (key, slova[key])
    parovi.append(par)
print(parovi)

# 2. nacin
parovi = slova.items()
for slovo, ponavljanje in parovi:
    print("Slovo", slovo, "se pojavljuje", ponavljanje, "puta")





