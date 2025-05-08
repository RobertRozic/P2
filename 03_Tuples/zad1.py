# Definiranje Liste
a = [1, 1, 2, 3, 5, 8, 13]

# Definiranje Tuple-a (ntorke)
b = (1, 1, 2, 3, 5, 8, 13)


# Određivanje duljine
print(len(a))
print(len(b))

print(type(a))
print(type(b))

# iteriranje
for broj in a:
    print(broj)
print("Treci element:", a[2])

for broj in b:
    print(broj)
print("Treci element:", a[2])

# Za usporedbu ćemo koristiti
# ugrađenu funkciju dir
for dl in dir(a):
  if dl[0] != '_':
    print (dl)
print ('----------')
for dl in dir(b):
  if dl[0] != '_':
    print (dl)

import sys

# Provjera veličine liste i ntorke
print(sys.getsizeof(a))
print(sys.getsizeof(b))

a[2] = 1111
print(a)

#b[2] = 1111
#print(b)

# Brzina kreiranja
import timeit

lista = timeit.timeit(stmt="[1,2,3,4,5,6]", number=100000000)
ntorka = timeit.timeit(stmt="(1,2,3,4,5,6)", number=100000000)

print("Lista:", lista)
print("Ntorka", ntorka)


