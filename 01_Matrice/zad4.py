# Učitaj 2 matrice dimenzija mxn
# i formiraj treću kao zbroj prve dvije i ispisati je.
r = 2
s = 3

matrica1 = []
matrica2 = []

# Unos prve matrice
print("-----Unos Matrica 1------")
for i in range(r):
    red = []
    for j in range(s):
        tekst = "Unesi broj na lokaciji "+str(i)+", "+ str(j)+ ": "
        unos = int(input(tekst))
        red.append(unos)
    matrica1.append(red)

# Unos druge matrice
print("-----Unos Matrica 2------")
for i in range(r):
    red = []
    for j in range(s):
        tekst = "Unesi broj na lokaciji "+str(i)+", "+ str(j)+ ": "
        unos = int(input(tekst))
        red.append(unos)
    matrica2.append(red)

print("-----Matrica 1------")
for red in matrica1:
    print(red)

print("-----Matrica 2------")
for red in matrica2:
    print(red)

# Zbrajanje u novu matricu
matrica3 = []
for i in range(r):
    red = [0] * s
    matrica3.append(red)
    for j in range(s):
        matrica3[i][j] = matrica1[i][j] + matrica2[i][j]

print("-----Matrica 3------")
for red in matrica3:
    print(red)





