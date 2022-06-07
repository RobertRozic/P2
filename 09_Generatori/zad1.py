def uvecaj(a):

  # Prvi put
  a = a + 1
  yield a
  
  # Drugi put
  a = a + 1
  yield a
  
  # Treci put
  a = a + 1
  yield a
  
my_gen = uvecaj(2)
print(type(my_gen))

for i in my_gen:
  print(i)
#print(next(my_gen))
#print(next(my_gen))
