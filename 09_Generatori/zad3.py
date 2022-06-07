def fibo(n):
  a = 0
  b = 1
  for i in range(n):
    c = a + b
    yield c
    a = b
    b = c

my_gen = fibo(10)

for i in my_gen:
  print(i)
    
    
