def vanjska():
    def unutarnja():
        print("Ja sam funkcija unutarnja()!")
    return unutarnja

vracena_funkcija = vanjska()
print(vracena_funkcija)
vracena_funkcija()
