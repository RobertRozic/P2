def uvecaj(a):
    a += 1
    yield a

broj = int(input("Unesi broj:"))

my_gen = uvecaj(broj)

print(my_gen)

rez = next(my_gen)
print("Uvecan broj je:", rez)

my_gen2 = uvecaj(rez)
rez = next(my_gen2)
print("Uvecan broj je:", rez)


