imena = [
    "Vedran", "Andrea", "Ana", "Marta", "Martina", "Iva", "Mirko", "Jakov", "Marko", "Mihaela",
    "Petar", "David", "Ivan", "Ivan", "Ana", "Dinko", "Petar", "Sanja", "Nikola", "Vinko", "Mihael",
    "Zdravko", "Patrik", "Kristijan", "Marin", "Kristijan", "Petar", "Mateo", "Bože", "Ivan-Kajo",
    "Matej", "Karlo", "Ana", "Lucija", "Bože", "Emanuel", "Ante-Roko", "Blaž", "Marijanela", 
    "Leonarda", "Antonio", "Ana-Maria", "Petra", "Leo", "Mario", "Marijana", "Jelena", "Stjepan",
    "Dario", "Matej"
]

rezultati = {}

for ime in imena:
    if ime in rezultati:
        rezultati[ime] += 1
    else:
        rezultati[ime] = 1

print(rezultati)

# imena koja se pojavljuju vise od jednom
for ime in rezultati:
    if rezultati[ime] > 1:
        print(ime, rezultati[ime])

