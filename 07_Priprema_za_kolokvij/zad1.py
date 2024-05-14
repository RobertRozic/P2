tekst = "When we say that dictionaries are ordered,\
it means that the items have a defined order,\
and that order will not change. Unordered means\
that the items do not have a defined order, you\
cannot refer to an item by using an index."

tekst = tekst.lower()
rjecnik = {}

for slovo in tekst:
    rjecnik[slovo] = rjecnik.get(slovo, 0) + 1
    #if slovo in rjecnik:
    #    rjecnik[slovo] += 1
    #else:
    #    rjecnik[slovo] = 1

print(rjecnik)

# Provjera ima li engleska slova ili broj
import re
reg = '[xyw\d]'

if re.search(reg, tekst):
    print("Engleski tekst")

#lista = []
#for key in rjecnik:
#    par = key, rjecnik[key]
#    lista.append(par)
#print(lista)

# Popis keyeva, kljuceva
kljucevi = rjecnik.keys()
# Popis values, vrijednosti
vrijednosti = rjecnik.values()

# Kombinirano
items = rjecnik.items()
print(items)







