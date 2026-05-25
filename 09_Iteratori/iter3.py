string_iter = iter('iterator')

print(next(string_iter))
print(next(string_iter))
print(next(string_iter))
print(next(string_iter))
print(next(string_iter))
print(next(string_iter))

tuple_iter = iter(('Ivan', 'Ivic', 20))
print(next(tuple_iter))
print(next(tuple_iter))
print(next(tuple_iter))

my_dict = {
  'ime': 'Ivan',
  'prezime': 'Ivic',
  'godine': 20
}
dict_iter = iter(my_dict)

novi_iter = iter(my_dict.values())

print(next(dict_iter))
print(next(dict_iter))

print(next(novi_iter))
print(next(novi_iter))




