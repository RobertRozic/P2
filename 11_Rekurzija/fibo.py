def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibo(n-1) + fibo(n-2)

rez = fibo(5)
#print(rez)

# Ispis prvih x brojeva
for i in range(1, 10):
    print(fibo(i))
