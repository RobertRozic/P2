# Primjer lambda funkcije za obrtanje stringa
lambda s: s[::-1]

# Tu funkciju možemo dodijeliti nekoj varijabli i pozivati je kao inače
reverse1 = lambda s: s[::-1]
print(reverse1("Robert"))

# Što je jednako definiranju funkcije
def reverse2(s):
    return s[::-1]

print(reverse2("Robert"))

# No, to nije potrebno
print((lambda s: s[::-1])("Robert"))

forty_two_producer  = lambda: 42
print(forty_two_producer())

