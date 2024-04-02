rezultati = {
 'Marko' : 56,
 'Ana' : 75,
 'Ivan' : 80,
 'Ivana' : 42,
 'Petar' : 92,
 'Mia' : 11,
 'Stjepan': 50
}

print(rezultati)

# Dohvacanje
#print(rezultati['Ivan'])

# Umetanje
rezultati['Robert'] = 60
#print(rezultati)

# Promjena/Azuriranje
rezultati['Ivan'] = 85
#print(rezultati['Ivan'])
#print(rezultati)

# Brisanje
del rezultati['Ivan']
print(rezultati)

# Provjera
if 'Stjepan' in rezultati: 
    print(rezultati['Stjepan'])

# Iteriranje
for key in rezultati:
    print(key, rezultati[key])















