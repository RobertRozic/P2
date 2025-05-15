'''
Napisati regex za provjeru unosa datuma.
Datum treba biti u formatu dd.MM.YYYY. (dan.mjesec.godina.)
Dan ne može biti veći od 31, mjesec od 12,
a godina ne smije biti manja od 1900.

Od korisnika tražiti unos rođendana
u ispravnom formatu i vratiti mu poruku o uspješnosti.

Kako bi prihvatili i jednoznamenkaste brojeve ?
'''

import re

regex = "^(0?[1-9]|[12][0-9]|3[01])\.(0?[1-9]|1[0-2])\.(19\d{2}|[2-9]\d{3})\.$"

result = None

while not result:
    tekst = input("Unesite datum rodjenja: ")

    result = re.search(regex, tekst)
    
print(result)
