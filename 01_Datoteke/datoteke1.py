dat = open("ucenici.txt", "r", encoding="utf-8")

#tekst = dat.read()
#print(tekst)

#for i in range(3):
#    linija = dat.readline()
#    print(linija[:-1])

#linije = dat.readlines()

#print("Broj linija: ", len(linije))
#print(linije)

#for linija in linije:
#    print(linija[:-1])

print(dat)
for linija in dat:
    print(linija[:-1])
    
