my_list = [1, 2, 3, 5, 7]
my_iter = iter(my_list)

print(my_iter)


#for dl in dir(my_iter):
#    print(dl)
    
#print(my_iter)

#print(next(my_iter))
#print(next(my_iter))
#print(next(my_iter))
#print(next(my_iter))
#print(next(my_iter))
#print(next(my_iter))

while True:
    try:
        el = next(my_iter)
        print(el)
    except StopIteration:
        break

print("----------")
string_iter = iter('iterator')
tuple_iter = iter(('Ivan', 'Ivic', 20))
print(next(string_iter))
print(next(string_iter))
print(next(string_iter))
print(next(string_iter))

print("----------")
print(next(tuple_iter))
print(next(tuple_iter))
print("----------")

my_dict = {
 'ime': 'Ivan',
 'prezime': 'Ivic',
 'godine': 20
}

dict_iter = iter(my_dict.values())
print(next(dict_iter))
print(next(dict_iter))





