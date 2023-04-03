ime = input("Unesi ime: ")
prezime = input("Unesi prezime: ")
godine = input("Unesi godine: ")

osoba = [ime, prezime, godine]

zapis = ",".join(osoba)

dat = open("osobe.txt", "a")
dat.write(zapis + "\n")
dat.close()
