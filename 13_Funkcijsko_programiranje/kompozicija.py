# Kompozicija
def unutarnja():
    print("Ja sam funkcija unutarnja()!")

def vanjska(funkcija_argument):
    funkcija_argument()

vanjska(unutarnja)
