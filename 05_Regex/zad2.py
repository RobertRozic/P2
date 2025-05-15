import re

txt = "Ovo je prrrrrredavanje programiranje 2."

#regex = "[pg]r"

#regex = "pr...amiranje"

#regex = "^Ovo"

#regex = "2\.$"

#regex = "pr*edavanje"

#regex = "pr+edavanje"

#regex = "pr?edavanje"

#regex = "pr{3}edavanje"

#regex = "pr{3,5}edavanje"

#regex = "p|r"

#regex = [abc]

#regex = "(a|b|c)"

regex = "[.]"

result = re.findall(regex, txt)

print(result)

result = re.split("\s", txt)

result = re.sub("\s", "5", txt)

print(result)



