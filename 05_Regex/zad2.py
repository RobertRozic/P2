import re

regex = '^(0?[1-9]|[12][0-9]|3[01])\.(0?[1-9]|1[0-2])\.(19[0-9]{2}|2[0-9]{3})\.$'

while 1:
    tekst = input("Unesite datum rodjenja: ")

    result = re.match(regex, tekst)

    if result:
        break

print("Uspjesan unos")
