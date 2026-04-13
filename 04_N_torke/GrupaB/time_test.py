import timeit

lista = timeit.timeit(stmt="[1,2,3,4,5,6]", number=100000000)
ntorka = timeit.timeit(stmt="(1,2,3,4,5,6)", number=100000000)

print("Kreiranje listi:", lista)
print("Kreiranje ntorki:", ntorka)
