brojevi = [1, 1, 2, 3, 5, 8, 13]
iter_obj = iter(brojevi)

while True:
    try:
        el = next(iter_obj)
        print(el)
    except StopIteration:
        print("Dosli smo do kraja!")
        break
