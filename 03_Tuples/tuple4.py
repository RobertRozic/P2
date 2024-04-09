# Dvije liste koje zelimo upariti
imena = ['Ivan', 'Ana', 'Pero']
godine = [21, 20, 22]

# zip objekt pretvaramo u listu
studenti = list(zip(imena, godine))

print(studenti) # lista tuple-a, odnosno ntorki

# Prolazak kroz listu studenata
for student in studenti:
    ime, godine = student # raspakiramo tuple
    print("Ime:", ime)
    print("Godine", godine)
