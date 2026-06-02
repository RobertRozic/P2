def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

rez = gcd(1071, 462)

#print(1071%462)
#print(462%147)
#print(147%21)

print(rez)

