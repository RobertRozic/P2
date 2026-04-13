imena = ["Ivan", "Ana", "Marko"]
prezimena = ["Ivic", "Anic", "Markic"]
godine = [20, 19, 21]

studenti = list(zip(imena, prezimena, godine))

for ime, prezime, godine in studenti:
    if godine > 19:
        print(ime, prezime, godine)
