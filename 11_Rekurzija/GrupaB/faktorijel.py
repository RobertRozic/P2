def faktorijel(n):
    if n == 0 or n == 1: # bazni slucaj
        return 1
    if n > 0: # rekurzivni slucaj
        return n * faktorijel(n-1)

rez = faktorijel(5)
# 5 * 4!
# 4! = 4 * 3 * 2 * 1
# 4! = 4 * 3!...

print(rez)

