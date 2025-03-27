'''
dat = open("primjer.txt", "r", encoding='utf-8')

#print(dat)
tekst = dat.read()

print(tekst)

dat.close()
'''

'''
# readline
dat = open("primjer.txt", "r", encoding='utf-8')

for i in range(3):
    linija = dat.readline()
    print(linija[:-1])

dat.close()
'''

# readlines
dat = open("primjer.txt", "r", encoding='utf-8')
linije = dat.readlines()
print(linije)
print("Broj linija:", len(linije))
for linija in linije:
    print(linija[:-1])

dat.close()




