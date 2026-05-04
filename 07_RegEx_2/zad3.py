'''
Napisati regex za provjeru unosa vremena. Vrijeme treba biti u 24-satnom formatu hh:mm:ss. (sat:minute:sekunde)
Sati ne smiju biti veći od 23, a sekunde i minute od 59.

Od korisnika tražiti unos satnice alarma i ispisati rezultat.
Prorgram treba prihvaćati i jednoznamenkaste brojeve za sate ali ne i za minute i sekunde.
npr. 4:12:30 DA , 4:3:1 NE
'''

import re

result = None

regex = r"^(0?\d|1\d|2[0-3]):([0-5]\d):([0-5]\d)$"

while not result:
    txt = input("Unesi alarm:")

    result = re.search(regex, txt)
print(result.group())
