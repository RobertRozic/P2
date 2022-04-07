rjecnik = dict()

rjecnik['ime'] = 'Robert'
rjecnik['prezime'] = 'Rozic'

print(rjecnik)

rjecnik2 = {
    "ime": "Robert",
    'prezime': 'Rozic'
    }

print(rjecnik2)

rezultati = {
    "Marko": 43,
    "Ana": 75,
    "Ivan": 80,
    "Ivana": 42,
    "Mia": 11
}

brojevi = [1, 4, 12, 15]
print("Prije", brojevi[2])
brojevi[2] = 50
print("Poslije", brojevi[2])

# Azuriranje
rezultati['Marko'] = 20

# Dohvacanje
print("Marko: ", rezultati['Marko'])

# Dodavanje
rezultati['Luka'] = 65
rezultati['Iva'] = 50
print(rezultati)

# Brisanje
#del rezultati['Marko']
print(rezultati)

# Provjera postojanja kljuca
if 'Iva' in rezultati:
    print("Iva postoji u rjecniku")
    print(rezultati["Iva"])

# Iteriranje rjecnika
print("Elementi iteriranja")
for element in rezultati:
    print(element, rezultati[element])





