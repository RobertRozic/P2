lista = [1, 2, 3]
my_iter = iter(lista)

for dl in dir(my_iter):
 print(dl)
 
print(my_iter)

#for i in my_iter:
#  print(i)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# Kako izbjeci StopIter Exception
#print(next(my_iter))

lista = [1, 2, 3]
my_iter = iter(lista)

while True:
  try:
    element = next(my_iter)
    print(element)
  except StopIteration:
    print("Kraj.")
    break
    
string_iter = iter('iterator')
tuple_iter = iter(('Ivan', 'Ivic', 20))  

print(next(string_iter))
print(next(string_iter)) 
print(next(string_iter)) 
print(next(string_iter))   
    
print(next(tuple_iter))
print(next(tuple_iter))
print(next(tuple_iter))

my_dict = {
 'ime': 'Ivan',
 'prezime': 'Ivic',
 'godine': 20
}
dict_iter = iter(my_dict.values())

print(next(dict_iter))
print(next(dict_iter))
print(next(dict_iter))

