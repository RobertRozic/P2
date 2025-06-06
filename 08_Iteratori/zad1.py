my_list = [1, 2, 3]
my_iter = iter(my_list)

#for dl in dir(my_iter):
#  print(dl)

print(my_iter)

print("Next:", next(my_iter))
#print(next(my_iter))
#print(next(my_iter))
#print(next(my_iter))

#print(my_iter.__next__())

for el in my_iter:
    print("U for:", el)

