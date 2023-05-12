# definirarnje liste imena i prezimena
imena = ['Ana', 'Ante', 'Ivana', 'Ivan',
         'Petra', 'Petar', 'Marija', 'Marko',
         'Luka', 'Lucija', 'Marta', 'Mirna',
         'Nikola', 'Nina', 'Josip', 'Jelena',
         'Kristina', 'Katarina', 'Tomislav', 'Tihana']

prezimena = ['Babić', 'Blažević', 'Horvat', 'Jurić',
             'Kovačić', 'Kovačević', 'Novak', 'Petrović',
             'Popović', 'Radmanović', 'Šimić', 'Tomić',
             'Varga', 'Vidović', 'Vuković', 'Zorić',
             'Kralj', 'Vukmanić', 'Župan', 'Matijević']

import random

# definiramo praznu listu za spremanje radnika
radnici = []

# 15 puta ponavljamo kod za generiranje random radnika
for i in range(15):
    radnik = {}
    radnik["ime"] = random.choice(imena)
    radnik["prezime"] = random.choice(prezimena)
    radnik["satnica"] = round(random.uniform(4, 6), 2)
    radnici.append(radnik)

print(radnici)

for radnik in radnici:
    radnik['tjedni_sati'] = random.randint(20, 30)

print(radnici)

isplate = []
for radnik in radnici:
    isplata = radnik["satnica"] * radnik["tjedni_sati"]
    mytuple = radnik["ime"], radnik["prezime"], round(isplata, 2)
    isplate.append(mytuple)
    
print(isplate)

iznos = 0
for ime, prezime, isplata in isplate:
    print(ime, prezime, isplata)
    iznos += isplata

print("Ukupno za isplatiti:", iznos)
    



