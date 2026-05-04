'''
Napisati regex za provjeru unosa telefonskog broja
koji se mora sastojati od 3 grupe po 3 broja.
Prva i druga grupa brojeva su razdvojene kosom crtom,
dok su druga i treća razdvojene crticom.
Prvi broj mora biti 0. npr 063/123-456
Od korisnika zatražiti unos broja sve dok ne unese
broj u ispravnom formatu.
'''

import re

regex = r"^(06[1237])/(\d{3})-(\d{3})$"

result = None

while not result:
    txt = input("Unesi broj telefona:")
    result = re.search(regex, txt)

print(result.group())
