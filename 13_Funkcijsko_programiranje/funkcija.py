def func():
    print("Ja sam funkcija func()!")

func()

nova_func = func

nova_func()

print("test", func, 20)


# Pozivanje funkcije kao element niza
objekti = ["test", func, 20]
objekti[1]()

# Korištenje funkcije kao kljuca u rječniku
d = {"test": 1, func: 2, 20: 3}
print(d[func])

#print(func + func)








