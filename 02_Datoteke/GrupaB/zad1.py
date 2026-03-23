# Otvaranje i zatvaranje datoteke u w mode
# Stvori i spremi praznu datoteku
#dat = open("primjer.txt", "w")
dat = open("primjer.txt", "r", encoding="utf-8")

'''
tekst = dat.read()
print(tekst)
'''

'''
prva = dat.readline()
print(prva)

druga = dat.readline()
print(druga)

treca = dat.readline()
print(treca)
'''

'''
for i in range(3):
    linija = dat.readline()
    #print(linija[:-1])
    print(linija, end="")
'''
#dat = open("primjer.txt", "r", encoding="utf-8")
'''
sve_linije = dat.readlines()

print("Broj linija:", len(sve_linije))

for linija in sve_linije:
    print(linija, end="")

dat.close()
'''
for linija in dat:
    print(linija, end="")

dat.close()
