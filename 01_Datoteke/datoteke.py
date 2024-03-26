dat = open("ucenici.txt", "r")

# Citanje cijelog sadrzaja
#tekst = dat.read()
#print(tekst)

# Citanje liniju po liniju
#for i in range(3):
#    tekst = dat.readline()
#    tekst = tekst[:-1]
#    print(tekst)

linije = dat.readlines()

for linija in linije:
    print(linija[:-1])

dat.close()
