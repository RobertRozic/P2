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
 'Marko' : 56,
 'Ana' : 75,
 'Ivan' : 80,
# 'ivan' : 50,
 'Ivana' : 42,
 'Petar' : 92,
 'Mia' : 11,
 'Marija': 55
}

#Dohvacanje
print(rezultati["Ivan"])

#Umetanje
rezultati["Luka"] = 57

#Azuriranje
rezultati["Marko"] = 65

#Brisanje
del rezultati["Ivan"]

#Provjera postoji li kljuc u rjecniku
if "Marija" in rezultati:
    print(rezultati["Marija"])

# Iteriranje
for student in rezultati:
    print(student, rezultati[student])
print(rezultati)

