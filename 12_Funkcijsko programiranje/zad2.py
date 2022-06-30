def unutarnja():
 print("Ja sam funkcija unutarnja()!")
 
def vanjska(a):
 a()

vanjska(unutarnja)
