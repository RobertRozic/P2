import re

string = '3980 1356, 21021111'
pattern = '(\d{3}) (\d{2})'
match = re.search(pattern, string) 

if match:
  print(match.group())
else:
  print("pattern not found")
