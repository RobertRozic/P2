#Napraviti generator funkciju
#koja broji do broja pet jedan po jedan
#svaki pozivom next metode.

def broji_do_pet():
    for i in range(1000):
        yield i+1

my_gen = broji_do_pet()

for i in my_gen:
    print(i)



