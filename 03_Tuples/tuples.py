import sys

# Definiranje liste
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(a)

a[0] = 0
print(a)
#print(len(a))

#for element in a:
#    print(element)

#print("Element na trecem mjestu:", a[2])

#print(dir(a))

for dl in dir(a):
 if dl[0] != '_':
    print (dl)

print("----------")
# Definiranje ntorke
b = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
print(b)

#b[0] = 0
#print(b)

#print(len(b))

#for element in b:
#    print(element)

#print("Element na trecem mjestu:", b[2])

for dl in dir(b):
 if dl[0] != '_':
    print (dl)

# Provjera veličine liste i ntorke
print("Velicina liste:", sys.getsizeof(a))
print("Velicina ntorke:", sys.getsizeof(b))


#Brzina kreiranja
import timeit
lista = timeit.timeit(stmt="[1,2,3,4,5,6]", number=100000000)
ntorka = timeit.timeit(stmt="(1,2,3,4,5,6)", number=100000000)

print("Kreiranje listi:", lista)

print("Kreiranje ntorki", ntorka)
