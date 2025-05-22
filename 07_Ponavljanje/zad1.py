#Napisati program koji broji broj slova u tekstu
#koristeci rječnike.
#Ključevi rječnika su slova,
#a vrijednosti broj ponavljanja.

import re

tekst = 'U računarstvu i informatici,regularni izraz (još i pravilni izraz, ispravni izraz[1] – često i engleske skraćenice regexp ili regex, u množini regexps, regexes ili regexen) je niz znakova koji opisuje druge nizove znakova (engl. string), u skladu s određenim sintaksnim pravilima. Prvenstvena svrha regularnog izraza je opisivaǌe uzorka za pretraživaǌe nizova znakova.'

'''
slova = {
'a': 20,
'b': 10,
...
    }
'''

slova = {}

tekst = tekst.lower()

for slovo in tekst:
    '''
    if slovo not in slova:
        slova[slovo] = 1
    else:
        slova[slovo] += 1
    '''
    slova[slovo] = slova.get(slovo, 0) + 1

#Provjeriti pojavljuju li se u tekstu engleski znakovi
#(x, y, w) ili brojevi.
reg = '[xyz\d]'

if re.search(reg, tekst):
    print('Pojavljuju se engleski znakovi ili brojevi')

#Iz rječnika dohvatiti uređene parove
#slova i broj ponavljanja te iterirati
#kroz for petlju i ispisati.
'''
parovi = []
for key in slova:
    par = key, slova[key]
    parovi.append(par)
'''

for slovo, br_ponavljanja in slova.items():
    print("Slovo", slovo, "se pojavljuje", br_ponavljanja, "puta.")

#print(slova.keys())
#print(slova.values())
#print(slova.items())
