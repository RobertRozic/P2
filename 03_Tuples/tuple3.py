# definiranje ntorke
# (ime, prezime, godine)

osoba = ("Robert", "Rozic", 26)
#osoba = tuple(("Robert", "Rozic", 26))
print(osoba)

# Stari nacin
ime = osoba[0]
print("Ime:", ime)

prezime = osoba[1]
print("Prezime:", prezime)

godine = osoba[2]
print("Godine:", godine)

# tuple way
ime, prezime, godine = osoba
print("Ime:", ime)
print("Prezime:", prezime)
print("Godine:", godine)

# Raspakiravanje (unpack) tuplea
a, b, c = (1, 2, 3)
print("a:", a)
print("b:", b)


