def potencije():
    a = 1
    while True:
        yield 2 ** a
        a += 1

my_gen = potencije()

'''
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
'''

for i in range(16):
    print(next(my_gen))
