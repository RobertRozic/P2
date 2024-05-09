import re

txt = "Ovo je predavanje programiranje2 programiranje2"
result = re.findall("programiranje2", txt)

print(result)
