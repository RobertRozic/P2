def faktorijel(n):
    if n == 1 or n == 0: # bazni slucaj
        return 1
    else: # rekurzivni slucaj
        return n * faktorijel(n-1)


rez = faktorijel(5)

print(rez)
