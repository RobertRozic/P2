def uvecaj(a):
 a += 1
 return a

def uvecajGen(a):
 a += 1
 yield a

rezultat = uvecaj(5)
rezultat2 = uvecajGen(5)
print(rezultat)
print(rezultat2)

print(type(rezultat))

print(next(rezultat2))
#print(next(rezultat2))

def my_gen():
    n = 0
    #yield n

    #n += 1
    #yield n

    #n += 1
    #yield n
    while True:
        yield n
        n += 1

rez = my_gen()
print(next(rez))
print(next(rez))
print(next(rez))
print(next(rez))
print(next(rez))

for el in rez:
    print(el)
