def broji_do_pet():
    n = 0
    while True:
        n += 1
        yield n

rez = broji_do_pet()

print(next(rez))
print(next(rez))
print(next(rez))
print(next(rez))
print(next(rez))
print(next(rez))
