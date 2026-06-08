# Dodjeljivanje lambda funkcije nekoj varijabli
reverse = lambda s: s[::-1]
print(reverse("I am a string"))

# Sto je jednako ovome - ekvivalent
def reverse(s):
    return s[::-1]

# Lambda funckija bez imena - anonimna
rezultat = (lambda s: s[::-1])("Test")
print(rezultat)

# Lambda funkcija ne mora primati parametre
forty_two_producer = lambda: 42
rez = forty_two_producer()
print(rez)
