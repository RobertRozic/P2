'''
Generiraj niz od 5 imena i 5 prezimena
i 5 godina te ih konvertiraj ih u uređeni
par ime, prezime, godina.

Datoteke
Rezultat spremiti u datoteku u obliku

ime,prezime,godina
ime2, prezime2, godina2
'''

imena = ['Ivan', 'Mate', 'Pero', 'Ana', 'Iva']
prezimena = ['Ivic', 'Matic', 'Peric', 'Anic', 'Ivic']
godine = [1997, 1998, 1999, 2000, 2001]

podaci = list(zip(imena, prezimena, godine))

print(podaci)

dat = open('rezultati.txt', 'w')

for ime, prezime, godina in podaci:
    dat.write(ime + ',' + prezime + ',' + str(godina) + '\n')

dat.close()







