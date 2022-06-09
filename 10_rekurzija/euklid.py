def euklid(a, b):
  print(a, b)
  if b == 0:
    return a
  else:
    return euklid(b, a%b)
    
rezultat = euklid(10, 20)
print(rezultat)

# 1. a = 10, b = 20
# 2. a = 20, b = 10
# 3. a = 10, b = 0
# return 10
