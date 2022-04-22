imena = ["Ivan", "Ana", "Marko"]
godine = [20, 19, 21]

osobe = list(zip(imena, godine))

print(osobe)

#for osoba in osobe:
    #ime, godine = osoba
#    print("Godine su:", godine)

for ime, godine in osobe:
    print("Godine su:", godine)




