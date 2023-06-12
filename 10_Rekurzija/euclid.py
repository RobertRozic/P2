def gcd(a, b):
    # bazni slucaj
    if b == 0:
        return a
    # rekurzivni slucaj
    else:
        return gcd(b, a % b)

print(gcd(1071, 462))
