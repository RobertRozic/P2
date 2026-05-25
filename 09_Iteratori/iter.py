my_list = [1,2,3]
my_iter = iter(my_list)

# Sve metode unutar iter objekta
#for dl in dir(my_iter):
#  print(dl)

print(my_iter)

print(next(my_iter))
#print(next(my_iter))
#print(my_iter.__next__())

#print(next(my_iter))

#brojevi = [1, 1, 2, 3, 5, 8, 13]
#for broj in brojevi:
#    print(broj)

for broj in my_iter:
    print(broj)
