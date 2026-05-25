def fibo(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
        '''
        pom = a
        a = b
        b = pom + b
        '''
        yield a

my_gen = fibo(10)

for i in my_gen:
    print(i)

    
