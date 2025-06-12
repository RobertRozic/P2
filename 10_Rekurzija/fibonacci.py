def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

zbroj = 0
for i in range(10):
    broj = fibonacci(i)
    zbroj += broj
    print(broj)

print("Zbroj prvih 10 je:", zbroj)

