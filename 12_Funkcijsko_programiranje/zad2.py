def unutarnja():
    print("Ja sam funkcija unutarnja()!")

def vanjska(ime_funkcije):
    ime_funkcije()

vanjska(unutarnja)
