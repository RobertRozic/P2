import sys

# Definiranje liste
print("-----Lista-----")
a = [1, 1, 2, 3, 5, 8, 13]
print(type(a))
print(len(a))
for el in a:
    print(el)
print("Element na indexu 2:", a[2])
for dl in dir(a):
  if dl[0] != '_':
    print (dl)

velicina_liste = sys.getsizeof(a)
print("Velicina liste:", velicina_liste)

# Definiranje ntorke
print("-----Ntorka-----")
b = (1, 1, 2, 3, 5, 8, 13)
print(type(b))
print(len(b))
for el in b:
    print(el)
print("Element na indexu 2:", b[2])
for dl in dir(b):
  if dl[0] != '_':
    print (dl)

velicina_ntorke = sys.getsizeof(b)
print("Velicina ntorke:", velicina_ntorke)


