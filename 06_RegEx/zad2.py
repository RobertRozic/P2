import re

txt = "Ovo je predavanje prograaaamiranje2"

#regex = "pr[eo]"

#regex = "pr..r"

#regex = "^Ovo"
#regex = "\AOvo"

#regex = "anje2$"

txt = "programiranje"

#regex = "progra*miranje"
#regex = "progra+miranje"
#regex = "progra?miranje"
#regex = "progra{1,3}miranje"

#regex = "p|r"
#regex = "pr(e|o)"

#regex = "ranje\."

result = re.findall(regex, txt)

print(result)
