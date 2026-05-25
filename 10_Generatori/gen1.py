def uvecaj(a):
    a += 1
    return a

broj = int(input("Unesi broj:"))

rez = uvecaj(broj)

print("Uvecani broj je:", rez)

rez = uvecaj(rez)

print("Uvecani broj je:", rez)
