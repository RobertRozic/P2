dat = open("ispis.txt", "w")

dat.write("Ovo je prva linija\n")
dat.write("Ovo je druga linija\n")

dat.write(str(5)+ "\n")
dat.write(str(10))

dat.close()
