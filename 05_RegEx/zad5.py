import re

string = '\n and \r are escape sequences.'

result = re.findall('\n', string)

print(result)
