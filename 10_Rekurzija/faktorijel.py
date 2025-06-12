def faktorijel(n):
    print('pozvano')
    # Bazni slucaj
    if n == 1:# ili n == 0
        return 1
    # Rekurzivni slucaj
    else:
        return n * faktorijel(n-1)

print(faktorijel(5))
    
