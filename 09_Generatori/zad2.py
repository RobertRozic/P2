# generator funkcija koja broji do 5
def broji_do_pet():
  for i in range(1, 6):
    yield i
    
my_gen = broji_do_pet()

#print(next(my_gen))
for i in my_gen:
  print(i)
  
# Funkcija koja broji u beskonacnost
def broji_u_beskonacnost():
  a = 0
  while True:
    yield a
    a+=1
    
broji = broji_u_beskonacnost()

print(next(broji))
print(next(broji))
print(next(broji))
print(next(broji))
print(next(broji))
print(next(broji))
print(next(broji))
print(next(broji))
print(next(broji))
print(next(broji))
print(next(broji))

#for i in broji:
#  print(i)
  
for i in range(1000):
  print(next(broji)) 


def potencije():
  a = 1
  while True:
    yield 2**a
    a += 1

pot = potencije()

print(next(pot))
print(next(pot))
print(next(pot))
print(next(pot))
