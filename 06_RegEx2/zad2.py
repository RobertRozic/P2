import re

result = None

while not result:
    unos = input("Unesi datum rodjenja:")
    reg = '^(0?[1-9]|[12][0-9]|3[01])\.(0?[1-9]|1[0-2])\.(19\d\d|[2-9]\d{3})\.$'
    result = re.match(reg, unos)

    print(result)
