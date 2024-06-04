def faktorijel(n):
    print("Unutar funckije:", n)
    # Bazni slucaj
    if n == 0: # ili n == 1
        return 1
    
    # Rekurzivni slucaj
    if n > 0:
        return n * faktorijel(n-1)

faktorijel(5)
