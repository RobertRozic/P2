# Definiranje broja redaka
# i stupaca
r = 2
s = 3

# Inicijaziranje
matrica = []

for i in range(r):
    # Inicijaliziranje reda s stupaca
    red = [0] * s
    # Na matricu dodajemo red
    #matrica.append(red)
    # ili
    matrica += [red]

# Prvi red, indeks retka je 0
matrica[0][0] = 3
matrica[0][1] = 5
matrica[0][2] = 7

# Drugi red, indeks retka je 1
matrica[1][0] = 1
matrica[1][1] = 4
matrica[1][2] = 2

#print(matrica)
for red in matrica:
    print(red)








