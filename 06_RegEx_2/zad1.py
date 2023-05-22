import re

result = []

result = False

result = None

while not result:
    unos = input("Unesi broj mobitela:")
    reg = '^$06[0-9]\/\d{3}-\d{3}$'
    result = re.match(reg, unos)

    print(result)

