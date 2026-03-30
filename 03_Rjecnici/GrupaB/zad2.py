rezultati = {
  'Marko' : 56,
  'Ana' : 75,
  'Ivan' : 80,
  'Ivana' : 42,
  'Petar' : 92,
  'Mia' : 11
}

# Dohvacanje
print(rezultati['Ivan'])

# Umetanje
rezultati['Luka'] = 65
rezultati['luka'] = 70
#print(rezultati)

# Azuriranje
rezultati['Ivan'] = 85
#print(rezultati)

# Brisanje
del rezultati['luka']
print(rezultati)

# Provjera postojanja kljuca
print('Robert' in rezultati)
rezultati['Robert'] = 15
print('Robert' in rezultati)
if 'Robert' in rezultati:
    print(rezultati['Robert'])

#Iteriranje
for kljuc in rezultati:
    print(kljuc, rezultati[kljuc])






