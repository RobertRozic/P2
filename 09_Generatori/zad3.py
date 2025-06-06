#Napraviti generator funkciju
#koja može ispisivati brojeve u beskonačnost.

def beskonacnost():
    i = 0
    while True:
        yield i
        i += 1

#print(beskonacnost())
my_gen = beskonacnost()
for i in my_gen:
    print(i)
