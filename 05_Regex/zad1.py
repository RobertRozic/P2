import re

txt = "Ovo je predavanje programiranje 2."

result = re.findall("Programiranje 2", txt)

print(result)

