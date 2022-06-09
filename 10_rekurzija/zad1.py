def faktorijel(n):
  # Bazni slucaj
  if n == 0:
    return 1
  # Rekurzivni slučaj: n! = n * (n-1)!
  else:
    return n * faktorijel(n-1)

rezultat = faktorijel(10)

print(rezultat)
