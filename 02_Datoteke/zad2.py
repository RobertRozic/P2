#dat = open("ispis.txt", "w")
dat = open("ispis.txt", "a")

dat.write("Ovo je prva linija\n")
dat.write("Ovo je druga linija\n")
dat.write("Ovo je treca linija\n")

dat.write(str(5) + "\n")
dat.write(str(6) + "\n")
dat.write(str(7) + "\n")

rezultat = 2 + 2
dat.write("Rezultat zbrajanja je: " + str(rezultat) + "\n")
dat.close()


