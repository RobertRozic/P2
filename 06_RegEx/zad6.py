import re

txt = "Ovo je predavanje programiranje2"

regex = "predavanje"

result = re.search(regex, txt)

# Tuple pocetka i kraja, pocetak i kraj
print(result.span(), result.start(), result.end())

print(result.group())

print(result.string, result.re)




