dat = open("brojevi.txt", "w")

dat.write(str(5) + "\n")
dat.write(str(6) + "\n")
dat.write(str(7) + "\n")

dat.close()

brojevi = open("brojevi.txt", "r")

zbroj = 0
for broj in brojevi:
    broj = int(broj)
    zbroj += broj

print("Zbroj brojeva je:", zbroj)

brojevi.close()
