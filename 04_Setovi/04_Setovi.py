myset = { "jabuka", "banana", "sljiva" }

print(myset)
print(type(myset))
print(len(myset))

myset = { "jabuka", "banana", "sljiva", "jabuka"}
lista = [ "jabuka", "banana", "sljiva", "jabuka"]
print(myset)
print(lista)

myset.add("naranca")
myset.remove("banana")
myset.add("Naranca")
print(myset)

# greska
#myset[2] = "tresnja"
