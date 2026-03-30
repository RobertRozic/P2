rezultati = {
  'Marko' : 56,
  'Ana' : 75,
  'Ivan' : 80,
  'Ivana' : 42,
  'Petar' : 92,
  'Mia' : 11
}

# Dohvacanje
print(rezultati['Mia'])
print(rezultati['Ivan'])

# Dodavanje vrijednosti
rezultati['Luka'] = 65

#print(rezultati)

# Azuriranje
rezultati['Ivan'] = 90
rezultati['ivan'] = 80
print(rezultati)

# Brisanje
del rezultati['ivan']

# Provjera kljuca
#rezultati['Robert'] = 15
print('Robert' in rezultati)
if 'Robert' in rezultati:
    print(rezultati['Robert'])

# Iteriranje
for student in rezultati:
    print(student, rezultati[student])









