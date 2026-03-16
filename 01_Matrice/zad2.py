# Definiranje broja redaka
# i stupaca
r = 2
s = 3
matrica = []

#for i in range(r):
#    red = [0] * s
#    matrica.append(red)

for i in range(r):
    red = [0] * s
    matrica.append(red)
    for j in range(s):
        tekst = "Unesi broj na lokaciji "+str(i)+", "+ str(j)
        matrica[i][j] = int(input(tekst))
        
for red in matrica:
    print(red)








