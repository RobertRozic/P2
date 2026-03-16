r = 2
s = 3
matrica = []

for i in range(r):
    red = []
    for j in range(s):
        unos = int(input("Unesi broj"))
        red.append(unos)
    matrica.append(red)

for red in matrica:
    print(red)

for red in matrica:
    for element in red:
        print(element)

for red in matrica:
    for element in red:
        print(element, end=" ")
    print()
