def func():
    print("Ja sam funckija func()")

novo_ime = func

#func()
novo_ime()

print(novo_ime)

lista = [1, "test", novo_ime]

lista[2]()


