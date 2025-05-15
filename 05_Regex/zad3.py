import re

txt = "Ovo je predavanje programiranje2"

result = re.search("predavanje", txt)

print(result)
# Tuple pocetka i kraja, pcoetak i kraj
print(result.span(), result.start(), result.end())

# Dio stringa koji se podudara
print(result.group())

# String i regularni izraz
print(result.string, result.re)
