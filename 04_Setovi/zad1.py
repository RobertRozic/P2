#Potrebno je kreirati evidenciju odrađenih sati
#i isplata radnika tvrtke koja se bavi dostavljanjem.

# Generirati 15 radnika random imena i prezimena
# iz ponuđene liste, te njegovu satnicu slučajnim
# odabirom floata između 4 i 6 zaokruženu na 2 decimale.

imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

import random
# Sve radnike spremiti u listu radnika,
# a jedan radnik je rječnik oblika 
# {“ime”: “John”, “prezime”: “Doe”, “satnica”: 5.20}
radnici = []
for i in range(15):
    radnik = {
        "ime": random.choice(imena),
        "prezime": random.choice(prezimena),
        "satnica": round(random.uniform(4,6), 2)
    }
    radnici.append(radnik)
#print(radnici)

# Iterirati kroz sve radnike i dodati im novo svojstvo
# “tjedni_sati” koji generira cijeli broj
# odrađenih sati u 1 tjednu od 20 do 30.

for radnik in radnici:
    radnik['tjedni_sati'] = random.randint(20,30)
print(radnici)


# Nakon toga napraviti obračun množenjem satnice
# sa tjednim satima i rezultate spremiti
# u listu tuple-a (trojki) oblika (ime, prezime, isplata).

ntorke = []
for radnik in radnici:
    za_isplatu = radnik['satnica'] * radnik['tjedni_sati']
    ntorka = radnik['ime'], radnik['prezime'], round(za_isplatu, 2)
    ntorke.append(ntorka)
print(ntorke)


# Iteriranjem ispisati podatke,
# a zatim izračunati ukupnu i prosječnu isplatuza taj tjedan.

zbroj = 0
for ime, prezime, isplata in ntorke:
    print(ime, prezime, isplata)
    zbroj += isplata

prosjecna = zbroj/len(radnici)

print("Ukupna isplata", round(zbroj,2))
print("Prosjecna isplata",round(prosjecna,2))

# Ispisati Imena svih radnika koji
# imaju isplatu iznad prosječne.

print("------------------")
print("Radnici koji imaju isplatu vecu od posjecne:")
for ime, prezime, isplata in ntorke:
    if isplata > prosjecna:
        print(ime, prezime)
