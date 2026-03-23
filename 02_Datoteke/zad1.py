ucenici = open("ucenici.txt", "r", encoding='utf-8')

#datoteka = open("brojevi.txt", "w")
#datoteka.close()

# Citav dokument
#tekst = ucenici.read()
#print(tekst)

#Linija po linija
'''
prva = ucenici.readline()
print(prva)

druga = ucenici.readline()
print(druga)

treca = ucenici.readline()
print(treca)
'''

'''
for i in range(3):
    tekst = ucenici.readline()
    print(tekst[:-1])
'''

'''
linije = ucenici.readlines()
print("Broj linija:", len(linije))

for linija in linije:
    print(linija, end="")
'''

for linija in ucenici:
    print(linija, end="")

ucenici.close()

