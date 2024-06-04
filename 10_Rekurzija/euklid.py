# Euklid gcd
#function gcd(a, b)
#    if b = 0
#        return a
#    else
#        return gcd(b, a mod b)
def gcd(a, b):
    if b == 0:
        return a
    else:
        print(a%b)
        # 462, 147
        # 147, 21
        # 21, 0
        return gcd(b, a % b)

print(gcd(1071, 462))
