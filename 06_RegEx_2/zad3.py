import re

result = None

while not result:
    unos = input("Unesi alarm:")
    reg = '^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$'
    result = re.match(reg, unos)

    print(result)

