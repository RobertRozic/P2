brojevi = [1, 1, 2, 3, 5, 8, 13]

iter_obj = iter(brojevi)
string_iter = iter('iterator')
tuple_iter = iter(('Ivan', 'Ivic', 20))

while True:
    try:
        element = next(tuple_iter)
        print(element)
    except StopIteration:
        print("Nema vise brojeva")
        break
