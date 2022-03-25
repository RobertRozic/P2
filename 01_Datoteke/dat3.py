dat = open("primjer.txt", "r")

linije = dat.readlines()

print(linije)

#for i in range(len(linije)):
#    print(linije[i], end='')

for linija in linije:
    print(linija, end='')

dat.close()
