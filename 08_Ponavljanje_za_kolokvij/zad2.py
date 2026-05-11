'''
Generiraj niz od 5 imena i 5 prezimena i 5 godina
te ih konvertiraj ih u uređeni par ime, prezime, godina.

Datoteke
Rezultat spremiti u datoteku u obliku

ime,prezime,godina
ime2, prezime2, godina2
'''

imena = ["Ivan", "Ana", "Pero", "Mate", "Maja"]
prezimena = ["Ivic", "Anic", "Peric", "Matic", "Majic"]
godine = [21, 22, 23, 24, 25]

podaci = list(zip(imena, prezimena, godine))

print(podaci)

dat = open("podaci.txt", "w")

for ime, prezime, godine in podaci:
    dat.write(ime + "," + prezime + "," + str(godine) + "\n")

dat.close()


