imena = ["Ivan", "Iva", "Ana", "Marko", "Pero"]
prezimena = ["Maric", "Peric", "Anic", "Markic", "Rozic"]
godine = ["20", "21", "20", "22", "23"]

parovi = []

import random

for i in range(5):
    ime = random.choice(imena)
    prezime = random.choice(prezimena)
    godina = random.choice(godine)
    par = ime, prezime, godina
    parovi.append(par)

print(parovi)

# drugi nacin
osobe = list(zip(imena, prezimena, godine))
print(osobe)
