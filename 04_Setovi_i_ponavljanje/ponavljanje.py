import random
imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan',
'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']

prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez',
'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith',
'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

radnici = []

for i in range(15):
	radnik = {}
	radnik["ime"] = random.choice(imena)
	radnik["prezime"] = random.choice(prezimena)
	radnik["satnica"] = round(random.uniform(4, 6), 2)
	radnici.append(radnik)
print(radnici)

for radnik in radnici:
	radnik["tjedni_sati"] = random.randint(20, 30)
	
print('-'*20)
	
print(radnici)

print('-'*20)

ntorke = []
for radnik in radnici:
	isplata = radnik['satnica'] * radnik['tjedni_sati']
	ntorka = (radnik['ime'], radnik['prezime'], isplata)
	ntorke.append(ntorka)
	
print(ntorke)

zbroj = 0

for ime, prezime, isplata in ntorke:
	zbroj += isplata

prosjek = zbroj / 15

print("Ukupna isplata", zbroj)
print("Prosjek", prosjek)

for ime, prezime, isplata in ntorke:
	if isplata > prosjek:
		print(ime, prezime)

