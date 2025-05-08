imena = ['ivan', 'Antonio', 'Antonija', 'Anto', 'Marijan', 'Zvjezdan', 'Ivan', 'Mihaela', 'Ružica', 'Dorijan', 'Petra', 'Matej', 'Filip', 'Magdalena', 'Mate', 'Iva', 'Danis', 'Josip', 'Nebojša', 'Ante', 'Luka', 'Ante', 'Lorena', 'Ivan', 'Nikola', 'Ivan', 'Helena', 'Ivan', 'Gabrijela', 'Andrija', 'Regina', 'Petar', 'Dino', 'Marija', 'Semir', 'Gabriela', 'Borna', 'Filip', 'Krešimir', 'Ivana', 'Gabrijel', 'Vinko', 'Vinko', 'Romana', 'Viktorija', 'Mija', 'Matej', 'Vinko', 'Luka', 'Antea', 'Ivan', 'Ivan', 'Luka', 'Daniel', 'Nikola', 'Marko']

print(imena)

rezultati = {}

#{"Ivan": 2, "Antonio": 1}

for ime in imena:
    ime = ime.lower()
    if ime in rezultati:
        rezultati[ime] += 1
    else:
        rezultati[ime] = 1

print(rezultati)
