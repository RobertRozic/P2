def faktorijel(n):
    # Bazni slucaj +
    if n == 1: # umjesto n == 0 - optimizacija
        return 1
    # Rekurzivni slucaj // ++
    else:
        return n * faktorijel(n-1)

print(faktorijel(5))

