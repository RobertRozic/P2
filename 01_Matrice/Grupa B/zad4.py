# Učitaj 2 matrice dimenzija rxs i formiraj treću
# kao zbroj prve dvije i ispisati je.
r = 2
s = 3

matrica1 = []
matrica2 = []
print('----Matrica 1-----')
for i in range(r):
    red = []
    for j in range(s):
        unos = int(input("Unesi broj"))
        red.append(unos)
    matrica1.append(red)

print('----Matrica 2-----')
for i in range(r):
    red = []
    for j in range(s):
        unos = int(input("Unesi broj"))
        red.append(unos)
    matrica2.append(red)

print('----Ispis Matrica 1-----')
for red in matrica1:
    print(red)

print('----Ispis Matrica 2-----')
for red in matrica2:
    print(red)

matrica3 = []
for i in range(r):
    red = [0]*s
    matrica3.append(red)
    for j in range(s):
        matrica3[i][j] = matrica1[i][j] + matrica2[i][j]

print('----Ispis Matrica 3-----')
for red in matrica3:
    print(red)





