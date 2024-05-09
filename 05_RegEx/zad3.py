import re

txt = "Ovo je predavanje programiranje2"
result = re.split("[aeiou]", txt.lower())

print(result)

txt = "Ovo je predavanje programiranje2"
result = re.sub("\s", "5", txt)

print(result)

