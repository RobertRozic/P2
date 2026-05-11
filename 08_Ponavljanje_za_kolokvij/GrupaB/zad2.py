'''
Generiraj niz od 5 imena i 5 prezimena i 5 godina te ih konvertiraj ih u uređeni par ime, prezime, godina.

Datoteke
Rezultat spremiti u datoteku u obliku

ime,prezime,godina
ime2, prezime2, godina2
…

'''
imena = ["Ante", "Ana", "Pero", "Mate", "Ivana"]
prezimena = ["Antic", "Anic", "Peric", "Matic", "Ivancic"]
godine = [22, 23, 24, 25, 26]

podaci = list(zip(imena, prezimena, godine))
print(podaci)

dat = open("podaci.csv", "w")

for ime, prezime, godina in podaci:
    dat.write(ime + ',' + prezime + ',' + str(godina) + '\n')

dat.close()



