# Definiranje redaka i stupaca
r = 2
s = 3

# Inicijalizacija matrice
matrica = []

for i in range(r):
    # definiranje jednog reda
    red = [0] * s
    # dodavanje reda u matricu
    matrica.append(red)

#print(matrica)

# Izmjena prvog retka
matrica[0][0] = 3
matrica[0][1] = 5
matrica[0][2] = 7

# Izmjena drugog retka
matrica[1][0] = 1
matrica[1][1] = 4
matrica[1][2] = 2

# ispis matrice
for red in matrica:
    print(red)


