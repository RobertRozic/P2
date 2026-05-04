import re

txt = "Ovo je predavanje programiranje2"

#result = re.split("r", txt)
result = re.sub("programiranje2", "matematika2", txt)

print(result)
