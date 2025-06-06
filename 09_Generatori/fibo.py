#Napraviti generator funkciju
#koja ispisuje prvih n brojeva Fibonaccijevog niza.
#Fibonaccijev niz je definiran kao
#niz brojeva gdje je nakon dvije prve vrijednosti
#svaki sljedeći broj zbroj zbroj dvaju prethodnika.
#tj. 0, 1, 1, 2, 3, 5, 8, 13, 21 …

def fibo():
    a = 0
    yield a
    b = 1
    yield b
    while True:
        c = a + b
        yield c
        a = b
        b = c

my_gen = fibo()
for i in range(7):
    print(next(my_gen))

        
