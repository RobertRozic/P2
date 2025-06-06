#Napraviti generator funkciju
#koja ispisuje potencije broja 2.

def potencije():
    a = 2
    e = 0
    while True:
        yield a**e
        e += 1

my_gen = potencije()
for i in range(5):
    print(next(my_gen))

