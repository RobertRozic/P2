# (ime, prezime, godine)
osoba = tuple(("Robert", "Rozic", 25))
osoba = "Robert", "Rozic", 25
osoba = ("Robert", "Rozic", 25)

print(osoba)

# List way
ime = osoba[0]
prezime = osoba[1]
godine = osoba[2]
print("Ime je:", ime)

# Tuple way
ime, prezime, godine = osoba
print("Ime je:", ime)

