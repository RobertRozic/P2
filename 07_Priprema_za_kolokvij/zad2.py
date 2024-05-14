imena = ["Ivan", "Iva", "Ana", "Ante", "Pero"]
prezimena = ["Ivic", "Peric", "Anic", "Antic", "Maric"]
godine = [1991, 1992, 1993, 1994, 1995]

#lista = []
#for i in range(5):
#    par = imena[i], prezimena[i], godine[i]
#    lista.append(par)
#print(lista)

# Kreiranje liste tupleova
lista2 = list(zip(imena, prezimena, godine))

# Iteriranje kroz listu tuple-ova
for ime, prezime, godina in lista2:
    if godina > 1993:
        print(ime, prezime)

# Zapisivanje u datoteku
dat = open("popis.txt", "w")
for ime, prezime, godina in lista2:
    dat.write(ime + ',' + prezime + ',' + str(godina) + '\n')
dat.close()

