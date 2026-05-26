'''
Grupa O

U datoteci attendance.py nalazi se lista dolazaka studenata.
Svaki dolazak predstavljen je kao string oblika:

    ime;status

Primjer:
    Ana;prisutan

Učitavanje podataka:
    Učitaj listu attendance iz datoteke attendance.py.

Provjera zapisa:
    Ispravan zapis mora imati:
        ime koje počinje velikim slovom
        status koji može biti prisutan ili odsutan

    Ispravnost zapisa provjeri pomoću regularnog izraza.

Obrada podataka:
    Izdvoji samo ispravne zapise.

    Prebroji koliko je studenata prisutno, a koliko odsutno.

Ispis i zapis rezultata:
    Na ekran ispiši:
        Broj svih zapisa
        Broj ispravnih zapisa
        Broj prisutnih studenata
        Broj odsutnih studenata

    Iste rezultate upiši u tekstualnu datoteku izvjestaj_dolasci.txt.

Napomena:
    Program mora raditi nad podacima učitanim iz datoteke attendance.py.
    Podatke nije dozvoljeno ručno prepisivati u rješenje.
'''

from attendance import attendance
import re

#print(attendance)

regex = "^[A-Z][a-z]+;(prisutan|odsutan)$"

ispravni = []
prisutni = 0
odsutni = 0

for zapis in attendance:
    rezultat = re.search(regex, zapis)
    if rezultat:
        ispravni.append(zapis)
        
        ime, prisutnost = zapis.split(';')
        print(ime, prisutnost)
        if prisutnost == "prisutan":
            prisutni += 1
        else:
            odsutni += 1

svi = len(attendance)
ispravni = len(ispravni)

print("Svi zapisi:", svi)
print("Ispravni zapisi", ispravni)
print("Prisutni studenti:", prisutni)
print("Odsutni studenti:", odsutni)

#print(ispravni)

dat = open("izvjestaj_dolasci.txt", "w")

dat.write("Svi zapisi: " + str(svi) + "\n")
dat.write("Ispravni zapisi: " + str(ispravni) + "\n")
dat.write("Prisutni studenti: " + str(prisutni) + "\n")
dat.write("odsutni studenti: " + str(odsutni) + "\n")

dat.close()
