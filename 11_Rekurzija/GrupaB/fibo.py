def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fibo(n-1) + fibo(n-2)

rez = fibo(6)
print("Sesti broj je:", rez)

# Prvih x brojeva fibo niza
for i in range(1,20):
    print(fibo(i))
