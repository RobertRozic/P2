import re

tekst = 'programiranje'

regex = '^programiranje$'

result = re.findall(regex, tekst)

print(result)
