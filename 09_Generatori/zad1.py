def uvecaj(a):
  a += 1
  return a

print(uvecaj(5))
print(uvecaj(5))
print(type(uvecaj(5)))

def uvecaj(a):
  a += 1
  print('Prvi put')
  yield a

  a += 1
  print('Drugi put')
  yield a

  a += 1
  print('Treci put')
  yield a

  yield 15

my_gen = uvecaj(5)
print(type(my_gen))
#print(next(my_gen))
#print(next(my_gen))
#print(next(my_gen))

for el in my_gen:
    print(el)


