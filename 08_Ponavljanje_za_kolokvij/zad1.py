'''
Napisati program koji broji broj slova u tekstu
koristeci rječnike.
Ključevi rječnika su slova, a vrijednosti broj ponavljanja.

Provjeriti pojavljuju li se u tekstu engleski znakovi (x, y, w) ili brojevi.

Iz rječnika dohvatiti uređene parove slova i broj ponavljanja te iterirati kroz for petlju i ispisati.

'''

tekst = "Lorem Ipsum is simply dummy text of the printing andtypesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

tekst = tekst.lower()

print(tekst)

slova = {}

for slovo in tekst:
    slova[slovo] = slova.get(slovo, 0) + 1
    #if slovo not in slova:
    #    slova[slovo] = 1
    #else:
    #    slova[slovo] += 1

print(slova)

print("Slova a ima:", slova.get("a"))

#if "x" in tekst or "y" in tekst or "w" in tekst:
#print('Engleski tekst')

import re

tekst = "Programiranje 1"
regex = "[xyw\d]"

result = re.search(regex, tekst)
if result:
    print("Nalaze se engleski znakovi ili brojevi!")
    print(result)
else:
    print("Nema engleskih znakova!")


# 1. Nacin
parovi = []

for key in slova:
    ntorka = key, slova[key]
    parovi.append(ntorka)

print(parovi)

# 2. Nacin
print(slova.items())
parovi = slova.items()

for slovo, ponavljanje in slova.items():
    print("Slovo " + slovo + " se pojavljuje " + str(ponavljanje) + " puta.")








