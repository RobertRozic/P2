dat = open("primjer.txt", "r")

for i in range(3):
    tekst = dat.readline()
    #print(tekst, end='')
    print(tekst[:-1])

dat.close()


