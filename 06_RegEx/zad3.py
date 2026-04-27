import re

txt = "programiranje2"

#regex = r"\Apro"

#regex = r"\Bpro"
#regex = r"anje\b"

#regex = r"programiranje\d"

#regex = r"programiranje\D"

#regex = r"programiranje\s\S"

#regex = r"programiranje\w"

#regex = r"programiranje\W"

regex = r"ranje2\Z"

result = re.findall(regex, txt)

print(result)
