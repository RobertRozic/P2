import re

result = None

while not result:
    unos = input("Unesi broj mobitela:")
    reg = '^06[123]\/\d{3}-\d{3}$'
    result = re.match(reg, unos)

    print(result)
