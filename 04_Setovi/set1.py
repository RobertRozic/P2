# Setovi ne dopustaju duplikate za razliku od listi
my_set = {"jabuka", "banana", "sljiva", "jabuka"}
lista = ["jabuka", "banana", "sljiva", "jabuka"]
print(my_set)
print(lista)

print(type(my_set))
print(len(my_set))

# Dodavanje u set
my_set.add("naranca")
my_set.add("jagoda")
print(my_set)

# Brisanje iz seta
my_set.remove("banana")
my_set.discard("jabuka")
print(my_set)

# U setu ne mogu mijenjati elementi
# samo ubacivati i izbacivati
