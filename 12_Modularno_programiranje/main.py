import fibonacci

rez1 = fibonacci.fib(5)
rez2 = fibonacci.ifib(10)

print("Peti:", rez1)
print("Deseti:", rez2)

import fibonacci

from importlib import reload
reload(fibonacci)

# Modul može biti učitan i kao skripta
if __name__ == "__main__":
    import sys
    print("Ucitano kao skripta")
    #rez = fibonacci.fib(int(sys.argv[1])) # Argument iz terminala
    print("Rezultat:", rez)

