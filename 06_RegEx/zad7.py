import re

string = '3980 1356, 210 21111'
pattern = '(\d{3}) (\d{2})'

match = re.search(pattern, string) 

if match:
  print(match.group())
else:
  print("pattern not found")

string = "\n and \r are escape sequences."
result = re.findall(r'[\n\r]', string)

print(result)

