lista = [12, 5, 19]
print(lista)

lista[1] = 12
print(lista)

lista.append(7)
print(lista)

ntrorka = (12, 5, 19)
print(ntrorka)

# Greska! Tuple je immutable, ne moze se mijenjati
#ntrorka[1] = 12
print(ntrorka)

prazna_ntorka = ()
a = ("test",)
b = (1, 2)
c = (1, 2, 3)

print(prazna_ntorka, type(prazna_ntorka))
print(a, type(a))
print(b)
print(c)

a = 1,
b = 1, 2
c = 1, 2, 3

print(a, type(a))
print(b, type(b))
print(c, type(c))



