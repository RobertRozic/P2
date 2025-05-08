rezultati = {
  'Marko' : 56,
  'Ana' : 75,
  'Ivan' : 80,
  'Ivana' : 42,
  'Petar' : 92,
  'Mia' : 11
}

print(rezultati)

# Dohvacanje
print("Ivan je ostvario", rezultati['Ivan'], "bodova.")

if rezultati['Ivan'] >= 50:
    print("Ivan je polozio ispit!")
else:
    print("Ivan nije polozio ispit")

# Umetanje
rezultati['Luka'] = 65
rezultati['luka'] = 70

print(rezultati)

# Azurirati
rezultati['Ana'] = 85
print(rezultati)

# Brisanje
del rezultati['Ivan']
print(rezultati)

del rezultati['Luka']
# Provjera postojanja kljuca
if 'Luka' in rezultati:
    print('Lukin ispit je upisan!')
else:
    print('Lukin ispit nije upisan!')


lista = ['Ivan', 'Pero', 'Luka']
for ime in lista:
    print(ime)

zbroj = 0
for element in rezultati:
    zbroj += rezultati[element]

print("Prosjecan broj bodova je:", round(zbroj/len(rezultati), 2))
