import re

txt = "Ovo je predavanje programiranje 2."

regex = r"\s"

#result = re.split(regex, txt)

result = re.sub(regex, ".", txt)

print(result)


