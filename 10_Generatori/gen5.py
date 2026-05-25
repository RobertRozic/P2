def broji_do_beskonacnosti():
    a = 0
    while True:
        yield a
        a+=1
        if a > 1000:
            break

my_gen = broji_do_beskonacnosti()

'''
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
'''

for i in my_gen:
    print(i)

print(len(my_gen))




