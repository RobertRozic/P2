dat = open("osobe.txt", "r")

linije = dat.readlines()

for linija in linije:
    zapis = linija[:-1].split(",")
    ime = zapis[0]
    prezime = zapis[1]
    godine = int(zapis[2])
    if godine > 19:
        print(zapis)
    #print(linija, end="")

dat.close()
