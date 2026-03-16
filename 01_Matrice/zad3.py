# Definiranje broja redaka
# i stupaca
r = 2
s = 3
matrica = []

for i in range(r):
    red = []
    for j in range(s):
        tekst = "Unesi broj na lokaciji "+str(i)+", "+ str(j)+ ": "
        unos = int(input(tekst))
        red.append(unos)
    matrica.append(red)

for red in matrica:
    print(red)

# Ispis
for red in matrica:
    for element in red:
        print(element, end=" ")
    print("")

for i in range(r):
    for j in range(s):
        print(matrica[i][j], end=" ")
    print()








