# Definiranje Liste
a = [1, 1, 2, 3, 5, 8, 13]
#print(a)

b = (1, 1, 2, 3, 5, 8, 13)
#print(b)

# Provjera duljine
#print(len(a))
#print(len(b))

# Iteriranje
#for el in a:
#    print(el)

#for el in b:
#    print(el)


#print(a[2])
#print(b[2])

print("lista:")
for el in dir(a):
    if el[0] != '_':
        print(el)

print("tuple:")
for el in dir(b):
    if el[0] != '_':
        print(el)
        
import sys

print("Velicina liste:", sys.getsizeof(a))
print("Velicina tuple-a:", sys.getsizeof(b))

import timeit
lista = timeit.timeit(stmt="[1,2,3,4,5,6]", number=1000000)
ntorka = timeit.timeit(stmt="(1,2,3,4,5,6)", number=1000000)

print("Vrijeme kreiranja liste", lista)
print("Vrijeme kreiranja tuplea", ntorka)
