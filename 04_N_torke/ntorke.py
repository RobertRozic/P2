# Definiranje liste
lista = [1, 1, 2, 3, 5, 8, 13]
print(lista)

# Definiranje tuple-a
ntorka = (1, 1, 2, 3, 5, 8, 13)
print(ntorka)

# Odredjivanje duljine
print(len(lista))
print(len(ntorka))

# Iteriranje i pristup el.
print("----Lista----")
for el in lista:
    print(el)
print("Element 2 liste:", lista[2])

print("----Ntorka----")
for el in ntorka:
    print(el)
print("Element 2 ntorke:", ntorka[2])

import sys

# Usporedba preko dir
print("----Lista----")
for dl in dir(lista):
  if dl[0] != '_':
    print (dl)
# Provjera velicine
velicina_liste = sys.getsizeof(lista)
print("Velcina liste:", velicina_liste)

print("----Ntorka----")
for dl in dir(ntorka):
  if dl[0] != '_':
    print (dl)
# Provjera velicine
velicina_ntorke = sys.getsizeof(ntorka)
print("Velicina n-torke:", velicina_ntorke)

