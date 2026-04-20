'''
Potrebno je kreirati evidenciju odrađenih sati
i isplata radnika tvrtke koja se bavi dostavljanjem.
Generirati 15 radnika random imena i prezimena
iz ponuđene liste, te njegovu satnicu slučajnim
odabirom floata između 4 i 6 zaokruženu na 2 decimale.
Sve radnike spremiti u listu radnika, a jedan radnik
je rječnik oblika 
{“ime”: “John”, “prezime”: “Doe”, “satnica”: 5.20}
Iterirati kroz sve radnike i dodati im novo svojstvo
“tjedni_sati” koji generira cijeli broj odrađenih sati
u 1 tjednu od 20 do 30.
Nakon toga napraviti obračun množenjem satnice sa
tjednim satima i rezultate spremiti u listu tuple-a (trojki)
oblika (ime, prezime, isplata).
Iteriranjem ispisati podatke, a zatim izračunati ukupnu
i prosječnu isplatu za taj tjedan.
Ispisati Imena svih radnika koji imaju isplatu
iznad prosječne.
'''
import random

imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']
prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

radnici = []

for i in range(15):
    radnik = {
        "ime": random.choice(imena),
        "prezime": random.choice(prezimena),
        "satnica": round(random.uniform(4, 6), 2)
    }
    radnici.append(radnik)

#print(radnici)

for radnik in radnici:
    radnik['tjedni_sati'] = random.randint(20,30)

print(radnici)

lista_ntorki = []

for radnik in radnici:
  isplata = round(radnik['tjedni_sati'] * radnik['satnica'],2)
  ntorka = (radnik['ime'], radnik['prezime'], isplata)
  lista_ntorki.append(ntorka)

#print(lista_ntorki)

ukupno = 0
for ime, prezime, isplata in lista_ntorki:
    print(ime, prezime, isplata)
    ukupno += isplata

print("Ukupno za isplatu:", round(ukupno,2))

prosjecna = ukupno / len(lista_ntorki)
print("Prosjecna isplata:", round(prosjecna, 2))

print("Vise od prosjeka imaju:")
for ime, prezime, isplata in lista_ntorki:
    if isplata > prosjecna:
        print(ime, prezime)




