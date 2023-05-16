import re

string = r'\n and \r are escape sequences.'

result = re.findall('\n', string)
print(result)
