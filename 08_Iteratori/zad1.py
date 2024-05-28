my_list = [1, 2, 3]
my_iter = iter(my_list)

print(my_list)
print(my_iter)

# Popis ugradjenih funckija
#for el in dir(my_iter):
#    print(el)

# Iteriranje pomocu next
#print(next(my_iter))
#print(next(my_iter))
#print(next(my_iter))
#print(next(my_iter))

brojevi = [1, 1, 2, 3, 5, 8, 13]
#for broj in brojevi:
#    print(broj)

brojevi_iter = iter(brojevi)
while True:
    try:
        element = next(brojevi_iter)
        print(element)
    except StopIteration:
        print("StopIteration")
        break

    






