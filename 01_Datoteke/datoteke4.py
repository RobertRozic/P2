dat = open("ucenici.txt", "r")

linije = dat.readlines()

suma = 0
for linija in linije:
    ucenik = linija.split(',')
    ocjena = ucenik[2][:-1]
    suma += int(ocjena)

print("Zbroj ocjena je:", suma)
print("Prosjek:", suma/3)

dat.close()
