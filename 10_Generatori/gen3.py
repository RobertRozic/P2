def my_gen():
    n = 1
    print("Prvi put!")
    yield n

    n+=1
    print("Drugi put!")
    yield n

    n+=1
    print("Treci put!")
    yield n

novi = my_gen()

print(next(novi))
print(next(novi))
print(next(novi))
print(next(novi))
