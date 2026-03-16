r = 2
s = 3
matrica = []

#for i in range(r):
#    red = [0]* s
#    matrica.append(red)

for i in range(r):
    red = [0]* s
    matrica.append(red)
    for j in range(s):
        #print(matrica[i][j])
        unos = int(input("Unesi broj:"))
        matrica[i][j] = unos

for red in matrica:
    print(red)
