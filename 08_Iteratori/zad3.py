my_dict = {
  'ime': 'Ivan',
  'prezime': 'Ivic',
  'godine': 20
}

dict_iter = iter(my_dict)

#dict_iter = iter(my_dict.values())

#print(my_dict[next(dict_iter)])
print(next(dict_iter))
print(next(dict_iter))
