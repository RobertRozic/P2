#for i in range(1, 6):
#    print(i)

def broji_do_pet():
    a = 1
    for i in range(1,6):
        yield a
        a += 1

novi = broji_do_pet()

print(next(novi))
print(next(novi))

