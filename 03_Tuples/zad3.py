# (ime, prezime, godine)
osoba = tuple(("Ivan", "Ivic", 20))

print(osoba)
ime = osoba[0]
prezime = osoba[1]
godine = osoba[2]

print(ime, prezime, godine)

# tuple way
ime, prezime, godine = osoba

print("Ime:", ime)
print("Prezime:", prezime)
print("Godine:", godine)

