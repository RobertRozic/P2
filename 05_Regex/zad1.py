import re

regex = '^0[0-9]{2}/[0-9]{3}-[0-9]{3}'

while 1:
    tekst = input("Unesite broj u formatu 063/123-456: ")

    result = re.match(regex, tekst)

    if result:
        break

print("Uspjesan unos")
