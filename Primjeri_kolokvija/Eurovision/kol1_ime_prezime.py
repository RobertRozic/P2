'''
Zadano je natjecanje za pjesmu Eurovizije u kojem sudjeluje 37 država.
Svaka država je predstavljena s uređenim parom koji sadrži ime države, ime izvođača i ime pjesme
 npr. ("Croatia", "Baby Lasagna", "Rim Tim Tagi Dim"),

Nasumično odabrati 26 država koje će se natjecati u finalu i dodati ih u novu listu rječnika oblika:
{
  "drzava": "Croatia",
  "izvodjac": "Lelek",
  "pjesma": "Andromeda"
}

Nakon izbora finalista, potrebno je simulirati glasanje. Svaka država s popisa 37 drzava moze glasati.

Nasumice se dodjeljuju se bodovi (12, 10, 8, 7, ..., 1) nekoj od država finalista.

Drzava ne moze glasati sama za sebe. Bodove spremati u novo svojstvo rječnika "bodovi".

Nakon glasanja ispisati pobjedničku državu - ona koja ima najvise bodova.

Za svaku državu ispisati broj bodova.
Zbrojiti i ispisati ukupan broj dodijeljenih bodova.

Proci kroz sve finaliste i pomoću regexa (dakle ne pomoću len ugrađene funkcije)
provjeriti i ispisati sve države koje u naslovu pjesme imaju vise od 10 slova.

Rezultat zapisati u datoteku u obliku

drzava,pjesma,izvodjac,bodovi
drzava2,pjesma2,izvodjac2,bodovi2
'''

from countries import countries

print(countries)

import random

finalisti_uzorak = random.sample(countries, 26)
finalisti = []

for drzava, izvodjac, pjesma in finalisti_uzorak:
    el = {
        "drzava": drzava,
        "izvodjac": izvodjac,
        "pjesma": pjesma
    }
    finalisti.append(el)

bodovi = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]
for drzava, izvodjac, pjesma in countries:
    bez_drzave = []
    for item in finalisti:
        if item["drzava"] != drzava:
            bez_drzave.append(item)
    za_bodovanje = random.sample(bez_drzave, 10)
    brojac = 0
    for bod in bodovi:
        naziv_drzave = za_bodovanje[brojac]["drzava"]
        for finalist in finalisti:
            if finalist["drzava"] == naziv_drzave:
                finalist["bodovi"] = finalist.get("bodovi", 0) + bod
                break
        brojac += 1

finalisti = sorted(finalisti, key=lambda x: x['bodovi'], reverse=True)

bodovi = 0
for item in finalisti:
    bodovi += item["bodovi"]

print(bodovi)

import re
reg = "$.{10}";

for item in finalisti:
	if re.search(reg, item['pjesma']):
		print(item)
