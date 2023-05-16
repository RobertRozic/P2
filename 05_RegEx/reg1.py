import re
txt = "Ovo je predavanje programiranje2"
result = re.search("pred[abc]vanje", txt)

print(result)

print(result.span(), result.start(), result.end())

print(result.group())

print(result.string, result.re)


